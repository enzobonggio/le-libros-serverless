default: clean install test copy zip

clean:
	rm -rf build
	rm -rf dist
	rm -f .coverage

build_path:
	mkdir build

install: build_path
	pip3 install -r requirements.txt -t build

test:
	coverage run -m pytest

copy:
	cp -R fetch_categories build/
	cp -R resources build/

build_dist:
	mkdir dist

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .
