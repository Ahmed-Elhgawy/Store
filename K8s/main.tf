terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "my-vpc" {
  source             = "./modules/network"
  cidr               = var.cidr
  availability_zones = var.availability_zones
}

resource "aws_iam_role" "eksClusterRole" {
  name = "eksClusterRole"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "eks.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  })

  tags = {
    tag-key = "Amazon EKS - Cluster role"
  }
}

resource "aws_iam_role" "AmazonEKSNodeRole" {
  name = "AmazonEKSNodeRole"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "ec2.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      }
    ]
  })

  tags = {
    tag-key = "Amazon EKS - Node role"
  }
}

data "aws_iam_policy" "AmazonEKSClusterPolicy" {
  arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
}

data "aws_iam_policy" "AmazonEC2ContainerRegistryReadOnly" {
  arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

data "aws_iam_policy" "AmazonEKS_CNI_Policy" {
  arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
}

data "aws_iam_policy" "AmazonEKSWorkerNodePolicy" {
  arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
}

resource "aws_iam_policy_attachment" "eksClusterRole-attach" {
  name       = "eksClusterRole-attachment"
  roles      = [aws_iam_role.eksClusterRole.name]
  policy_arn = data.aws_iam_policy.AmazonEKSClusterPolicy.arn
}

resource "aws_iam_policy_attachment" "AmazonEKSNodeRole-attach" {
  name = "AmazonEKSNodeRole-attachment"
  for_each = toset([
    data.aws_iam_policy.AmazonEC2ContainerRegistryReadOnly.arn,
    data.aws_iam_policy.AmazonEKS_CNI_Policy.arn,
    data.aws_iam_policy.AmazonEKSWorkerNodePolicy.arn
  ])

  roles      = [aws_iam_role.AmazonEKSNodeRole.name]
  policy_arn = each.value
}

resource "aws_eks_cluster" "my-cluster" {
  name     = "my-cluster"
  role_arn = aws_iam_role.eksClusterRole.arn

  vpc_config {
    subnet_ids = module.my-vpc.public_subnets
  }

  depends_on = [
    aws_iam_policy_attachment.eksClusterRole-attach
  ]
}

resource "aws_eks_node_group" "node-group1" {
  cluster_name    = aws_eks_cluster.my-cluster.name
  node_group_name = "node-group1"
  node_role_arn   = aws_iam_role.AmazonEKSNodeRole.arn
  subnet_ids      = module.my-vpc.public_subnets

  scaling_config {
    desired_size = 1
    max_size     = 2
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

  # Ensure that IAM Role permissions are created before and deleted after EKS Node Group handling.
  # Otherwise, EKS will not be able to properly delete EC2 Instances and Elastic Network Interfaces.
  depends_on = [
    aws_iam_policy_attachment.AmazonEKSNodeRole-attach
  ]
}