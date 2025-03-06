class ImagenMedicaDTO:
    def __init__(self, id=None, url=None, modalidad=None, region_anatomica=None, patologia=None, estado_procesamiento="pendiente"):
        self.id = id
        self.url = url
        self.modalidad = modalidad
        self.region_anatomica = region_anatomica
        self.patologia = patologia
        self.estado_procesamiento = estado_procesamiento
