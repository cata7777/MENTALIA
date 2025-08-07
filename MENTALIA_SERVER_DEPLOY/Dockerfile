FROM python:3.10-slim

WORKDIR /opt/mentalia

COPY . /opt/mentalia

RUN pip install --upgrade pip && \
    pip install flask gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
