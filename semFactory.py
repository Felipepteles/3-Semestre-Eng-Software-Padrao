class EntregaCorreios:
    def entregar(self):
        print("Entrega pelos Correios")

class EntregaMotoboy:
    def entregar(self):
        print("Entrega por Motoboy")

class Cliente:
    def solicitar_entrega(self, tipo):
        if tipo == "correios":
            entrega = EntregaCorreios()
        elif tipo == "motoboy":
            entrega = EntregaMotoboy()
        else:
            raise ValueError("Tipo de entrega inválido")
        
        entrega.entregar()

cliente = Cliente()
cliente.solicitar_entrega("correios")
cliente.solicitar_entrega("motoboy")
