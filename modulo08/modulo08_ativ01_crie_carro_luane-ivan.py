# Cria a class "Carro" que ira exibir a marca e modelo no terminal
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
# Marca e modelo que irá ser exibidas    
meu_carro = Carro("Ford", "Mustang")
print(meu_carro.exibir_info())

