FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=src/backend/api_app.py

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
