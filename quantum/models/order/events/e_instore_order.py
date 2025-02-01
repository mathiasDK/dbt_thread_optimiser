import pandas as pd
import random
from datetime import datetime, timedelta

def model(dbt, session):

    n = 1000
    n_customers = 100
    n_stores = 10
    order_ids = [f'po_{1000+i}' for i in range(n)]
    customers = [f'c_10xx_{i}' for i in range(n_customers)]
    stores = [f's_{i}' for i in range(n_stores)]
    order_dates = [(datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d') for _ in range(n)]

    data = {
        'order_id': order_ids,
        'customer_id': [random.choice(customers) for _ in range(n)],
        'store_id': [random.choice(stores) for _ in range(n)],
        'date': order_dates
    }

    df = pd.DataFrame(data)

    return df