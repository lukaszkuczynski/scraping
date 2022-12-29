build:
	docker build . -t lukscraping/pyselenium

run:
	docker run \
		-ti --rm \
		-v ${PWD}/../selenium:/selenium \
		--entrypoint "/usr/bin/python3" \
		lukscraping/pyselenium \
		"/selenium/morizon.py"


bashrun:
	docker run \
		-ti --rm \
		-v ${PWD}/../selenium:/selenium \
		--entrypoint "/bin/bash" \
		lukscraping/pyselenium