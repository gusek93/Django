FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip 

WORKDIR /workAutomation
ADD . /workAutomation
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--bin", "0:5000","workAutomation.wsgi:application"]