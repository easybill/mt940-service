FROM python:3.7

MAINTAINER patrick@romowicz.de

RUN pip install mt-940

EXPOSE 8000

COPY app /usr/local/app

CMD ["python","/usr/local/app/server.py"]