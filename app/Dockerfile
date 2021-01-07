# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster
EXPOSE 5000
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
#RUN apt-get update; apt-get install curl -y
# Install pip requirements
RUN python -m pip install -r requirements.txt
# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser ./
USER appuser
