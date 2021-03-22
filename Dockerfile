FROM python:3.9.1

ENV PYTHONUNBUFFERED 1

COPY . /django_learning/
WORKDIR /django_learning/django_proyect/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["mysite/manage.py", "runserver" , "0.0.0.0:8000"]
