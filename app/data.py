import httpx
from typing import List, Optional
from datetime import datetime

# URL oficial de la API de Indicadores del Banco Mundial
WB_API_URL = "https://api.worldbank.org/v2/country/PA/indicator/SH.IMM.MEAS"

def fetch_world_bank_data() -> List[dict]:
    try:
        response = httpx.get(f"{WB_API_URL}?format=json&per_page=100")
        response.raise_for_status() # Lanza error si la conexión falla
        
        data = response.json()
        
        # La API del BM devuelve una lista: [metadata, data_list]
        # Si no hay datos, la lista 'data_list' (índice 1) estará vacía o nula
        if len(data) < 2 or not data[1]:
            return []

        clean_data = []
        for item in data[1]:
            # Solo procesamos si hay un valor numérico válido
            if item.get("value") is not None:
                record = {
                    "year": int(item["date"]),
                    "country": item["country"]["value"],
                    "iso_code": item["countryiso3code"],
                    "value": float(item["value"])
                }
                clean_data.append(record)
        
        # Ordenamos por año descendente (del más reciente al más antiguo)
        return sorted(clean_data, key=lambda x: x["year"], reverse=True)

    except Exception as e:
        print(f"Error conectando con Banco Mundial: {e}")
        return []

# Variable global para simular caché y no llamar a la API en cada click
_cached_data = []

def get_all_vaccination_data() -> List[dict]:
    global _cached_data
    if not _cached_data:
        _cached_data = fetch_world_bank_data()
    return _cached_data

def get_data_by_year(year: int) -> Optional[dict]:
    data = get_all_vaccination_data()
    # Buscamos en la lista descargada
    return next((item for item in data if item["year"] == year), None)

def simulate_provincial_data(province_name: str) -> List[dict]:
    # Seguimos simulando las provincias porque el BM solo da datos nacionales
    import random
    national_data = get_all_vaccination_data()
    provincial_data = []
    
    for record in national_data:
        variance = random.uniform(-5.0, 5.0)
        simulated_value = max(0.0, min(100.0, record["value"] + variance))
        
        new_record = record.copy()
        new_record["province"] = province_name.title()
        new_record["value"] = round(simulated_value, 2)
        provincial_data.append(new_record)
    
    return provincial_data
