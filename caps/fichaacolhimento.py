
from reportlab.pdfgen import canvas

def genPef():
    c = canvas.Canvas("Olamundo.pdf")
    c.drawString(100, 750, "Welcome to Reportlab!")
    c.save()



