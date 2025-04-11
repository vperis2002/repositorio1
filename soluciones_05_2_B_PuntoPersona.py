


class Persona:
    """
    Añade a la clase Persona los siguientes métodos públicos:
    •	imprime()  // Imprime la información del objeto: “DNI:… Nombre:… etc.”
    •	es_mayor_edad() // Devuelve true si es mayor de edad (false si no).
    •	es_jubilado() // Devuelve true si tiene 65 años o más (false si no).
    •	diferencia_edad(Persona p) // Devuelve la diferencia de edad entre ‘this’ y p.
    Prueba a utilizar estos métodos desde el main para comprobar su funcionamiento.
    """

    def __init__(self, dni=None, nombre=None, apellidos=None, edad=None):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __del__(self):
        del self

    def imprime(self):
        return f"{self.nombre} {self.apellidos} con DNI {self.dni}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def es_mayor_jubilado(self):
        return self.edad >= 65

    def diferencia_edad(self, p):
        diferencia = 0
        if isinstance(p, Persona):
            diferencia = abs(p.edad - self.edad)
        return diferencia


class Rectangulo:
    """
    En nuestro software necesitamos asegurarnos de que la coordenada (x1,y1) represente la esquina inferior izquierda
    y la (x2,y2) la superior derecha del rectángulo, como en el dibujo.
    Incluye un if que compruebe los valores. Si son válidos guardará los parámetros en el objeto.
    Si no lo los inicializará a el valor de la cordenada inferior.
    Añade a la clase Rectángulo métodos públicos con las siguientes funcionalidades:
    •	Método para imprimir la información del rectángulo por pantalla.
    •	Métodos setters dobles y cuadruples: set_x1y1, set_x2y2 y set_all(…).
    •	Métodos get_perimetro y get_area que calculen y devuelvan el perímetro y área del objeto.
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 if x2 >= self.x1 else x1
        self.y2 = y2 if y2 >= self.y1 else y1

    @property
    def distancia_x(self):
        return abs(self.x2 - self.x1)

    @property
    def distancia_y(self):
        return abs(self.y2 - self.y1)

    def get_area(self):
        return self.distancia_x * self.distancia_y

    def get_perimetro(self):
        return 2 * self.distancia_x + 2 * self.distancia_y

    def imprimir(self):
        return f"({self.x1},{self.y1})-({self.x2},{self.y2})"

    def set_x1y1(self, x1=0, y1=0):
        self.x1 = x1
        self.y1 = y1

    def set_x2y2(self, x2=0, y2=0):
        self.x2 = x2
        self.y2 = y2

    def set_all(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 if x2 >= self.x1 else x1
        self.y2 = y2 if y2 >= self.y1 else y1


class Articulo:
    """
    Añade a la clase Artículo métodos públicos con las siguientes funcionalidades:
    •	Método para imprimir la información del artículo por pantalla.
    •	Método get_pvp que devuelva el precio de venta al público (PVP) con iva incluido.
    •	Método get_pvp_descuento que devuelva el PVP con un descuento pasado como argumento.
    •	Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ (si es  posible).
    Devolverá true si ha sido posible (false en caso contrario).
    •	Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad ‘x’.
    """
    IVA = 21

    def __init__(self, nombre="", precio=0, stock=0):
        self.nombre = nombre
        self.precio = precio if type(precio) is int and precio > 0 else 0
        self.stock = stock if type(stock) is int and stock > 0 else 0

    def get_pvp(self):
        return self.precio + (Articulo.IVA * self.precio / 100)

    def get_pvp_descuento(self, descuento=0):
        iva = Articulo.IVA * self.precio / 100
        descuento = abs(descuento) if -100 < descuento < 100 else abs(descuento / 100)
        return self.precio + iva - self.precio * descuento

    def vender(self, cantidad):
        vendido = False
        if self.stock >= abs(cantidad):
            self.stock -= cantidad
            vendido = True
        return vendido

    def almacenar(self, cantidad):
        self.stock += cantidad
        return True


class App:
    @staticmethod
    def main():
        pass


App().main()
