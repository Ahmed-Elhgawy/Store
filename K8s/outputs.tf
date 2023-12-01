output "eksClusterRole" {
  value = aws_iam_role.eksClusterRole.arn
}

output "AmazonEKSNodeRole" {
  value = aws_iam_role.AmazonEKSNodeRole.arn
}

output "endpoint" {
  value = aws_eks_cluster.my-cluster.endpoint
}

output "kubeconfig-certificate-authority-data" {
  value = aws_eks_cluster.my-cluster.certificate_authority[0].data
}