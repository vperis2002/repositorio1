class SistemaIluminacion:
    def __init__(self):
        self.__nivel_brillo = 0  # Nivel de brillo privado

    @property
    def nivel_brillo(self):
        #Propiedad para obtener el nivel de brillo actual.
        return self.__nivel_brillo

    @nivel_brillo.setter
    def nivel_brillo(self, valor):
        #Establece el nivel de brillo asegurando que esté en el rango 0-100.
        if 0 <= valor <= 100:
            self.__nivel_brillo = valor
            print(f"Nivel de brillo ajustado a {valor}.")
        else:
            print("El nivel de brillo debe estar entre 0 y 100.")

# Uso de la clase
sistema = SistemaIluminacion()
sistema.nivel_brillo = 70  # Ajuste válido
print(sistema.nivel_brillo)
sistema.nivel_brillo = 150  # Ajuste inválido
