init:
	pip install -r requirements.txt

test:
	py.test tests
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

coverage:
	py.test --verbose --cov-report term --cov=hack tests

clean:
	rm -rf py_nand2tetris.egg-info

update:
	echo "use https://github.com/jazzband/pip-tools"; \
	if type pip-compile > /dev/null 2>&1; then \
		echo 'found'; \
		pip-compile --output-file requirements.txt requirements.in \
	else \
		echo 'not found'; \
		pip install --upgrade pip; \
		pip install pip-tools; \
		pip-compile --output-file requirements.txt requirements.in; \
	fi

install:
	echo "use https://github.com/jazzband/pip-tools"; \
	if type guile > /dev/null 2>&1; then \
		echo 'found'; \
	else \
		echo 'not found'; \
		brew install guile; \
		guile; \
	fi


.PHONY: init test	
