# colabsakila
Caso practico #2 colaborativo Ciencias de Datos I


### Paso 1 - Configurar Credenciales a Utilizar

- Debe realizar una copia del .env.example para colocar tus credenciales de BD:
```env
DB_HOST=localhost
DB_USER=your_username
DB_PORT=3306
DB_PASSWORD=your_password
DB_DATABASE=sakila
```

### Paso 2 - Para usar el proyecto, ejecuta estos comandos:

- Activar el entorno virtual (macOS/Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

- Instalar dependencias
```bash
pip install -r requirements.txt
```

- Ejecutar el programa
```bash
python main.py
```

### Paso 3 - Subir nuestra bases de datos Sakila

```bash
% docker-compose up -d
```


### Paso 4 - Utilizar el sistema

```bash
% python main.py
```