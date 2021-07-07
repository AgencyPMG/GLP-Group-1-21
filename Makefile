build:
	docker build -t semfeed-api:latest .
up:
	docker run -dp 5000:5000 semfeed-api
stop:
	docker stop sapi
clear:
	docker container prune
