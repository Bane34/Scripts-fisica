from typing import Tuple

class Espejo:
    def __init__(self, centro):
        self.centro = centro
        self.foco = centro / 2

    def imagen(self, y, s):
        s_prima = (s * self.foco) / (s - self.foco)
        y_prima = -(s_prima * y) / s

        return (s_prima, y_prima)

class Lente:
    def __init__(self, foco):
        self.foco_imagen = foco 
        self.foco_objeto = -foco
        self.dos_foco = 2 * foco 

        self.potencia = 1 / foco

    def imagen(self, y, s):
        s_prima = (s * self.foco_imagen) / (s + self.foco_imagen)
        y_prima = (s_prima * y) / s
