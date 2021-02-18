FROM bitnami/python
RUN pip install flask && pip install mysqlclient && pip install mysql-connector-python-rf 
WORKDIR /app
COPY app.py ./
CMD python app.py