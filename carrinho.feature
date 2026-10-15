# language: pt
# Thiago Alves Soares - 2502664

Funcionalidade: Carrinho de compras
  Como cliente do e-commerce
  Eu quero adicionar produtos ao carrinho e ver o valor total atualizado
  Para que eu não consiga comprar mais unidades do que existem no estoque

  Contexto:
    Dado que o carrinho está vazio

  Cenário: Adicionar um produto com sucesso
    Quando eu tento adicionar 2 unidades de um produto com estoque de 5 e preço de 10
    Então o total do carrinho deve ser 20
    E o carrinho deve ter 2 itens

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Quando eu tento adicionar 5 unidades de um produto com estoque de 3 e preço de 10
    Então o sistema deve exibir o erro "Estoque insuficiente"
    E o total do carrinho deve ser 0
    E o carrinho deve ter 0 itens
