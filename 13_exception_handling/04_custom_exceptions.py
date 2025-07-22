# Definición de la excepción personalizada
class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando el saldo de una cuenta es insuficiente."""
    def __init__(self, mensaje="Saldo insuficiente para la operación.", saldo_actual=0, monto_requerido=0):
        self.mensaje = mensaje
        self.saldo_actual = saldo_actual
        self.monto_requerido = monto_requerido
        super().__init__(self.mensaje) # Llama al constructor de la clase base Exception

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError(
                f"No hay fondos suficientes para retirar {monto}. Saldo actual: {self.saldo}",
                saldo_actual=self.saldo,
                monto_requerido=monto
            )
        self.saldo -= monto
        print(f"Retiro de {monto} exitoso. Nuevo saldo: {self.saldo}")

print("--- Uso de excepción personalizada ---")
mi_cuenta = CuentaBancaria(saldo_inicial=500)

try:
    mi_cuenta.retirar(200)
    mi_cuenta.retirar(400) # Esto debería lanzar la excepción
except SaldoInsuficienteError as e:
    print(f"\n¡ERROR PERSONALIZADO! {e.mensaje}")
    print(f"Detalles del error: Saldo actual: {e.saldo_actual}, Monto requerido: {e.monto_requerido}")
except Exception as e:
    print(f"Ocurrió otro tipo de error: {e}")