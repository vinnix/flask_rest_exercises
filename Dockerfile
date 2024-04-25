FROM vinnix/ubuntu_base:v7

MAINTAINER "Vinícius Schmidt"

EXPOSE 5100
EXPOSE 80


CMD ["/opt/bin/container_loop.sh"] 

