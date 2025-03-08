
build: build-frontend build-backend
run: run-frontend run-backend
start: start-frontend start-backend
stop: stop-frontend stop-backend

build-frontend:
	docker build -t react-app frontend
build-backend:
	docker build -t django-app backend

run-frontend:
	docker run -d -p 3000:3000 --name react-app  react-app
run-backend:
	docker run -d -p 8000:8000  --name django-app django-app

start-frontend:
	docker start  react-app
start-backend:
	docker start django-app

stop-frontend:
	docker stop react-app
stop-backend:
	docker stop django-app

restart: stop start