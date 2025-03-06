from dataclasses import dataclass

@dataclass(frozen=True)
class MetadatosClinicos:
    modalidad: str
    region_anatomica: str
    patologia: str