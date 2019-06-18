FROM python:3.7-slim-stretch
MAINTAINER Mohsin Mohammed "mohsinmohammed25@outlook.com"
ARG api_token
RUN mkdir /app
COPY ./script/ /app
COPY requirement.txt /app
RUN chmod 755 -R /app
WORKDIR /app
RUN pip install -r requirement.txt
CMD ["python"]