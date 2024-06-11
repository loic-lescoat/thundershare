
# set container name to be equal to name of directory of project
container_name := $(notdir $(CURDIR))
PORT := 8000

build:
	docker build --build-arg PORT=$(PORT) -t $(container_name) .
run:
	docker run -d -p $(PORT):$(PORT) -v thundershare-volume:/deploy/storage $(container_name)


