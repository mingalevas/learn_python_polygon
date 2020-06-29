FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
RUN python manage.py makemigrations && python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
