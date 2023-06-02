import time
import pandas as pd
import matplotlib.pyplot as plt
import concurrent.futures

start_time = time.time()

files = ['sales_data/sales_2017.csv', 'sales_data/sales_2018.csv', 'sales_data/sales_2019.csv']

def read_csv(file):
    return pd.read_csv(file)

with concurrent.futures.ThreadPoolExecutor() as executor:
    data = list(executor.map(read_csv, files))

x_values = []
y_values = []

for df in data:
    x_values.append(pd.to_numeric(df['Quantity Ordered'], errors='coerce'))
    y_values.append(pd.to_numeric(df['Price Each'], errors='coerce'))

plt.xlabel('Quantity Ordered')
plt.ylabel('Price Each')
plt.title('BOZO')

for x, y in zip(x_values, y_values):
    plt.plot(x, y)

plt.legend(['2017', '2018', '2019'])
plt.show()

plt.savefig('graph.png')


print(start_time)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")
