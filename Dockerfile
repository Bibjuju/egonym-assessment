FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opencv-python-headless==4.5.3.56

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]