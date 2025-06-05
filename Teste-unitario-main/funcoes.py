def saudacao(nome):
    """Função que retorna 'Olá, {nome}!'"""
    return f"Olá, {nome}!"

def maior_idade(idade):
    """Função que retorna True se idade >= 18"""
    return idade >= 18

def criar_lista_com_referencia(lista, item):
    """Cria lista referenciando outra e adiciona item"""
    nova_lista = lista
    nova_lista.append(item)
    return nova_lista

def buscar_elemento(lista, elemento):
    """Busca elemento em lista, retorna None se não encontrado"""
    if elemento in lista:
        return lista.index(elemento)
    return None

def verificar_membro(lista, elemento):
    """Verifica se elemento está na lista"""
    return elemento in lista

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.nome == other.nome and self.preco == other.preco
        return False

def processar_dados(dados):
    """Função que processa dados e pode retornar diferentes status"""
    if not dados:
        return "vazio"
    if len(dados) > 5:
        return "grande"
    return "normal"
