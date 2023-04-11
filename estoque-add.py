# -*- coding: utf-8 -*-
import pandas as pd
import requests

df = pd.read_excel("dados-estoque.xlsx", sheet_name="Plan1")

for index, row in df.iterrows():
    item_name = row["A"]
    description = row["C"]
    qnt = row["D"]
    price = row["E"]

    if description != description:
        description = ""

    unitPrice = price/qnt
    teste = round(unitPrice, 2)

    payload = {"name": item_name, "description": description, "available": 1000, "price": teste}

    response = requests.post("https://estoque-api.henriquebarucco.com.br/products", json=payload)

    print(f"Status code: {response.status_code}")
