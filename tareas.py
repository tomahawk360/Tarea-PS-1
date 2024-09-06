from datetime import datetime

class Tarea:
    def __init__(self, titulo, descripcion, etiqueta):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = self.ingresar_fecha_vencimiento()  # Llamada a la función durante la creación
        self.etiqueta = etiqueta

    def ingresar_fecha_vencimiento(self):
        while True:
            try:
                entrada = input("Ingrese la fecha y hora de vencimiento (YYYY-MM-DD HH:MM): ")
                fecha_vencimiento = datetime.strptime(entrada, '%Y-%m-%d %H:%M')
                return fecha_vencimiento
            except ValueError:
                print("Formato de fecha y hora incorrecto. Por favor, ingrese la fecha en el formato 'YYYY-MM-DD HH:MM'.")

    def mostrar_tarea(self):
        fecha_formateada = self.fecha_vencimiento.strftime('%Y-%m-%d %H:%M')
        return (f"Título: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha de Vencimiento: {fecha_formateada}\n"
                f"Etiqueta: {self.etiqueta}")

# Crear una instancia de Tarea
tarea1 = Tarea("Entregar informe", "Preparar el informe mensual para la reunión", "trabajo")

# Mostrar la información de la tarea
print(tarea1.mostrar_tarea())