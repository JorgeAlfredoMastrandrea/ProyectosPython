# en este archivo voy a hacer un objeto pdf mediante la clase FPDF

# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

from fpdf import FPDF

class PDF(FPDF):
    
    def tamaño(self):
        # Portrait , A4
        self.add_page('P', 'A4')

    # pie de página
    def footer(self):
        # posicionarse a 1.5 cm desde abajo
        # seleccionar texto
        # poner número de página
        print("footer")        
    
    # cabecera
    def header(self):        
        # logo
        self.image('logos/membrete.png', 0 , 0 , 210)        
        # set_font(string family [, string style [, float size]])
        self.set_font('Arial', 'B', 12)        
        # posicionarse
        # título
        # salto de linea
       

    def cuerpo(self,  name):        
        self.set_font('Arial', 'B', 12)
        self.cell(0, 5, 'Alineado Centrado'  , True , 2 , 'C')
        self.image('logos/logo_1.png', 0 , 0 , 210)
        print("cuerpo")
    
    

pdf = PDF()
pdf.cuerpo("cuerpo")
pdf.output('tuto2.pdf', 'F')



