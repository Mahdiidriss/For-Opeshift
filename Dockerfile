FROM docker.io/library/python
RUN pip install -r requirements.txt 
WORKDIR /app
COPY app.py ./
CMD python app.py
