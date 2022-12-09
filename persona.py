class Persona:
    nombre          = str
    edad            = int
    centroEstudios  = str
    
    def __init__(self, nombre, edad, centroEstudios):
        self.nombre         = nombre
        self.edad           = edad
        self.centroEstudios = centroEstudios
    
    def conversar (self, otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}, estudio en {self.centroEstudios}'

if __name__ == "__main__":
    Persona2 = Persona("Juan", 18, "Yavirac")
    Persona1 = Persona("Alisson", 21, "UCE")

    print(Persona1.conversar(Persona2))