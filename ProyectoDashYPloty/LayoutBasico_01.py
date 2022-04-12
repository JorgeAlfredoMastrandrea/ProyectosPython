# help
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

from fpdf import FPDF

# fuentes de texto :
# Trabajo
FuentesTrabajo = 'D:/GIT/Python/ProyectosPython/ProyectoDashYPloty/fuentes/Lato-Italic.ttf'
# Notebook 
FuentesNotebook = 'C:/Users/bigja/Documents/GIT/ProyectosPython/PythonDASH_PLOTLY_PDF/PythonPDF/fuentes/Lato-Italic.ttf'

# Textos
textoPágina_01 = 'textos/01-TextoPrimeraPágina.txt'

class PDF(FPDF):
        
    def header(self):
        print("...setting tamaño a Portrait , mm , A4...")
        FPDF('P',  'mm', 'A4')        
        print("...setting imagen en la cabecera con el logo de la Dirección de Evaluación...")
        self.image('logos/membrete.png', 0 , 0 , 210)
        return
    
    def footer(self):
        return
    
    def AgregarFuentes(self):
        self.add_font('Lato-Black','',FuentesTrabajo, uni=True)
        self.add_font('Lato-BlackItalic','',FuentesTrabajo, uni=True)
        self.add_font('Lato-Bold','',FuentesTrabajo, uni=True)
        self.add_font('Lato-BoldItalic','',FuentesTrabajo, uni=True)
        self.add_font('Lato-Italic','',FuentesTrabajo, uni=True)
        self.add_font('Lato-Light','',FuentesTrabajo, uni=True)
        self.add_font('Lato-LightItalic','',FuentesTrabajo, uni=True)
        self.add_font('Lato-Regular','',FuentesTrabajo, uni=True)
        self.add_font('Lato-Thin','',FuentesTrabajo, uni=True)
        self.add_font('Lato-ThinItalic','',FuentesTrabajo, uni=True) 
    
    def ImprimirLineas(self , cadaMM):
        # color
        self.set_draw_color(236 , 236  , 236)
        # horizontales
        for x in range(0 , 210 , cadaMM):
            self.line(x, 0 , x , 297)
        # verticales
        for y in range(0 , 297 , cadaMM):
            self.line(0, y , 210 , y)
            
    def LeerTexto(self , texto):
        # Leer archivo de texto
        with open(texto, 'rb') as fh:
            elTexto = fh.read().decode('utf8')
        return elTexto
    
    def LayoutPaginaInicio(self):
        print("...colocando los elementos de la primera página...")
        print("...leyendo texto de la primeta página...")
        textoPagina_01 = self.LeerTexto(textoPágina_01)
        self.set_fill_color(0 , 255  , 0)
        self.set_font('Lato-Italic', '', 10)
        self.set_xy(10 , 65) 
        self.multi_cell(90 , 5 , textoPagina_01 , True , 'C' , True) # ancho de la celda y alto de la celda
        self.set_xy(110 , 65) 
        self.multi_cell(90 , 5 , textoPagina_01 , True , 'C' , True) # ancho de la celda y alto de la celda
        self.image('imagenes/fig1.png', 15 , 130 , 180 , 120)
        self.ln()
        return
    
    def LayoutPaginaDos(self):
        print("...agrego otra página...")
        self.add_page()
        print("...colocando los elementos de la primera página...")
        print("...leyendo texto de la primeta página...")
        textoPagina_01 = self.LeerTexto(textoPágina_01)
        self.set_fill_color(0 , 255  , 0)
        self.set_font('Lato-Italic', '', 10)
        self.set_xy(10 , 65) 
        self.multi_cell(90 , 5 , textoPagina_01 , True , 'C' , True) # ancho de la celda y alto de la celda
        self.set_xy(110 , 65) 
        self.multi_cell(90 , 2 , textoPagina_01 , True , 'C' , True) # ancho de la celda y alto de la celda
        self.image('imagenes/fig1.png', 15 , 130 , 180 , 120)
        self.ln()
        return
    
    def SettingPágina(self , imprimeLineas , cadaMM):
        """setea la página de referencia, 
        en caso de que sea True el primer valor, 
        se dibujarán las líneas de referencia
        """
        print("...setenado márgenes...")
        self.set_left_margin(0)
        self.set_right_margin(210)
        self.set_top_margin(0)        
        print("...Agregando la página antes de comenzar a dibujar algo...")
        self.add_page()
        if imprimeLineas == True:
            self.ImprimirLineas(cadaMM)
        return        

pdf = PDF()
#agregar todas la fuentes de la tipografía Lato
pdf.AgregarFuentes()
pdf.SettingPágina(True , 5)
#pdf.LayoutPaginaInicio()
#pdf.LayoutPaginaDos()

pdf.output('LayoutBasico_01.pdf', 'F')
