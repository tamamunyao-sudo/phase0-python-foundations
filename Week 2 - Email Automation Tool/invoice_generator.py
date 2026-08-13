from reportlab.pdfgen import canvas

def create_invoice(client, invoice_number):
    pdf_path = f"INV-00{invoice_number}_{client['Client']}.pdf"

    client_pdf = canvas.Canvas(pdf_path)

    client_pdf.line(50, 800, 540, 800)
    client_pdf.drawString(205, 770, "TAMA AUTOMATION AGENCY")
    client_pdf.drawString(265, 740, "INVOICE")
    client_pdf.drawString(50, 700, f"Invoice #: INV-00{invoice_number}")
    client_pdf.drawString(435, 700, "Date: July 28, 2026")
    client_pdf.line(50, 670, 540, 670)

    client_pdf.drawString(50, 640, "Bill To:")
    client_pdf.drawString(50, 610, f"{client['Client']}")
    client_pdf.line(50, 590, 540, 590)

    client_pdf.drawString(50, 560, "Service")
    client_pdf.drawString(50, 540, f"{client['Service']}")
    client_pdf.drawString(435, 560, "Amount")
    client_pdf.drawString(435, 540, f"{client['Amount']}.00")
    client_pdf.line(50, 510, 540, 510)

    client_pdf.drawString(50, 480, "TOTAL")
    client_pdf.drawString(435, 480, f"{client['Amount']}.00")
    client_pdf.line(50, 450, 540, 450)

    client_pdf.drawString(50, 420, "Payment Due: August 11, 2026")
    client_pdf.setFont("Helvetica", 11)
    client_pdf.drawString(50, 390, "Thank you for your business!")
    client_pdf.drawString(50, 370, "If you have any questions, contact: ")
    client_pdf.drawString(50, 350, "tama.munyao@gmail.com")
    client_pdf.line(50, 320, 540, 320)

    client_pdf.save()

    return pdf_path

