class miClase:
    x = 5
    
p1= miClase()
print(p1.x)

class persona:
    nombre = str
    edad   = int
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad   = edad

    def __str__(self):
        return f"Su nombre es: {self.nombre}. Y su edad es: {self.edad}."
    
p2 = persona("Diego", 29)

print(p2)

class Persona2:
    nombre = str
    edad   = int
    cedula = str
    
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad   = edad
        self.cedula = cedula
    
    def miFuncion(self):
        print("Hola mi nombre es " + self.nombre + ". Con numero de cedula: "+ self.cedula)
        
p3 = Persona2("Alexander", 30, "171111111")
p3.miFuncion()


p3.nombre = "Carlos"
p3.cedula = "18181818181818"

p3.miFuncion()

class persona3:
    nombre = str
    edad   = int
    estatura = int
    
    def __init__(self,nombre,edad, estatura):
        self.nombre = nombre
        self.edad   = edad
        self.estatura = estatura

    def __str__(self):
        return f"Su nombre es: {self.nombre}. Y su edad es: {self.edad} y su estatura es: {self.estatura}cm"
    
p4 = persona3("Diego", 29, 171)

print(p4)

del p4.edad

print(p4)


