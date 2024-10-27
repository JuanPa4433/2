class Impresora:

    def __init__(self, tinta, papel,):
        self.tinta = tinta 
        self.papel = papel

    def imprimir(self):
        print("Imprimí ", self.papel, "hojas de papel", "con una tinta de color ", self.tinta)

mi_impresora = Impresora("Verde", 2 )

mi_impresora.imprimir()  



    


    
    


