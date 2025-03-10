# Booking Platform

Este proyecto es una plataforma de gestión de reservas. Actualmente está centrado en el sector de restaurantes, pero está diseñado para ser escalable a otros sectores como peluquerías, consultorios médicos y salones de belleza.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Inicializar el Proyecto

Sigue estos pasos para poner en marcha el proyecto:

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/mauri92x/booking-platform-backend.git
cd booking-platform-backend
```

### 2. Crear y Configurar el Entorno Virtual

Ejecuta los siguientes comandos para configurar el entorno virtual usando Poetry:

poetry install

Esto instalará todas las dependencias necesarias del proyecto.

### 3. Configurar Variables de Entorno

Crea un archivo .env en la raíz del proyecto y agrega la configuración correspondiente:

DEBUG=True
SECRET_KEY=super-secret-key
DATABASE_URL=postgresql://usuario:password@localhost:5432/booking_db
ALLOWED_HOSTS=\*

Asegúrate de reemplazar usuario, password y booking_db con tus credenciales reales de PostgreSQL.

### 4. Aplicar Migraciones

Ejecuta las migraciones de la base de datos:

poetry run python manage.py migrate

### 5. Crear un Superusuario (Opcional)

Si deseas acceder al panel de administración, crea un superusuario con:

poetry run python manage.py createsuperuser

### 6. Ejecutar el Servidor

Finalmente, levanta el servidor de desarrollo con:

poetry run python manage.py runserver

El backend estará disponible en http://127.0.0.1:8000/.
