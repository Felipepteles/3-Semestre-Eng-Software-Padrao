class Banco:
    def init(self):
        self.saldo = 1000

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo restante: R${self.saldo}")
        else:
            print("Saldo insuficiente.")

banco1 = Banco()
banco2 = Banco()

banco1.sacar(200)
banco2.sacar(300)

print(f"Saldo banco1: R${banco1.saldo}") 
print(f"Saldo banco2: R${banco2.saldo}") 