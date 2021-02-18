FROM python
RUN pip install mysqlclient mysql-connector-python-rf flask
WORKDIR /app
COPY app.py ./
CMD python app.py