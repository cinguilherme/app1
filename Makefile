build-image:
	sudo docker build . -t app1:latest

run:
	sudo docker-compose up

run-local:
	python code/app.py


activate-virtual-env:
	source venv/bin/activate