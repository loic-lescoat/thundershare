
# set container name to be equal to name of directory of project
container_name := $(notdir $(CURDIR))
PORT := 8000

build:
	docker build --build-arg PORT=$(PORT) -t $(container_name) .
run:
	docker run -p $(PORT):$(PORT) $(container_name)
