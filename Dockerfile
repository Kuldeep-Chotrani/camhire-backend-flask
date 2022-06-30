FROM continuumio/anaconda3:2022.05

ADD . /code
WORKDIR /code

ENTRYPOINT ["python","app.py"]
