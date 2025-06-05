import unittest
from funcoes import saudacao, maior_idade, criar_lista_com_referencia, buscar_elemento, verificar_membro, Produto, processar_dados

class TestFuncoes(unittest.TestCase):
    def test_saudacao(self):
        resultado = saudacao("João")
        self.assertEqual(resultado, "Olá, João!")
        
        resultado2 = saudacao("Maria")
        self.assertEqual(resultado2, "Olá, Maria!")

    def test_maior_idade_true(self):
        self.assertTrue(maior_idade(18))
        self.assertTrue(maior_idade(25))

    def test_maior_idade_false(self):
        self.assertFalse(maior_idade(17))
        self.assertFalse(maior_idade(10))

    def test_referencia_lista(self):
        lista_original = [1, 2, 3]
        lista_retornada = criar_lista_com_referencia(lista_original, 4)
        self.assertIs(lista_retornada, lista_original)

    def test_buscar_elemento_encontrado(self):
        lista = ["a", "b", "c"]
        resultado = buscar_elemento(lista, "b")
        self.assertEqual(resultado, 1)

    def test_buscar_elemento_nao_encontrado(self):
        lista = ["a", "b", "c"]
        resultado = buscar_elemento(lista, "x")
        self.assertIsNone(resultado)

    def test_membro_presente(self):
        lista = [1, 2, 3, 4, 5]
        self.assertTrue(verificar_membro(lista, 3))

    def test_membro_ausente(self):
        lista = [1, 2, 3, 4, 5]
        self.assertFalse(verificar_membro(lista, 6))

    def test_produtos_iguais(self):
        produto1 = Produto("Notebook", 2500.00)
        produto2 = Produto("Notebook", 2500.00)
        self.assertEqual(produto1, produto2)

    def test_produtos_diferentes(self):
        produto1 = Produto("Notebook", 2500.00)
        produto2 = Produto("Mouse", 50.00)
        self.assertNotEqual(produto1, produto2)

    def test_dados_vazios(self):
        resultado = processar_dados([])
        self.assertEqual(resultado, "vazio")

    def test_dados_grandes(self):
        dados_grandes = list(range(10))  # Lista com 10 elementos
        resultado = processar_dados(dados_grandes)
        self.assertEqual(resultado, "grande")

    def test_dados_normais(self):
        dados_normais = [1, 2, 3]
        resultado = processar_dados(dados_normais)
        self.assertEqual(resultado, "normal")

if __name__ == '__main__':
    unittest.main()
