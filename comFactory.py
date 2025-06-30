from abc import ABC, abstractmethod

class Entrega(ABC):
    @abstractmethod
    def entregar(self):
        pass

class EntregaCorreios(Entrega):
    def entregar(self):
        print("Entrega pelos Correios")

class EntregaMotoboy(Entrega):
    def entregar(self):
        print("Entrega por Motoboy")

class Logistica(ABC):
    @abstractmethod
    def criar_entrega(self) -> Entrega:
        pass

    def processar_entrega(self):
        entrega = self.criar_entrega()
        entrega.entregar()

class LogisticaCorreios(Logistica):
    def criar_entrega(self):
        return EntregaCorreios()

class LogisticaMotoboy(Logistica):
    def criar_entrega(self):
        return EntregaMotoboy()

logistica1 = LogisticaCorreios()
logistica2 = LogisticaMotoboy()

logistica1.processar_entrega()
logistica2.processar_entrega()
