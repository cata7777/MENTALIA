FROM python:3.10-slim

WORKDIR /opt/mentalia

COPY . /opt/mentalia

RUN pip install --upgrade pip && \
    pip install llama-cpp-python flask gunicorn

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
