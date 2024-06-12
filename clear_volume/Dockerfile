FROM busybox

WORKDIR /deploy

COPY delete_storage_periodically.bash delete_storage_once.bash .

# seconds
ENV thundershare_delete_delay=60

CMD ./delete_storage_periodically.bash
