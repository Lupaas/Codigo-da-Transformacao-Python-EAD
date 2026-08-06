leitura_arquivo = open('leitura_arquivo_luane.txt', 'r', encoding='utf-8')

conteudo_arquivo = leitura_arquivo.readlines()

print(conteudo_arquivo[1].strip())
print(conteudo_arquivo[44].strip())

leitura_arquivo.close()