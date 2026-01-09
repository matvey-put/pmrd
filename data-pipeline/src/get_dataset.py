import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

def generate_synthetic_data(num_rows=1000):
    fake = Faker('ru_RU')
    data = []

    categories = ['Электроника', 'Одежда', 'Дом и сад', 'Спорт', 'Игрушки']
    statuses = ['Active', 'Discontinued', 'Out of Stock']

    for i in range(num_rows):
        product_id = i + 101
        
        price = round(random.uniform(10.5, 500.0), 2)
        stock_quantity = random.randint(0, 1000)
        rating = round(random.uniform(1.0, 5.0), 1)
        
        category = random.choice(categories)
        status = random.choice(statuses)
        
        start_date = fake.date_between(start_date='-2y', end_date='-1y')
        if random.random() > 0.8:
            end_date = start_date + timedelta(days=random.randint(30, 180))
            is_current = False
        else:
            end_date = None
            is_current = True

        data.append({
            "product_id": product_id,           
            "product_name": fake.catch_phrase(),
            "category": category,               
            "price": price,                   
            "stock_quantity": stock_quantity,   
            "rating": rating,                   
            "supplier_email": fake.email(),     
            "status": status,                 
            "effective_from": start_date,        
            "effective_to": end_date             
        })

    return pd.DataFrame(data)