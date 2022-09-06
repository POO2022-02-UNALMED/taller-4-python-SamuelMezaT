from classroom.asignatura import Asignatura
class Grupo:
    grado = "Grado 12"
    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    def listadoAsignaturas(self, **kwargs):
        a=[]
        for x in kwargs.values():
            a.append(Asignatura(x))
        self._asignaturas=a
    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos =  lista + [alumno]
    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo