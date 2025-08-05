FROM python:3.9.23-alpine3.22
COPY . .
RUN pip install -r devops/requirements.txt
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]