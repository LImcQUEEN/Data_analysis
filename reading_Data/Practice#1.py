import pandas as pd
import matplotlib.pyplot as plt
# filepath = "btc-market-price.csv"
# with open(filepath, 'r') as reader:
#     for index, line in enumerate(reader.readlines()):
#         if index < 10:
#             print(index, line)
df = pd.read_csv('btc-market-price.csv',
                 header=None,
                 na_values=['', '?', '-'],
                 names=['Timestamp', 'Price'],
                 dtype={'Price': 'float'},
                 parse_dates=[0])