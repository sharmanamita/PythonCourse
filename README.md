# cmds for installing Django

python -m pip install --upgrade pip
python -m pip install django

# how to create python environment and activate one

STEP1: python -m venv rentnpay
STEP2: activate the venv by running rentnpay/scripts/activate.bat or just run activate file.
STEP3: it has pip to install packages

# how to install django/flask/fastAPI

pip install flask
pip install django
pip install fastapi uvicorn
pip install mysql-connector-python
pip install jwt

# To track the librabries versions we can create requirements.txt using

pip freeze > requirements.txt

# this will create new file and will all entries in files (similar to package-lock.json)

# Unistall all packages listed in requirements.txt

pip uninstall -r requirements.txt -y

# Install everything from requirements.txt

pip install -r requirements.txt
