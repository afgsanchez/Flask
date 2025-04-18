class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self): # el metodo __str__ sirve para imprimir en cualquier momento el estado del objeto.
        return (f"Id: {self.id}, Nombre: {self.nombre},"
                f" Apellido: {self.apellido}, Membresia: {self.membresia}")