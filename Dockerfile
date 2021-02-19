FROM docker.io/library/python
RUN pip install flask mysqlclient mysql-connector-python-rf 
WORKDIR /app
COPY app.py ./
CMD python app.py