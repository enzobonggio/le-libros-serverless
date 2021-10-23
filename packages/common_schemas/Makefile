default: clean install

clean:
	rm -rf build
	rm -rf le_libros_common_schemas.egg-info

install:
	pip3 install -r requirements.txt -t build
	pip3 install -e .
