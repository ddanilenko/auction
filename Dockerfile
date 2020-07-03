FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD python manage.py migrate && \
    python manage.py loaddata initial_data && \
    python manage.py runserver 0:8000

EXPOSE 5000