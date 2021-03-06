#
# Postgres container
#

docker kill chlex-postgres
docker rm chlex-postgres

docker build -t 0xffea/chlex-postgres - <<EOL
FROM ubuntu:14.04
MAINTAINER David Höppner <0xffea@gmail.com>

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get -qy install		\
	postgresql

EXPOSE 5432

ADD https://raw.github.com/beijingren/dedalus-infrastructure/master/linux-docker/scripts/start-postgres.sh /root/start-postgres.sh
RUN chmod 0755 /root/start-postgres.sh

CMD ["/root/start-postgres.sh"]
EOL

docker run -d --name chlex-postgres -p 5432:5432 -v /docker:/docker:rw -t 0xffea/chlex-postgres
