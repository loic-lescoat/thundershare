# TODO set container name to be equal to name of directory of project
container_name := $(notdir $(CURDIR))
PORT := 8000
VOLUME_NAME = thundershare-volume

build:
	docker build --build-arg PORT=$(PORT) -t $(container_name) .
run:
	docker run -d -p $(PORT):$(PORT) -v $(VOLUME_NAME):/deploy/storage $(container_name)

# TODO don't hardcode storage dir
enter:
	docker run -v $(VOLUME_NAME):/deploy/storage -it $(container_name) bash
kill:
	docker kill `docker ps -q --filter "ancestor=$(container_name)"`
	sleep 1 # may get "port already allocated" error without this
	$(MAKE) build
	$(MAKE) run

	


