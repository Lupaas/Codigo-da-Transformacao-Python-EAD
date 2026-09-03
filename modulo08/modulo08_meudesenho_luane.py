'''
Desenhos:

A lenda de anng - Katara
Kung Fu Panda - Tigreza ou Víbora
Team Umizoomi - Milli
Ni Hao, Kai-Lan - Hoho

'''

class BonecoToyStory:
    def __init__(self, nome, dono, frase_de_efeito):
        self.nome = nome
        self.dono = dono
        self.frase_de_efeito = frase_de_efeito
        
        
woody = BonecoToyStory(
    nome = "Woody",
    dono = "Andy",
    frase_de_efeito = "Há uma cobra na minnha bota!"
)

slinky = BonecoToyStory(
    nome = "Slinky",
    dono = "Andy",
    frase_de_efeito = "O Woody nunca nos guiou errado antes."
)

lotso = BonecoToyStory(
    nome = "Lotso",
    dono = "Daisy",
    frase_de_efeito = "Não ter dono significa não sofrer mais"
)

print(f'Nome: {slinky.nome} | Dono: {slinky.dono} | Frase: {slinky.frase_de_efeito}')