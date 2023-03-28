# syntax=docker/dockerfile:1
FROM python
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
EXPOSE  8000