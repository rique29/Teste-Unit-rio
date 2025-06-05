# Guia de Testes Unitários em Python

Este projeto demonstra a implementação de testes unitários em Python usando o módulo `unittest`. São apresentados diversos exemplos de funções e seus respectivos testes, cobrindo diferentes cenários de teste.

## Estrutura do Projeto

```
├── funcoes.py         # Arquivo com as funções a serem testadas
├── test_funcoes.py    # Arquivo contendo os testes unitários
└── README.md         # Este arquivo
```

## Funções Implementadas

1. `saudacao(nome)`: Retorna uma mensagem de saudação
2. `maior_idade(idade)`: Verifica se uma pessoa é maior de idade
3. `criar_lista_com_referencia(lista, item)`: Demonstra referência de objetos em Python
4. `buscar_elemento(lista, elemento)`: Busca um elemento em uma lista
5. `verificar_membro(lista, elemento)`: Verifica se um elemento está em uma lista
6. `class Produto`: Demonstra comparação de objetos
7. `processar_dados(dados)`: Processa dados com diferentes condições

## Como Executar os Testes

Você pode executar os testes de várias maneiras:

1. **Executar todos os testes com detalhes:**
   ```bash
   python -m unittest -v test_funcoes.py
   ```

2. **Executar um teste específico:**
   ```bash
   python -m unittest test_funcoes.TestFuncoes.test_saudacao
   ```

3. **Descobrir e executar todos os testes no diretório:**
   ```bash
   python -m unittest discover -s . -p "test_*.py"
   ```

## Tipos de Testes Implementados

1. **Testes de Igualdade** (`assertEqual`)
   - Exemplo: `test_saudacao`
   ```python
   self.assertEqual(saudacao("João"), "Olá, João!")
   ```

2. **Testes Booleanos** (`assertTrue`/`assertFalse`)
   - Exemplo: `test_maior_idade_true`
   ```python
   self.assertTrue(maior_idade(18))
   ```

3. **Testes de Referência** (`assertIs`)
   - Exemplo: `test_referencia_lista`
   ```python
   self.assertIs(lista_retornada, lista_original)
   ```

4. **Testes de Valor Nulo** (`assertIsNone`)
   - Exemplo: `test_buscar_elemento_nao_encontrado`
   ```python
   self.assertIsNone(buscar_elemento(lista, "x"))
   ```

5. **Testes de Objetos** (`assertEqual` com `__eq__`)
   - Exemplo: `test_produtos_iguais`
   ```python
   self.assertEqual(produto1, produto2)
   ```

## Como Adicionar Novos Testes

1. Adicione sua função em `funcoes.py`
2. Crie um método de teste correspondente em `test_funcoes.py`
3. O nome do método de teste deve começar com `test_`
4. Use os assertions apropriados para verificar o comportamento esperado

Exemplo:
```python
def test_minha_nova_funcao(self):
    resultado = minha_funcao(entrada)
    self.assertEqual(resultado, valor_esperado)
```

## Boas Práticas

1. **Nomeação de Testes:**
   - Use nomes descritivos
   - Comece com `test_`
   - Indique o que está sendo testado

2. **Organização:**
   - Um teste por comportamento
   - Testes independentes
   - Setup e teardown quando necessário

3. **Cobertura:**
   - Teste casos normais
   - Teste casos de borda
   - Teste casos de erro

4. **Documentação:**
   - Docstrings nas funções
   - Comentários em testes complexos
   - README atualizado

## Interpretação dos Resultados

- `.` (ponto): Teste passou
- `F`: Teste falhou
- `E`: Erro durante execução
- `s`: Teste pulado

## Requisitos

- Python 3.6 ou superior
- Módulo `unittest` (incluído na biblioteca padrão Python)