FROM python
RUN pip install pip install mysql-connector-python-rf
WORKDIR /app
COPY app.py ./
CMD python app.py