FROM python
RUN pip install mysqlclient mysql-connector-python-rf
WORKDIR /app
COPY app.py ./
CMD python app.py