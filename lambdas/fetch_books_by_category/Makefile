install: clean install_requirements copy zip
test: requirements coverage

clean:
	rm -rf build
	rm -rf dist

build_path:
	mkdir build

install_requirements: build_path
	pip3 install -r requirements.txt -t build

requirements:
	pip3 install -r requirements.txt

coverage:
	coverage run -m pytest

copy:
	cp -R fetch_books_by_category build/
	cp -R resources build/

build_dist:
	mkdir dist

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .
