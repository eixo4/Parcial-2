import random
from typing import List, Optional

# Datos estáticos basados en el histórico real aproximado de Panamá (SH.IMM.MEAS)
# Se hardcodean para garantizar disponibilidad sin depender de conexión externa inmediata.
mock_db = [
    {"year": 2022, "country": "Panama", "iso_code": "PAN", "value": 85.0},
    {"year": 2021, "country": "Panama", "iso_code": "PAN", "value": 81.0},
    {"year": 2020, "country": "Panama", "iso_code": "PAN", "value": 79.0},
    {"year": 2019, "country": "Panama", "iso_code": "PAN", "value": 88.0},
    {"year": 2018, "country": "Panama", "iso_code": "PAN", "value": 90.0},
    {"year": 2010, "country": "Panama", "iso_code": "PAN", "value": 95.0},
    {"year": 2000, "country": "Panama", "iso_code": "PAN", "value": 97.0},
]


def get_all_vaccination_data() -> List[dict]:
    return mock_db


def get_data_by_year(year: int) -> Optional[dict]:
    # Retorna None si no encuentra el año para facilitar el manejo de errores 404 luego
    return next((item for item in mock_db if item["year"] == year), None)


def simulate_provincial_data(province_name: str) -> List[dict]:
    # Generamos datos ficticios aplicando una varianza aleatoria al promedio nacional
    # para cumplir con el requisito opcional de datos regionales.
    provincial_data = []
    for record in mock_db:
        # Variación entre -5% y +5% respecto a la media nacional
        variance = random.uniform(-5.0, 5.0)
        simulated_value = max(0.0, min(100.0, record["value"] + variance))

        new_record = record.copy()
        new_record["province"] = province_name.title()
        new_record["value"] = round(simulated_value, 2)
        provincial_data.append(new_record)

    return provincial_data