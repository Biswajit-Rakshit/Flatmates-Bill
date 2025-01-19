"""
This code is not a part of project
It is just written for basic understanding of the fpdf package
"""

from fpdf import FPDF

pdf = FPDF(orientation='P',unit='pt',format='A4')
pdf.add_page()

# Add some text
pdf.set_font(family='Times',size=24,style='B')
pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1,align="C", ln=1)
pdf.cell(w=100, h=40, txt="Period :", border=1)
pdf.cell(w=150, h=40, txt="March 2024", border=1)

pdf.output("bill.pdf")
