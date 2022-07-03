FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /order_services

COPY . /order_services/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
