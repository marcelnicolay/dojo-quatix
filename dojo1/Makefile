clean:
	@echo "Cleaning up build and *.pyc files..."
	@find . -name '*.pyc' -exec rm -rf {} \;
	@rm -rf build

unit: clean
	@echo "Running torneira unit tests..."
	@export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/sudoku  &&  \
		nosetests -s --verbose --with-coverage --cover-package=sudoku tests/*
