FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /user_services

COPY . /user_services/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
