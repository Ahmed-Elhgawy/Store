FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y && \ 
    apt-get install python3 -y && \
    apt-get install python3-pip -y && \
    apt-get install nginx -y

RUN pip install django

RUN mkdir -p /usr/src/app
COPY src/store_project/ /usr/src/app

COPY src/default.conf /etc/nginx/sites-available/store_project
RUN ln -s /etc/nginx/sites-available/store_project /etc/nginx/sites-enabled

WORKDIR /usr/src/app

RUN python3 manage.py collectstatic
RUN chmod -R 755 /usr/src/app/staticfiles/

RUN pip install pytz && \
    pip install tzdata

RUN service nginx restart

CMD python3 manage.py runserver 0.0.0.0:8000
