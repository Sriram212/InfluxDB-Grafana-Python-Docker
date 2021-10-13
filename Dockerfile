FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR C:\Users\Sriram\OneDrive\Desktop\InfluxDB

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY test.py .

CMD [ "python", "test.py" ]