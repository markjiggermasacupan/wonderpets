from flask import Flask, render_template

import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def add_entries_to_vendor_table(supabase, vendor_count):
    fake = Faker()
    foreign_key_list = []
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    for i in range(vendor_count):
        value = {'vendor_name': fake.company(), 'total_employees': fake.random_int(40, 169),
                 'vendor_location': fake.country()}

        main_list.append(value)
    data = supabase.table('Vendor').insert(main_list).execute()
    data_json = json.loads(data.json())
    data_entries = data_json['data']
    for i in range(len(data_entries)):
        foreign_key_list.append(int(data_entries[i]['vendor_id']))
    return foreign_key_list


def add_entries_to_product_table(supabase, vendor_id):
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    main_list = []
    iterator = fake.random_int(1, 15)
    for i in range(iterator):
        value = {'id picture': vendor_id, 'product_name': fake.ecommerce_name(),
                 'inventory_count': fake.random_int(1, 100), 'price': fake.random_int(45, 100)}
        main_list.append(value)
    data = supabase.table('Product').insert(main_list).execute()


def main():
    vendor_count = 10
    load_dotenv()
    url: str = os.environ.get("https://pbwmdpuznvbagayomxun.supabase.co")
    key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBid21kcHV6bnZiYWdheW9teHVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NjYwMTYxNjksImV4cCI6MTk4MTU5MjE2OX0.dGjKEwQuc8iOUogPadgLhBp-eUoq_RGXwCFAmPYhvl8")
    supabase: Client = create_client(url, key)
    fk_list = add_entries_to_vendor_table(supabase, vendor_count)
    for i in range(len(fk_list)):
        add_entries_to_product_table(supabase, fk_list[i])


main()

app.run(host="localhost", debug=True)