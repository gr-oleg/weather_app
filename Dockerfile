FROM python:3.10-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN /opt/venv/bin/python3 -m pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python"]