import random
import string
import json
from datetime import datetime, timedelta

# Function to generate a random string
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate and save dummy customer invoices
def generate_and_save_dummy_invoices(num_invoices, filename):
    invoices = []
    customer_name = generate_random_string(10)
    vat_percentage = random.randint(5, 25)  # Random VAT percentage between 5% and 25%
    konstnadskonto = random.randint(1000, 9999)  # Random konstnadskonto between 1000 and 9999
    today = datetime.now()
    for _ in range(num_invoices):
        invoice_number = generate_random_string(8)
        amount = round(random.uniform(100, 1000), 2)
        due_date = today - timedelta(days=random.randint(14, 44))  # Random due date between 2 weeks ago and 1 month in the future
        is_paid = random.choice([True, False])  # Randomly set the 'paid' field to True or False
        invoice = {
            "invoice_number": invoice_number,
            "customer_name": customer_name,
            "amount": amount,
            "vat_percentage": vat_percentage,
            "konstnadskonto": konstnadskonto,
            "due_date": due_date.strftime('%Y-%m-%d'),
            "paid": is_paid
        }
        invoices.append(invoice)

    # Save the generated invoices to a JSON file
    with open(filename, "w") as file:
        json.dump(invoices, file)

    print("Data saved to", filename)

# Generate and save 10 dummy invoices for one customer
