clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@rm -rf build

unit: clean
	@export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/  &&  \
		nosetests -s --verbose --with-coverage --cover-package=* tests/*
