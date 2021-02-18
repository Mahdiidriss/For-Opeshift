FROM python
RUN pip install mysqlclient
WORKDIR /app
COPY app.py ./
CMD python app.py