all: setup training

setup:
	@echo "Installing the dependencies"
	@python3 -m venv venv
	@. venv/bin/activate && pip install -r ./requirements.txt

training:
	@echo "Running the training program..."
	@. venv/bin/activate && python3 training.py

prediction:
	@echo "Running the prediction program..."
	@. venv/bin/activate && python3 prediction.py
