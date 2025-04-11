class CuentaBancaria:
    def __init__(self, dni, saldo_inicial=0):
        self._saldo = saldo_inicial  # Saldo es un atributo privado
        self.dni = dni
        self._comision = 5


        ###############

    @property
    def saldo(self): #GETTER
        #Propiedad de solo lectura para obtener el saldo.
        return self._saldo
    
    @saldo.setter
    def saldo(self, cantidad):
        self._saldo = cantidad

    @property
    def comision(self, cantidad):
        pass

    @comision.setter
    def comision(self, cantidad):
        if cantidad < 0:
            print("mal")
        else:
            self._comision = cantidad
    
   
    def depositar(self, cantidad):
        #Método para depositar dinero en la cuenta.
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self._saldo}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, cantidad):
        #Método para retirar dinero de la cuenta, asegurando que el saldo no sea negativo.
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retirada exitosa. Saldo restante: {self._saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

def main():
    # Uso de la clase
    cuenta = CuentaBancaria(100)
    print(cuenta.saldo)  # Acceso de solo lectura al saldo
    cuenta.depositar(50)
    cuenta.retirar(20)
    cuenta.saldo = 100
    cantidad = cuenta.saldo

    print(cuenta.saldo)  # Acceso de solo lectura al saldo


main()