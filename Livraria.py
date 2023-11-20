from SistemaDeCompra import SistemaDeCompra as sdc
import datetime as dt
import time


def main():
    todosClientes = []
    livros = sdc.livros
    while True:
        usuario_selecionado = sdc.mostraClientes(todosClientes)

        if usuario_selecionado == (len(todosClientes) + 1):
            break

        elif usuario_selecionado != None:
            escolha = sdc.oqueFara(usuario_selecionado)

            if escolha == 1:
                sdc.ver_informaçoes_livros(usuario_selecionado, todosClientes)
            elif escolha == 2:
                sdc.ver_informaçoes(usuario_selecionado, todosClientes)

            elif escolha == 3:
                compras, livros = sdc.compras(livros)
                try:
                    book, isbn, data = sdc.pega_livros(
                        usuario_selecionado, todosClientes
                    )
                    compras = sdc.funde_livros(compras, book, isbn, data)
                except TypeError:
                    todosClientes[usuario_selecionado].update({"compras": compras})

            elif escolha == 4:
                pass

        elif usuario_selecionado == None:
            cliente = sdc.criaCliente()
            compras, livros = sdc.compras(livros)
            clientePronto = sdc.salva_cliente(cliente, compras)
            todosClientes.append(clientePronto)

    sdc.sair()


if __name__ == "__main__":
    main()
