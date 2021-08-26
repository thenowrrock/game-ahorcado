class Conceptos:

    listaC = []
    tamano :int

    def __init__(self,tamano = 0):
        self.tam = tamano


    def agregar(self,titulo,concepto):
        self.listaC[titulo] = concepto


    def buscarT(self,titulo):
        if titulo in self.listaC:
            return True
        else:
            return False

    def buscarC(self,concepto):
        if concepto in self.listaC.values():
            return True
        else:   
            return False 

    def eliminar(self,titulo):
        if titulo in self.listaC:
           self.listaC.remove(titulo)
            
        else:
            print("No se logro encontrar :" + titulo) 
            return False    

    def editar(self,titulo):
        if titulo in self.listaC:
            self.listaC.index(titulo)
            return True
        else:
            print("No se logro remplazar :" + titulo)
            return False       
                  

    def imprimir(self):
        for t in self.listaC:
            print("")        
                                       