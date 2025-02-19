# 📝 Sistema de Gestión de Tareas con Django

Un sistema web robusto y elegante para la gestión de tareas personales, construido con Django y Bootstrap. Este proyecto permite a los usuarios gestionar sus tareas diarias de manera eficiente y segura.

## ✨ Características

- 🔐 Sistema de autenticación completo (registro, inicio de sesión, cierre de sesión)
- ✅ Gestión completa de tareas (CRUD)
  - Crear nuevas tareas
  - Ver lista de tareas pendientes y completadas
  - Editar tareas existentes
  - Eliminar tareas
  - Marcar tareas como completadas
- ⭐ Marcado de tareas importantes
- 📱 Diseño responsivo (adaptable a móviles)
- 🎨 Interfaz de usuario intuitiva y moderna

## 🛠️ Tecnologías Utilizadas

- Django 4.2.6
- Bootstrap (para el diseño responsivo)
- SQLite (base de datos)
- HTML/CSS
- Python 3

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone [URL del repositorio]
```

2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Realiza las migraciones de la base de datos:
```bash
python manage.py migrate
```

4. Inicia el servidor:
```bash
python manage.py runserver
```

5. Visita `http://localhost:8000` en tu navegador

## 💡 Uso

1. Regístrate en la plataforma
2. Inicia sesión con tus credenciales
3. Comienza a crear y gestionar tus tareas
4. Marca las tareas como importantes según sea necesario
5. Completa las tareas cuando las hayas terminado

## 🔒 Características de Seguridad

- Autenticación de usuarios
- Protección contra CSRF
- Cada usuario solo puede ver y gestionar sus propias tareas
- Sesiones seguras

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

---
⌨️ con ❤️ por DAVID A. CHENTES