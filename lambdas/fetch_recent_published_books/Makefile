install: clean install_requirements copy zip

clean:
	rm -rf build
	rm -rf dist

build_path:
	mkdir build

install_requirements: build_path
	pip3 install -r requirements.txt -t build

copy:
	cp -R fetch_recent_published_books build/
	cp -R resources build/

build_dist:
	mkdir dist

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .
