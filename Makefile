all: setup

setup:
	@virtualenv venv
	@. venv/bin/activate && pip install -r ./requirements.txt

training:
	@python3 training.py

prediction:
	@python3 prediction.py
