install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py

format:
	black *.py


lint:s
	pylint --disable=R,C main.py

deploy:
	python ./main.py

show_pacs:	
	pip list && pip freeze	

all: install lint tests