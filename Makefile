VENV = venv
VBIN = $(VENV)/bin


all: start


clean:
	rm -rf venv
	rm -rf *.egg-info
	rm -rf __pycache__


$(VBIN)/python:
	python -m venv venv
	chmod +x venv/bin/activate
	./venv/bin/activate


start: $(VBIN)/python
	pip install -e .
	python botoven


.PHONY: all clean start
