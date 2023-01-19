FROM python:latest

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . . 

ENV SECRET_KEY='django-insecure-z9o^ay=(^5=(w2!^3^-8e7+)qct3-kdee8#c5o07fcw)pn10)#'
ENV ENV='DEV'

ADD . ${ENV}
ADD . ${SECRET_KEY}

CMD ["gunicorn", "core.wsgi:application",  "--bind", "0.0.0.0:8000"]