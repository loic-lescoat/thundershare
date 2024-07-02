# Deletes all files older than PERIOD minutes
PERIOD=1440 # one day in minutes
rm $(find . -mmin +$PERIOD)

