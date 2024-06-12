
# set container name to be equal to name of directory of project
container_name := $(notdir $(CURDIR))

build:
	docker build -t $(container_name) .
run:
	docker run -v thundershare-volume:/storage -it $(container_name)
