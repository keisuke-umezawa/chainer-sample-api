.PHONY: api all black build

MAKEFILE_PATH := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
PROJECT_ROOT := $(abspath $(MAKEFILE_PATH)/)

api:
	docker-compose run api pipenv run dev

all:
	docker-compose up

build:
	docker-compose build

black:
	docker pull unibeautify/black
	docker run -it -v $(PROJECT_ROOT):/workdir -w /workdir unibeautify/black --line-length 80 /workdir
