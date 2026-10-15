# Carrinho de Compras com BDD

Thiago Alves Soares - 2502664

Exercício prático de BDD (Behavior Driven Development) com Python, pytest e pytest-bdd.

## O problema

O Product Owner pediu um carrinho de compras básico: o usuário adiciona um produto e vê o valor total atualizado. Se a quantidade desejada for maior que o estoque, o sistema deve dar o erro "Estoque insuficiente".

## Arquivos

| Arquivo | Função |
|---|---|
| `carrinho.feature` | Cenários em Gherkin (comportamento esperado) |
| `carrinho.py` | Regra de negócio: `criar_carrinho()` e `adicionar_produto()` |
| `test_carrinho.py` | Passos do pytest-bdd que ligam o Gherkin ao código |

## Como rodar

```bash
pip install pytest pytest-bdd
python -m pytest test_carrinho.py -v
```

Resultado esperado: 2 testes passando.

## Cenários

1. Adicionar um produto com sucesso, quando há estoque suficiente.
2. Tentar adicionar um produto sem estoque suficiente, que gera o erro "Estoque insuficiente" e mantém o carrinho vazio.