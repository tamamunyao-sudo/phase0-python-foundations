import csv
import email_sender
import invoice_generator
from datetime import datetime

with open("invoice_log.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Client", "Invoice Number", "Status", "Date"])

with open("clients.csv", "r") as csvfile:
    clients = csv.DictReader(csvfile)
    for index, client in enumerate(clients):
        invoice_number = index + 1

        pdf_path = invoice_generator.create_invoice(client, index+1)
        email_status = email_sender.send_email(client, pdf_path)

        if email_status:
            client["Status"] = "Sent"
        else:
            client["Status"] = "Failed"

        with open("invoice_log.csv", "a") as csvfile2:
            csvwriter = csv.writer(csvfile2)
            csvwriter.writerow([client["Client"], f"INV-00{invoice_number}", client["Status"], datetime.now().strftime("%Y-%m-%d")] )