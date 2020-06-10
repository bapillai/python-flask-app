# Steps to setup and run this python project

>python3 -m venv env
>source env/bin/activate
>touch .gitignore requirements.txt
>python -m pip install Flask==1.1.1
>python -m pip freeze > requirements.txt
>python app.py

#To use environment variables in the application we use autoenv

>deactivate
>pip install autoenv==1.0.0
>touch .env

#Copy the following to the .env file
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"

#Update your .bashrc file by running the following:
> echo "source `which activate.sh`" >> ~/.bashrc
>source ~/.bashrc
>python app.py