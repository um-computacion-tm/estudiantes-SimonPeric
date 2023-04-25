class Persona: # La herencia son cosas que comparten clases, por ejemplo los alumnos y profesores comparten que son personas
    
class Profesor(Persona):
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

profesor_pepe:Profesor = Profesor("Pepe", "jose@um.edu.ar")

print(id(profesor_pepe))
print("el nombre es: ")
print(profesor_pepe.nombre)

print("el email es: ")
print(profesor_pepe.email)

print("su asistencia es: ")
print(profesor_pepe.asistencia)

class Alumno(Persona):
    def __init__(self, param_nombre, param_apellido, param_edad, param_dni, param_curso, param_email): #init: Sirve como una constructora de objetos
        
        self.nombre = param_nombre
        self.apellido = param_apellido
        self.edad = param_edad
        self.dni = param_dni
        self.curso = param_curso
        self.email = param_email
    
alumno_simon = Alumno("Simon","Peric","21","43.748.217","2do de Ing en computación")

print("El nombre del alumno es:")
print(alumno_simon.nombre)

print("El apellido del alumno es:")
print(alumno_simon.apellido)

print("La edad de el alumno es:")
print(alumno_simon.edad)

print("El DNI es:")
print(alumno_simon.dni)

print("Esta cursando en:")
print(alumno_simon.curso)

print("El email del alumno es:")
print(alumno_simon.email)