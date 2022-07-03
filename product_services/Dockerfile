FROM python

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /product_services

COPY . /product_services/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
