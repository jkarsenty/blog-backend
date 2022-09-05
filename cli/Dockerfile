FROM python:3.8-slim

WORKDIR /cli

COPY ./requirements.txt /cli/requirements.txt

RUN pip install --no-cache-dir -r /cli/requirements.txt

COPY . /cli/.

#CMD ["python", "main.py", "--help"]