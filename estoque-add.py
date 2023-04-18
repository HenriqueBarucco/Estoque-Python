# -*- coding: utf-8 -*-
import pandas as pd
import requests

df = pd.read_excel("2022.xlsx", sheet_name="Plan1")

for index, row in df.iterrows():
    item_name = str(row["A"])
    model = row["C"]
    qnt = row["D"]
    price = row["E"]

    # Dividindo o texto em duas partes
    values = item_name.split(" ", 1)
    print(values[1])
    #text = values[1] # "175/65/14 GOODYEAR KELLY EDGE TOURING 82T"

    # Dividindo o texto restante em duas sub-partes
    values2 = values[1].split(" ", 1)
    measure = values2[0] # "175/65/14"
    product = values2[1] # "GOODYEAR KELLY EDGE TOURING 82T"

    print(measure) # "175/65/14"
    print(product) # "GOODYEAR KELLY EDGE TOURING 82T"

    if model != model:
        model = ""

    unitPrice = price/qnt
    unitPriceFormatted = round(unitPrice, 2)

    payload = {"name": product, "model": model, "measure": measure, "available": 1000, "price": unitPriceFormatted}

    try:
        response = requests.post("https://estoque-api.henriquebarucco.com.br/products", json=payload)
        print(response.status_code)
        response.raise_for_status()

        data = response.json()

        payload = {"productId": data.get("id"), "quantity": qnt}
        response = requests.post("https://estoque-api.henriquebarucco.com.br/sales", json=payload)
        print(response.status_code)
    except:
        print("Produto já no estoque")