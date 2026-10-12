class cartao:

   def __init__(self, num, cor):
    self.num = num
    self.cor = cor
    self.proximo = None
      
class listaEncadeadaSimples:

    def __init__(self,):
        self.head = None
        self.nA = 201
        self.nV = 1
        self.lista_ = []
        
    def inserirSemPrioridade(self, nodo=None):
        if self.head is None: 
            self.head = nodo 
            return 
        
        nodo_atual = self.head 
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        
        nodo_atual.proximo = nodo
        return
    
    def inserirComPrioridade(self, nodo=None):
        if self.head is None: 
            self.head = nodo  
            return 
        
        if self.head.proximo is None:
            self.head.proximo = nodo
            return
                          
        if self.head.cor == 'V':
            nd = self.head
            self.head = nodo 
            nodo.proximo = nd
            return
                             
        nodo_atual = self.head
             
        while nodo_atual.proximo != None:
            n = nodo_atual           
            nodo_atual = nodo_atual.proximo 
            
            if nodo_atual.cor == 'A':
                nod = nodo_atual 
                nodo_atual = nodo_atual.proximo 

                if nodo_atual is None:
                    nodo_atual = nodo
                    nod.proximo = nodo
                    return
                
                elif nodo_atual.cor == 'V':
                    nd = nodo_atual
                    nodo_atual = nodo 
                    nodo.proximo = nd
                    nod.proximo = nodo
                    return
                
                elif nodo_atual.cor == 'A' and nodo_atual.proximo is None:
                    nodo_atual.proximo = nodo
                    return
                
                elif nodo_atual.cor == 'A':
                    continue 
                 
            elif nodo_atual.cor == 'V':
                nd = nodo_atual
                nodo_atual = nodo 
                nodo.proximo = nd
                n.proximo = nodo  
                return    
        
    def inserir(self,):
        
        cor = str(input('Adicione a cor do cartão A|V: '))
        while(cor):
            
            if cor == 'A':
                self.inserirComPrioridade(cartao(self.nA,'A'))
                self.nA += 1
                break
            elif cor == 'V':
                self.inserirSemPrioridade(cartao(self.nV,'V'))
                self.nV += 1
                break
            else:
                print('Caracter inválido, use apenas A ou V em maiúsculo')
                cor = str(input('Adicione a cor do cartão A|V: '))
                continue
        
    def imprimirListaEspera(self,):
        self.lista_.clear()
        lista = []
        nodo_atual = self.head
        self.lista_.append(self.head)
        
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo  
            self.lista_.append(nodo_atual)
        for obj in self.lista_:
            lista.append(f'[{obj.cor}, {obj.num}]')
    
        print('Lista => ' + " ".join(lista))
            
    def atenderPaciente(self,):
        print(f'\nAtendendo o paciente cartão cor {self.head.cor} e número {self.head.num}')
        newHead = self.head.proximo
        self.head = newHead
        
        
# PROGRAMA PRINCIPAL:    
ls = listaEncadeadaSimples() 
print('\nSISTEMA DE TRIAGEM\n')  
while(True):
                         
    print('\nEcolha as opções: ')
    print(' 1 - Adicionar paciente a fila. ')
    print(' 2 - Mostrar paciente na fila. ')
    print(' 3 - Chamar paciente. ')
    print(' 4 - Sair. ')
    
    try:
        opc = int(input('>'))
    except:
        print('\nTipo inválido, encolha apenas uma dessas opções:')
        continue
    
    if opc == 1 :
        ls.inserir()
        
    elif opc == 2:
        try:
            ls.imprimirListaEspera()
        except:
            print('\nLista vazia, insira pelomenos um paciente!')
        
    elif opc == 3:
        try:
            ls.atenderPaciente()
        except:
            print('\nLista vazia, insira pelomenos um paciente!')
                    
    elif opc == 4:
        break
    else:
        print('Opção inválida, encolha apenas uma dessas opções:')
        continue
        
print('Programa encerrado!')
