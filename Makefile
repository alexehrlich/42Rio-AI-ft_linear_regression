all: setup

setup:
	@virtualenv venv
	@. venv/bin/activate && pip install -r ./requirements.txt

training:
	. venv/bin/activate && python3 training.py

prediction:
	. venv/bin/activate && python3 prediction.py
