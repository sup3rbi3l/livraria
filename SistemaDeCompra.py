import datetime as dt
from random import randint
import time


class SistemaDeCompra:
    def __init__(self, nome, telefone, cpf_cnpj, cpf_Ou_cnpj,endereço):
        self.nome = nome
        self.telefone = telefone
        self.endereço = endereço

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
        endereço = input('Digite o seu endereço:')
        telefone = SistemaDeCompra.onlyInt('Digite o seu telefone:')
        cpf_cnpj = SistemaDeCompra.onlyInt('Digite o seu cpf/cnpj:\n')
        
        return SistemaDeCompra(nome,telefone, cpf_cnpj,cpf_Ou_cnpj,endereço)
    
    livros =[{
            
            'nome':'A Arte da Guerra',
            'autor':'Sun Tzu',
            'assunto':' Estratégia Militar',
            'Editora':'Estratégia Publicações',
            'Preço': 'R$ 25,00',
            'estoque':2 
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
                            
            }]
    def compras(livros):
        
        
        livrosComprados = []
        dataComprada = []
        ISBN = []
        while True:
            sistema = 0
            contador = 1
            compra = 0
            
            
            try:
                for x in range(len(livros)):
                    
                    if  livros[x]['nome'] == RemoverDoEstoque:
                        livros[x]['estoque'] -= 1
                        break
            except :
                pass
            RemoverDoEstoque = None
            
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

                    compra = SistemaDeCompra.onlyInt('Qual livro quer comprar?:\n==>')
                compra -= 1 
                if livros[compra]['estoque'] >0:
                    
                    livrosComprados.append(livros[compra]['nome'])
                    dataComprada.append(str(dt.date.today()))
                    ISBN.append(randint(0,50000))
                    RemoverDoEstoque = livrosComprados[-1]
                    input(f'A loja agradece pela compra de "{livros[compra]['nome']}"(precione enter para continuar)')
                else:
                    print('acabou',livros[compra]['nome'],'no estoque!!Que pena!')
                    input('(precione enter para continuar)')
                
                
                
            elif sistema == 2:
                contador = 1
                book = 0
                for livro in livros:
                
                    print (f'{contador}){livro['nome']}')
                    contador += 1
                    
                while book <1 or book >5:

                    book = SistemaDeCompra.onlyInt('Qual livro quer informações?:\n==>')
                    
                book -= 1
                print('======================================')
                for informaçao in livros[book]:
                    print(informaçao,':',livros[book][informaçao])
                print('======================================')       
                      
                input('(enter para voltar as compras)')

            else:
                compras = {
                    'livros':livrosComprados,
                    'ISBN':ISBN,
                    'data':dataComprada 
                }
                
                return compras,livros
    
    def salva_cliente(cliente,compras): 
        
        try:
            return{
                'nome':cliente.nome,
                'cpf':cliente.cpf,
                'telefone':cliente.telefone,
                'endereço':cliente.endereço,
                'compras':compras
                
            }
        except:
            return{
            'nome':cliente.nome,
            'cnpj':cliente.cnpj,
            'telefone':cliente.telefone,
            'endereço':cliente.endereço,
            'compras':compras
            
            
        }    
        
    def mostraClientes(todos_clientes):
        
        if (len(todos_clientes) == 0):
            
            print('==========================================\nAinda não existe usuarios,crie o primeiro!\n==========================================')
            return None
        else:
            print('=================================')
            print('=============Usuarios============')
            for i in range(len(todos_clientes)):
                print(f'{i+1}){todos_clientes[i]['nome']}')
                
            print(f'{len(todos_clientes)+1})criar novo usuario para o cliente')
            print(f'{len(todos_clientes)+2})fechar o programa')
            print('=================================')
            
            usuario_selecionado = (SistemaDeCompra.onlyInt('==>')-1)
            if len(todos_clientes) == usuario_selecionado:
                usuario_selecionado = None
            return usuario_selecionado
        

    def oqueFara(usuario_selecionado):
        valor = 0
        print('Oque voce fara?\n1)Ver os livros comprados\n2)Ver dados\n3)Comprar mais\n4)Mudar usuario')
        while valor <1 or valor >4:
            valor =SistemaDeCompra.onlyInt('==>')
            
        return valor
    
    def ver_informaçoes_livros(usuario_selecionado,todos_usuarios):
        print(todos_usuarios[usuario_selecionado]['nome'])

        for i in range(len(todos_usuarios[usuario_selecionado]['compras']['livros'])):
            print('=============================')           
            print('Livro:',todos_usuarios[usuario_selecionado]['compras']['livros'][i])
            print('ISBN:',todos_usuarios[usuario_selecionado]['compras']['ISBN'][i])            
            print('Data comprado:',todos_usuarios[usuario_selecionado]['compras']['data'][i]) 
            print('=============================')
            
        if len(todos_usuarios[usuario_selecionado]['compras']['livros']) == 0:
            print('=============================') 
            print('Não comprou livros ainda!!')
            print('=============================') 
        input('(precione enter para continuar)')
            
        
    def ver_informaçoes(usuario_selecionado,todos_usuarios):
        cpf_cnpj = 0
        try:
            todos_usuarios[usuario_selecionado]['cpf'] = todos_usuarios[usuario_selecionado]['cpf']
            cpf_cnpj = 1
        except:
            todos_usuarios[usuario_selecionado]['cnpj'] = todos_usuarios[usuario_selecionado]['cnpj']
            cpf_cnpj = 2
        print('===========================')
        print(f'Nome:{todos_usuarios[usuario_selecionado]['nome']}')
        print(f'Telefone:{todos_usuarios[usuario_selecionado]['telefone']}')
        print(f'Endereço:{todos_usuarios[usuario_selecionado]['endereço']}')
    

        if cpf_cnpj == 1:
            print(f'CPF:{todos_usuarios[usuario_selecionado]['cpf']}')
        else:
            print(f'CNPJ:{todos_usuarios[usuario_selecionado]['cnpj']}')
        print('===========================')
        input('(precione enter para continuar)')
        
    def pega_livros(usuario_selecionado,todos_usuarios):
        livros = []
        isbn = []
        data = []
        for i in range(len(todos_usuarios[usuario_selecionado]['compras']['livros'])):
                    
            livros.append(todos_usuarios[usuario_selecionado]['compras']['livros'][i])
            isbn.append(todos_usuarios[usuario_selecionado]['compras']['ISBN'][i]) 
            data.append(todos_usuarios[usuario_selecionado]['compras']['data'][i])
            return livros,isbn,data

    def funde_livros(compras,book,isbn,data):
        
        
        compras['livros'] = (compras['livros']+book)
        compras['ISBN'] = (compras['ISBN']+isbn)
        compras['data'] = (compras['data']+data)
        
        return compras
    
    def sair():
        print('Agradecemos por aparecer')
        time.sleep(0.5)
        print('...')
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('..')
