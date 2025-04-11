

class Articulo:
    """
    Ejercicio 4 – Artículo
    Crea un programa con una clase llamada Articulo con los siguientes atributos: nombre, precio (sin __IVA),
    iva (siempre será 21) y cuantosQuedan (representa cuantos quedan en el almacén).
    En el main de la clase principal instancia un objeto de la clase artículo. Asígnale valores a todos sus atributos
    (los que quieras) y muestra por pantalla un mensaje del estilo “Pijama - Precio:10€ - __IVA:21% - PVP:12,1€”
    (el PVP es el precio de venta al público, es decir, el precio con __IVA). Luego, cambia el precio
    y vuelve a imprimir el mensaje.
    """
    IVA = 21

    def __init__(self, nombre="", precio=0, stock = 0):
        self.nombre = nombre
        self.precio = precio 
        self.stock = stock
    
    def incrementar_stock(self, cantidad):
        self.stock += cantidad
    
    def vender_unidades(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad

            return cantidad * self.calcular_precio_iva()
        else:
            print("No hay stock suficiente.")
    
    def calcular_precio_iva(self):
        return self.precio * self.IVA /100


def main():

    lista_de_articulos = []

    while True:

        nombre_articulo = input("Dime en nombre del articulo: ")
        stock_inicial_articulo = int(input("Dime cuanto stock inicial tenemos: "))
        articulo_temporal = Articulo(nombre_articulo, stock_inicial_articulo)

        articulo_temporal.incrementar_stock(100)

        cantidad_a_vender = int(input("Dime cuantas unidades quieres vender:"))
        articulo_temporal.vender_unidades(cantidad_a_vender)

        lista_de_articulos.append(articulo_temporal)
        
        continuar = input("¿Quieres seguir dándome artículos?")
main()
