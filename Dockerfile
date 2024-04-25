FROM vinnix/ubuntu_base:v10

MAINTAINER "Vinícius Schmidt"

EXPOSE 5100
EXPOSE 80

COPY . /opt

CMD ["/opt/bin/container_loop.sh"] 

