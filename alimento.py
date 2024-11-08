class Alimento:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
        
    def usar(self, cantidad_u):
        if self.cantidad >= cantidad_u:
            self.cantidad -= cantidad_u
        else:
            print(f"No hay suficiente {self.tipo} disponible.")
    
    
 