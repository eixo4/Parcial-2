from fastapi import APIRouter, HTTPException, Path
from typing import List
from . import data, models

router = APIRouter()


@router.get("/vacunas", response_model=List[models.VaccinationRecord])
def get_vacunas():
    """Devuelve todos los registros históricos disponibles."""
    return data.get_all_vaccination_data()


@router.get("/vacunas/{anio}", response_model=models.VaccinationRecord)
def get_vacuna_por_anio(
        anio: int = Path(..., title="Año", description="Año del registro a consultar (ej. 2021)")
):
    """Devuelve el registro de un año específico."""
    record = data.get_data_by_year(anio)

    # Es crucial informar al cliente si el recurso no existe según estándares REST
    if not record:
        raise HTTPException(status_code=404, detail="Registro no encontrado para el año especificado")

    return record


@router.get("/vacunas/provincia/{nombre}", response_model=List[models.ProvincialRecord])
def get_vacunas_por_provincia(nombre: str):
    """
    Simula datos para una provincia específica.
    """
    return data.simulate_provincial_data(nombre)