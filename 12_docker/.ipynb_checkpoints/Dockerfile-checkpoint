# a docker file for fast api
# base image
FROM python:3.12-slim

# setting a working directory
WORKDIR /app

#copying requirements and installing dependeces
COPY requirements.txt .
RUN pip install -r requirements.txt

#copying rest of the code
COPY . .

#exposing port
EXPOSE 8000

#command to start fast api application
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

