
build:
	docker build -t django-app backend
	docker build -t react-app frontend

run:
	docker run -d -p 8000:8000  --name django-app django-app
	docker run -d -p 3000:3000 --name react-app  react-app
start:
	docker start django-app
	docker start  react-app

stop:
	docker stop django-app
	docker stop react-app

restart: stop start