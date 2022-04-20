FROM python:3.8.10

WORKDIR ~/messenger-auth-server

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "./run.py" ]
