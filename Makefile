
# set container name to be equal to name of directory of project
container_name := $(notdir $(CURDIR))

build:
	docker build -t $(container_name) .
run:
	docker run -p 8000:8000 $(container_name)
