class animal:
    def __init__(self, patas, especie, accion):
        self.especie = especie
        self.patas = patas
        self.accion = accion

    def hacer_accion(self):
        print(f"{self.nombre} esta {self.accion}")
        

class perro(animal):
    def __init__(self, patas, especie, accion, color, nombre):
        super().__init__(patas, especie, accion)
        self.color = color
        self.nombre = nombre
    
    def introduccion(self):
        print(f"{self.nombre} es un {self.especie} {self.color} de {self.patas} patas.")


pedro = perro(patas= 4, especie= "perro", color = "blanco", nombre = "pedro", accion = "ladrando")
chiqui = perro(patas= 4, especie = "gato", color = "multicolor", nombre = "chiqui", accion = "maullando")
