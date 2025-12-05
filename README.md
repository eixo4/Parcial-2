# 🇵🇦 API de Vacunación Sarampión - Panamá

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=flat&logo=fastapi)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Descripción

Esta es una **API RESTful de solo lectura (GET-only)** diseñada para consultar datos históricos sobre la cobertura de vacunación contra el sarampión en niños de 12 a 23 meses en Panamá.

El proyecto utiliza datos basados en el indicador **SH.IMM.MEAS** del Banco Mundial. La API permite consultar registros históricos nacionales y simula una distribución regional para fines demostrativos.

## 🚀 Tecnologías

* **Lenguaje:** Python 3.10+
* **Framework Web:** FastAPI
* **Servidor:** Uvicorn
* **Validación de Datos:** Pydantic
* **Testing:** Pytest

## 📂 Estructura del Proyecto

```text
panama_vacunas_api/
├── app/
│   ├── __init__.py
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── models.py        # Esquemas de datos Pydantic
│   ├── routes.py        # Definición de endpoints
│   └── data.py          # Capa de datos (Mock Data / Lógica)
├── tests/
│   ├── __init__.py
│   └── test_main.py     # Pruebas unitarias e integración
├── requirements.txt     # Dependencias del proyecto
└── pytest.ini           # Configuración de pruebas
````

## 🛠️ Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1\. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPO>
cd panama_vacunas_api
```

### 2\. Crear entorno virtual

```bash
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3\. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4\. Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor iniciará en `http://127.0.0.1:8000`.

## 📖 Documentación de la API

FastAPI genera documentación interactiva automáticamente. Una vez corras el servidor, visita:

  * **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
  * **ReDoc:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

### Endpoints Principales

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/vacunas` | Obtiene todos los registros históricos disponibles. |
| `GET` | `/vacunas/{anio}` | Obtiene el registro de un año específico (ej. 2021). Retorna 404 si no existe. |
| `GET` | `/vacunas/provincia/{nombre}` | Genera datos simulados para una provincia específica basados en la media nacional. |

## ✅ Pruebas (Testing)

El proyecto incluye pruebas unitarias para garantizar la estabilidad de los endpoints. Para ejecutarlas:

```bash
pytest
```

## 📝 Licencia

Este proyecto es de uso educativo y libre. Los datos base pertenecen a los indicadores públicos del Banco Mundial.
