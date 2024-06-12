set -u

while [ true ]; do
  sleep $thundershare_delete_delay
  echo "deleting storage at: $(date)"
  ./delete_storage_once.bash
done

