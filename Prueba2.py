class Caballero():
    def __init__(self, nombre, color_armadura, nombre_espada, yelmo ):
        self.nombre = nombre
        self.color_armadura = color_armadura 
        self.nombre_espada = nombre_espada
        self.yelmo = yelmo

    def llamar_caballero(self):
        print("Hola, soy ser ", self.nombre, "mi armadura es de color", self.color_armadura, "mi espada se llama", self.nombre_espada, "y uso un ", self.yelmo) 

mi_caballero = Caballero("Duncan", "dorada", "excalibur", "yelmo de dragon") 

mi_caballero2 = Caballero("Rhaegar", "plateada", "Fuego oscuro", "yelmo de dragon") 

class Dragon():
    def __init__(self) -> None:
        pass




mi_caballero.llamar_caballero()

mi_caballero2.llamar_caballero()






        