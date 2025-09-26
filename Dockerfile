# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala FastAPI y Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Expone el puerto en el que se ejecutará la app
EXPOSE 8050

# Comando para iniciar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8050"]
