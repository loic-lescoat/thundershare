PERIOD=1440 # one day in minutes
rm $(find . -mmin +$PERIOD)

