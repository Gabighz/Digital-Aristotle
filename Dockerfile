FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /digital-aristotle
WORKDIR /digital-aristotle
COPY requirements.txt /digital-aristotle/
RUN pip install -r requirements.txt
COPY . /digital-aristotle/