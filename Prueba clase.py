class Impresora:

    def __init__(self, papel, tinta):
        self.tinta = tinta 
        self.papel = papel
        
    def imprimir(self):
        print("Imprimí ", self.papel, "hojas de papel" "con una tinta de color ", self.tinta)
mi_impresora = Impresora( 2, "verde")

# Call the imprimir method to print the message
mi_impresora.imprimir() 



