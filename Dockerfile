FROM python:3.12-slim

WORKDIR /app

COPY modular_auditor.py .

CMD ["python", "modular_auditor.py"]