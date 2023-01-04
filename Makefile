build:
	docker build \
	 	-t lukscraping/pyselenium_arm \
		-f docker/Dockerfile .

buildcloud:
	docker build \
	 	-t lukscraping/pyselenium \
		-f docker/Dockerfile_cloud .

morirun:
	docker run \
		-ti --rm \
		-v ${PWD}/../selenium:/selenium \
		--entrypoint "/usr/bin/python3" \
		lukscraping/pyselenium \
		"/selenium/morizon.py"

run:
	docker run \
		-ti --rm \
				lukscraping/pyselenium_arm

bashrun:
	docker run \
		-ti --rm \
		-v ${PWD}/../selenium:/selenium \
		--entrypoint "/bin/bash" \
		lukscraping/pyselenium