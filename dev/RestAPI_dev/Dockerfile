FROM ubuntu:20.04

RUN apt-get update && apt-get install python3-pip 

WORKDIR /djangoproject
ADD . /djangoproject
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3", "manage.py", "runserver","0.0.0.0:5000"]