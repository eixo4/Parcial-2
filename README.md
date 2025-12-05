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
