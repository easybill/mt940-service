build:
	docker build -t mt940-py-service .
run:
	docker run -p 8000:8000 --rm -it mt940-py-service
