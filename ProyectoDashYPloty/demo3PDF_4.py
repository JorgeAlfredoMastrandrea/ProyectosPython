from fpdf import FPDF

title = '20000 Leagues Under the Seas'
# Trabajo
FuentesTrabajo = 'D:/GIT/Python/ProyectosPython/ProyectoDashYPloty/fuentes/Lato-Italic.ttf'
# Notebook 
FuentesNotebook = 'C:/Users/bigja/Documents/GIT/ProyectosPython/PythonDASH_PLOTLY_PDF/PythonPDF/fuentes/Lato-Italic.ttf'

class PDF(FPDF):
    def tamaño(self):
        # Portrait , A4        
        self.add_page('P', 'mm', 'A4')        
    
    def header(self):
        print("tamaño")
        FPDF('P',  'mm', 'A4')
        self.image('logos/membrete.png', 0 , 0 , 210)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calcular ancho del texto (title) y establecer posición
        # w = self.get_string_width(title) + 6
        # self.set_x((210 - w) / 2)
        # Colores del marco, fondo y texto
        # self.set_draw_color(0, 80, 180)
        # self.set_fill_color(230, 230, 0)
        # self.set_text_color(220, 50, 50)
        # Grosor del marco (1 mm)
        # self.set_line_width(1)
        # Titulo
        # self.cell(w, 9, title, 1, 1, 'C', 1)
        # Salto de línea
        self.ln(10)

    def footer(self):
        # Posición a 1.5 cm desde abajo
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Color de texto en gris
        self.set_text_color(128)
        # Numero de pagina
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Lato-Italic', '', 12)
        # Color de fondo
        self.set_fill_color(200, 220, 255)
        # Titulo
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Salto de línea
        self.ln(4)

    def chapter_body(self, name):
        # Leer archivo de texto
        with open(name, 'rb') as fh:
            txt = fh.read().decode('utf8')
        # Times 12
        self.set_font('Lato-Italic', '', 10)
        # Emitir texto justificado
        # self.cell(0, 15, txt)
        # multi_cell(w: float, h: float, txt: str, border = 0, align: str = 'J', fill: bool = False)
        self.set_fill_color(255 , 0  , 255)
        self.set_xy(10 , 65)
        self.multi_cell(150 , 5 , txt , True , 'C' , True) # ancho de la celda y alto de la celda
        #self.set_xy(10 , 150)
        self.image('imagenes/fig1.png', 10 , 150 , 175 , 125)
        #self.multi_cell(190 , 180 , txt , True , 'C' , True)
        # Salto de línea
        self.ln()
        # Mención en italic -cursiva-
        # self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')

    def print_lineas(self):
        # color
        self.set_draw_color(236 , 236  , 236)
        # horizontales
        for x in range(0 , 210 , 5):
            self.line(x, 0 , x , 297)
        # verticales
        for y in range(0 , 297 , 5):
            self.line(0, y , 210 , y)
        
    
    def print_chapter(self, num, title, name):
        #self.set_left_margin(0)
        #self.set_right_margin(297)
        self.add_page()
        self.print_lineas()        
        #self.chapter_title(num, title)
        self.chapter_body(name)
        

pdf = PDF()
# pdf.add_font(family: str, style = '', fname = '', uni = False)
# paths de las fuentes:


pdf.add_font('Lato-Italic','',FuentesNotebook, uni=True)
pdf.set_title(title)
pdf.set_author('Jules Verne')
pdf.print_chapter(1, 'A RUNAWAY REEF', 'textos/texto1.txt')
pdf.print_chapter(2, 'THE PROS AND CONS', 'textos/texto2.txt')
pdf.output('tuto3.pdf', 'F')