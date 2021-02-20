FROM docker.io/library/python
WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt 
CMD python app.py
