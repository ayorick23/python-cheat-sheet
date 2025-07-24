class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # Atributo público
        self._saldo = saldo_inicial # Atributo protegido (convención)
        self.__numero_cuenta = "XYZ123ABC" # Atributo "privado" (name mangling)

    # Método público para depositar
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto:.2f} realizado. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("El monto del depósito debe ser positivo.")

    # Método público para retirar
    def retirar(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro de ${monto:.2f} realizado. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("Monto inválido o saldo insuficiente.")

    # Método público para obtener el saldo (controla el acceso al atributo protegido)
    def obtener_saldo(self):
        return self._saldo

    # Método "privado" (para demostración de name mangling)
    def __mostrar_numero_cuenta(self):
        print(f"Número de cuenta (interno): {self.__numero_cuenta}")

# Creando una cuenta
mi_cuenta = CuentaBancaria("Juan Pérez", 1000)

print(f"Titular de la cuenta: {mi_cuenta.titular}")
print(f"Saldo inicial: ${mi_cuenta.obtener_saldo():.2f}")

mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.retirar(1500) # Intento de retiro insuficiente

# Acceso directo al atributo público (generalmente está bien)
mi_cuenta.titular = "Juan P. González"
print(f"Nuevo titular: {mi_cuenta.titular}")

# Acceso directo al atributo protegido (¡posible, pero desaconsejado!)
# Puedes hacerlo, pero la convención dice que no deberías modificarlo directamente
mi_cuenta._saldo += 100 # Esto rompe el encapsulamiento
print(f"Saldo después de acceso directo: ${mi_cuenta.obtener_saldo():.2f}")

# Intento de acceso directo al atributo "privado" (fallará)
try:
    print(f"Intentando acceder a __numero_cuenta: {mi_cuenta.__numero_cuenta}")
except AttributeError as e:
    print(f"Error al intentar acceder directamente a __numero_cuenta: {e}")

# Accediendo al atributo "privado" mediante name mangling (no recomendado para uso normal)
print(f"Acceso con name mangling: {mi_cuenta._CuentaBancaria__numero_cuenta}")

# Intento de llamar al método "privado" (fallará)
try:
    mi_cuenta.__mostrar_numero_cuenta()
except AttributeError as e:
    print(f"Error al intentar llamar directamente a __mostrar_numero_cuenta: {e}")

# Llamando al método "privado" mediante name mangling
mi_cuenta._CuentaBancaria__mostrar_numero_cuenta()