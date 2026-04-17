FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code
COPY . .

# LIAISON : On informe que l'app utilise le port 5000
EXPOSE 5000

CMD ["python", "main.py"]
