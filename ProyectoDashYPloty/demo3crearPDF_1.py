# para crear un PDF, la idea es que se pueda crearlo, 
# agregarle un logo, texto y las imágenes de cada uno de los informes.

# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 12)

pdf.cell(0, 5, 'Alineado Izquierda' , True , 2)
pdf.cell(0, 5, 'Alineado Centrado'  , True , 2 , 'C')
pdf.cell(0, 5, 'Alineado Derecha'  ,  True , 2 , 'R')

#pdf.cell(0, 4, 'C')
#pdf.cell(1, 1, 'Powered by FPDF.', 0, 1, 'C')
pdf.output('tuto1.pdf', 'F')

# After including the library file, we create an FPDF object. 
# The FPDF constructor is used here with the default values: 
# pages are in A4 portrait and the measure unit is millimeter. 
# It could have been specified explicitly with:

pdf = FPDF('P', 'mm', 'A4')

# It is possible to use landscape (L), 
# other page formats (such as Letter and Legal) 
# and measure units (pt, cm, in).

# There is no page for the moment, 
# so we have to add one with add_page. 
# The origin is at the upper-left corner and the current position 
# is by default placed at 1 cm from the borders; the margins can be changed with set_margins.

# Before we can print text, it is mandatory to select a font with set_font, 
# otherwise the document would be invalid. We choose Arial bold 16:





