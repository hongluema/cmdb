FROM daocloud.io/python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir /code
WORKDIR /code
COPY . /code
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh
EXPOSE 80

CMD /code/entrypoint.sh
