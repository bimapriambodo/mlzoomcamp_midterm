From python:3.8.12-slim

COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/

ADD ./requirements.txt /usr/app/requirements.txt
RUN pip install -r requirements.txt
ADD . /usr/app/

CMD python predict.py