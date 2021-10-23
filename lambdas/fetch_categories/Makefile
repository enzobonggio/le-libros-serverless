install: clean install_requirements_build copy zip
requirements: install_requirements

clean:
	rm -rf build
	rm -rf dist

build_path:
	mkdir build

install_requirements_build: build_path
	pip3 install -r requirements.txt -t build

install_requirements:
	pip3 install -r requirements.txt

copy:
	cp -R fetch_categories build/
	cp -R resources build/

build_dist:
	mkdir dist

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .
