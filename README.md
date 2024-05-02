# Python/Flask exercises and study 

## Objectices and challanges

Challange: Implement a system that allows a user to upload images through a REST backend application in any language. 
           Using a simple front end, later on to communicate with it. No authentication for now. 

Objectice: Learn more about python and webframework flask using REST techniques

## Approach used:

	* Mapping activities on https://github.com/users/vinnix/projects/2/views/1 (Kanban board)
	* Saving links of interest and studying the problem: https://github.com/vinnix/dbtune_interview/blob/main/docs/ResourceMaterial.md
	* Studying Docker and its mechanisms to create: https://gist.github.com/vinnix/d6b7523753ae72d66c3548b54ce59918


## Decisions made (technical and not):
	* To use python3/Flask
	* PostgreSQL 16.2 built from strach inside my woen Docker image
	* ByteA column to store images
	* To go as fast as possible however careful think on each step
	* To not reinvent the weel and to take benefit of the common problem already mapped around
	* To understand each part of the code and architecture from the fundations

## Environment:
	* Virtualbox running CentOS 9 image
	* For now one single docker container built from stratch, using a Ubuntu Focal simple image



## Install and run:

``` 
	git clone https://github.com/vinnix/dbtune_interview.git
	cd dbtune_interview
	docker pull vinnix/ubuntu_image:v15
	
	docker create vinnix/ubuntu_image:v15
	docker start <container id>
	docker exec -it <container id> /bin/bash
``` 
Service will be at:
	http://ip:5100/

Test(curl based):
	bin/put_image.sh


## Next steps:

	[X] Align code with deployment on container
	[ ] More details about th eproject at:
	    https://github.com/users/vinnix/projects/2/views/1
