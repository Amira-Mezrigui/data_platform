FROM python:3.9-slim
WORKDIR /work/app_flask
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]