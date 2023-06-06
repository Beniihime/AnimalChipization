FROM python:3.10.6-alpine

WORKDIR /animal-chipization

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev



COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .



CMD ["python", "manage.py", "runserver", "webapi:8080"]


ENTRYPOINT ["/animal-chipization/entrypoint.sh"]
