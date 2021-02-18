FROM python
RUN pip install mysqlclient
RUN pip install mysql-connector-python-rf 
RUN pip install flask
WORKDIR /app
COPY app.py ./
CMD python app.py