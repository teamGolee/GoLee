FROM ubuntu:18.04

ADD . /www
WORKDIR /www/src

RUN apt update \
    && apt install -y python3-dev python3-pip python3-setuptools
RUN apt install -y mysql-client
RUN pip3 install --upgrade pip
RUN pip3 install flask pymysql request flask_restplus pysafebrowsing uwsgi

#CMD ["/bin/bash", "start.sh"]
CMD ["python3", "main.py"]
