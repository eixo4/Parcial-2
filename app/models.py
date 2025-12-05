from pydantic import BaseModel

class VaccinationRecord(BaseModel):
    year: int
    country: str
    iso_code: str
    value: float  # Porcentaje de cobertura

    # Configuración para facilitar la conversión desde diccionarios
    class Config:
        from_attributes = True

class ProvincialRecord(VaccinationRecord):
    province: str