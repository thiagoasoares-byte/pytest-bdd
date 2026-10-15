# Thiago Alves Soares - 2502664

from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto

scenarios("carrinho.feature")


@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@when(
    parsers.parse(
        "eu tento adicionar {quantidade:d} unidades de um produto "
        "com estoque de {estoque:d} e preço de {preco:d}"
    )
)
def tentar_adicionar(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as e:
        carrinho["erro"] = str(e)


@then(parsers.parse("o total do carrinho deve ser {total:d}"))
def validar_total(carrinho, total):
    assert carrinho["total"] == total


@then(parsers.parse("o carrinho deve ter {itens:d} itens"))
def validar_itens(carrinho, itens):
    assert carrinho["itens"] == itens


@then(parsers.parse('o sistema deve exibir o erro "{mensagem}"'))
def validar_erro(carrinho, mensagem):
    assert carrinho.get("erro") == mensagem
