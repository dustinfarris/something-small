develop:
	pip install -e "file://`pwd`#egg=something_small[tests]"

test:
	pytest

watch:
	ptw


.PHONY: develop test watch
