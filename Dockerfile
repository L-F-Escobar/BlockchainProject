FROM python:3.6
WORKDIR /app
ADD . /app
RUN cd /app \ pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["python", "blockchain.py", "--port", "5000"]