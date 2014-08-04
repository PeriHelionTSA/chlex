#
# Django container
#

docker kill chlex
docker rm chlex

docker build -t 0xffea/chlex-django - <<EOL
FROM ubuntu:14.04
MAINTAINER David Höppner <0xffea@gmail.com>

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -qy install		\
	python-django		\
	python-psycopg2		\
	python-pip		\
	git


RUN mkdir -p /home/chlex
WORKDIR /home/chlex

RUN git clone https://github.com/PeriHelionTSA/chlex.git
WORKDIR /home/chlex/chlex

EXPOSE 8010

CMD python manage.py syncdb ; python manage.py runserver 0.0.0.0:8001
EOL

docker run -d -p 8010:8010 --name chlex --link postgres:db -v /docker:/docker:rw -t 0xffea/chlex-django
