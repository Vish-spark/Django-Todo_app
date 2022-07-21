From python:3.11.0b4-bullseye

COPY requirements.txt /Todo_app/requirements.txt

WORKDIR /Todo_app

RUN pip install -r requirements.txt

COPY . /Todo_app

RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8000"]



