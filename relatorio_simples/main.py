import pandas as pd

carros_vendidos = {
    'Carros': ['Onix', 'Polo', 'Argo', 'Kwid','HB20'],
    'Ano': [2022,2024,2022,2025,2022],
    'Valor': [50000.00,70000.00,55000.00,80000.00,45000.00]
    }

df = pd.DataFrame(carros_vendidos)

relatorio = df.to_string(index=False)

with open('vendas.txt','w',encoding='utf-8') as arquivo:
    arquivo.write('RELATORIO DE VENDAS DE CARROS\n')
    arquivo.write('='*40 + '\n')
    arquivo.write(relatorio)