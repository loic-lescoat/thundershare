build:
	docker build -t tmp .
run:
	docker run -p 8000:8000 tmp
