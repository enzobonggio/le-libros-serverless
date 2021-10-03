default: clean install copy zip

clean:
	rm -rf build
	rm -rf dist

build_path:
	mkdir build

install: build_path
	pip3 install -r requirements.txt -t build

copy:
	cp -R src/* build/

build_dist:
	mkdir dist

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .

