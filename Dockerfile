FROM daocloud.io/python:2.7
MAINTAINER imsilence@outlook.com
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir /code
WORKDIR /code
COPY . /code
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh
EXPOSE 8888

CMD /code/entrypoint.sh
