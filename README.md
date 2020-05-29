# GFU Online Meeting 2020
This notebook is the basis for an online meeting hosted by the GFU Cyrus AG. It gives an hands-on overview to Data Science from data exploration to model deplyoment.

## Setup
To run this Jupyter notebook a Python Package Manager like conda or pip is needed.

### Using pip 
pip install -r requirements.txt

### To start the notebook
python -m jupyter notebook

### To run the model service
export FLASK_APP=app/__init__.py
flask run
