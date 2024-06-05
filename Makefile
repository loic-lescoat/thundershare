run:
	flask --app app run -h 0.0.0.0 -p 8000

debug:
	flask --app app run -h 0.0.0.0 -p 8000 --debug
