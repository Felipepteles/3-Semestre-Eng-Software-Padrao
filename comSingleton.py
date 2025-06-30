class BancoSingleton:
    _instancia = None

    def __init__(cls):
        if cls._instancia is None:
            cls._instancia = super().__init__(cls)
            cls._instancia.saldo = 1000
        return cls._instancia

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

banco1 = BancoSingleton()
banco2 = BancoSingleton()

banco1.sacar(200)
banco2.sacar(300)

print(f"Saldo banco1: R${banco1.saldo}")
print(f"Saldo banco2: R${banco2.saldo}")
