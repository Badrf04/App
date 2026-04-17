FROM python:3.10-slim

WORKDIR /app

# On copie d'abord les requirements pour optimiser le cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste (main.py, calcule.py, etc.)
COPY . .

# Port interne NiceGUI
EXPOSE 5000

CMD ["python", "main.py"]
