class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
if __name__ == "__main__":
    alisson = Persona("Alisson", "Cumbajin", 21)
    lenin   = Persona("Lenin", "Montanlvo", 19)
    
    print(vars(alisson))
    print(lenin.apellido)

#La funcion __str__() : Definir el string que se imprime

class Persona2:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
    
    def __str__(self):
        return f'Hola me llamo {self.nombre} {self.apellido}. Soy estudiante de la carrera de {self.carrera}'

ejemplo1 = Persona2("Diego", "Yanez", 29, "Desarrollo de Software")
ejemplo2 = Persona2("Aexander", "Yanez", 29, "Marketing")
ejemplo3 = Persona2("Carlos", "Gonzales", 19, "Diseño")


print(ejemplo1)
print(ejemplo2)
print(ejemplo3)

#Creacion de metodos dentro de objetos

class Persona3:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    semestre = int
    
    def __init__(self, nombre, apellido, edad, carrera, semestre):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        self.semestre = semestre

    def bienvenida(self):
        print("Hola "+ self.nombre + " Bienvenido a la carrera de "+ self.carrera + "Tu " + self.semestre + " semestre va a ser muy interesante.")
        
ejemplo4 = Persona3("Diego", "Yanez", 29, "Desarrollo de Software", "3")
ejemplo5 = Persona3("David", "Yepez", 19, "Desarrollo Apps Moviles", "1")
ejemplo6 = Persona3("Dario", "Rodriguez", 9, "Diseño Web", "2")

ejemplo4.bienvenida()
ejemplo5.bienvenida()
ejemplo6.bienvenida()

class persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.edad     = edad
        self.apellido = apellido
    
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} {self.apellido}, tengo {self.edad} años y tu ? '

persona1 = persona("Jordan", "Gonzales", 22)
persona2 = persona("Enzo", "Perez", 21)

print(persona1.conversar(persona2))
print(persona1.conversar(alisson))

