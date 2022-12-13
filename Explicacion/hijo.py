from padre import Persona
from padre import Persona2
from madre import Madre
from padre import Padre

class Hijo3(Persona):
    vivenda = str

    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivenda

hijo3 = Hijo3("Diego", "Yanez", 29, "Centro Historico")
padre3 = Persona("German", "Yanez", 55)

print(vars(hijo3))
print(vars(padre3))
print(hijo3.conversar(padre3))

class Hijo4(Persona2):
    edad     = int
    semestre = str

    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
    
    def felicitar(self, padre):
        return f'Felicidades {self.nombre}, acabas de terminar tu {self.semestre} semestre a tus {self.edad} años de edad. Att {padre.nombre} {padre.apellido}'
    
padre4 = Persona2("Carlos", "Borja")
hijo4  = Hijo4("Ivan", "Borja", 18, "Quinto")

print(vars(padre4))
print(vars(hijo4))
print(hijo4.felicitar(padre4))

class Hijofinal(Madre):
    nombre          = str
    apellidoPaterno = str
    apellidoMaterno = str
    edad            = int
    madre           = Madre("", "", "", "")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, madre):
        self.apellidoMaterno = apellidoMaterno
        self.apellidoPaterno = apellidoPaterno
        self.madre           = madre

#padrefinal = Padre("German", "Yanez", 55, "Quito")
#madrefinal = Madre("Veronica", "Flores", 55, "Quito")
hijofinal  = Hijofinal("Diego", "Yanez", "Flores", 29, Madre("Veronica", "Flores", 55, "Quito"))

#print(vars(padrefinal))
#print(vars(madrefinal))
print(vars(hijofinal))
print(vars(hijofinal.madre))
