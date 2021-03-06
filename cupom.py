nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():
	dados = nome_loja + "\n"
	dados += ("%s, %d %s" % (logradouro, numero, complemento))+ "\n"
	dados += ("%s - %s - %s" % (bairro, municipio, estado))+ "\n"	
	dados += ("CEP:%s Tel %s" % (cep, telefone))+ "\n"
	dados += (observacao)+ "\n"
	dados += ("CNPJ: %s" % cnpj)+ "\n"
	dados += ("IE: %s" % inscricao_estadual)+ "\n"
	return dados
