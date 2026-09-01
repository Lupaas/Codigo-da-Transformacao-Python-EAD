# Cria a class "Carro" que ira exibir a marca e modelo no terminal
class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


# Cria a class "CarroEletrico" que irá exibir a marca, modelo e a autonomia da bateria
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia da Bateria: {self.autonomia} km"


# Marca, modelo e autonomia da bateria que irão ser exibidas no terminal
meu_carro = CarroEletrico("BYD", "Dolphin", 600)
print(meu_carro.exibir_info())