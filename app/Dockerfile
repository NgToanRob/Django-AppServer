# pull official base image
FROM python:3.9.6-alpine

LABEL author.name="Toan Nguyen" \
author.email="nguyentoan10601@gmail.com"

# # set work directory
# WORKDIR /usr/src/app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # copy project
# COPY . .

# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev \
#     # install dependencies
#     && pip install --upgrade pip \
#     # COPY ./requirements.txt .
#     && pip install -r requirements.txt \
#     # copy entrypoint.sh
#     # COPY ./entrypoint.sh .
#     && sed -i 's/\r$//g' /usr/src/app/entrypoint.sh \
#     && chmod +x /usr/src/app/entrypoint.sh


# # run entrypoint.sh
# ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

