import datetime as dt
from random import randint


class SistemaDeCompra:
    def __init__(self, nome, telefone, cpf_cnpj, cpf_Ou_cnpj):
        self.nome = nome
        self.telefone = telefone
        

        if cpf_Ou_cnpj == 1:
            self.cpf = cpf_cnpj
        else:
            self.cnpj = cpf_cnpj

    def onlyInt(texto):
        valor = ""
        while type(valor) != int:
            try:
                valor = int (input(texto))
            except ValueError:
                print("digite algo valido")

        return valor

    def criaCliente():
        cpf_Ou_cnpj = 0
        while cpf_Ou_cnpj <1 or cpf_Ou_cnpj >2:
            cpf_Ou_cnpj = SistemaDeCompra.onlyInt('Voce é pessoa fisica ou jurídica?:\nfisica(1)\njurídica(2)\n==>')
        
        nome = input('Digite o seu nome:')
        nome = nome.capitalize()
        telefone = SistemaDeCompra.onlyInt('Digite o seu telefone:')
        cpf_cnpj = SistemaDeCompra.onlyInt('Digite o seu cpf/cnpj:')
        
        return SistemaDeCompra(nome,telefone, cpf_cnpj,cpf_Ou_cnpj)
    
    def livros():
        livros = [[{}]]
        livros =[{
            
            'nome':'A Arte da Guerra',
            'autor':'Sun Tzu',
            'assunto':' Estratégia Militar',
            'Editora':'Estratégia Publicações',
            'Preço': 'R$ 25,00',
            'estoque':20 
            },{
            'nome':'Cem Anos de Solidão',
            'autor':'Gabriel García Márquez',
            'assunto':' Ficção Latino-Americana',
            'Editora':'Realismo Mágico Edições',
            'Preço': 'R$ 30,00',
            'estoque':20
                
            },{
            'nome':'O Senhor dos Anéis',
            'autor':'J.R.R. Tolkien',
            'assunto':' Fantasia Épica',
            'Editora':'Terra Média Books',
            'Preço': 'R$ 40,00',
            'estoque':20
                    
            },{
            'nome':'Ponto de Inflexão',
            'autor':'Malcolm Gladwell',
            'assunto':'Psicologia Social',
            'Editora':'Conexões Editoriais',
            'Preço': 'R$ 28,00',
            'estoque':20   
                        
            },{
            'nome':'A Revolução dos Bichos',
            'autor':'George Orwell',
            'assunto':'  Sátira Política',
            'Editora':'Livros Rebeldes',
            'Preço': 'R$ 22,00',
            'estoque':20      
                            
            }
            ]
        comprando = 1
        while comprando == 1:
            sistema = 0
            contador = 1
            compra = 0
            livrosComprados = []
            dataComprada = []
            ISBN = []
            print('os livros no estoque são:')
            for livro in livros:
                
                print (livro['nome'])
                
            while sistema <1 or sistema >3:
                sistema = SistemaDeCompra.onlyInt('\nOque voce deseja fazer?\n1)comprar\n2)ver informações sobre o livro\n3)sair \n==>')
            
            
            if sistema == 1:
                
                for livro in livros:
                
                    print (f'{contador}){livro['nome']}')
                    contador += 1
                while compra <1 or compra >5:

                    compra = SistemaDeCompra.onlyInt('Qual livro?:\n==>')
                compra -= 1 
                livrosComprados.append([livros[compra]['nome']])
                dataComprada.append(str(dt.date.today()))
                ISBN.append(randint(0,50000))
                input(f'A loja agradece pela compra de "{livros[compra]['nome']}"(precione enter para continuar)')
                
            elif sistema == 2:
                contador = 1
                book = 0
                for livro in livros:
                
                    print (f'{contador}){livro['nome']}')
                    contador += 1
                while book <1 or book >5:

                    book = SistemaDeCompra.onlyInt('Qual livro?:\n==>')
                book -= 1
                print('======================================')
                for informaçao in livros[book]:
                    print(informaçao,':',livros[book][informaçao])
                print('======================================')                
                input('(enter para voltar as compras)')
            
            else:
                pass
    
    def salva_cliente(cliente):
        
        pass