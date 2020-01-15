build-image:
	docker build . -t app1:latest

run:
	docker run app1:latest


activate-virtual-env:
	source venv/bin/activate