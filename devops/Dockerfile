FROM python:3.9
RUN pip install -r devops/requirements.txt
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]