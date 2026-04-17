# Utilisation d'une image Python légère
FROM python:3.10-slim

# Répertoire de travail
WORKDIR /app

# Installation des dépendances
# Assure-toi que 'nicegui' est dans ton requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source (dont ton main.py)
COPY . .

# NiceGUI écoute sur le port 5000 à l'intérieur du conteneur
EXPOSE 5000

# Lancement de l'application
CMD ["python", "main.py"]
