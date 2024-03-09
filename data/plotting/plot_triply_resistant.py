import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = '../g_freqs.csv'
data = pd.read_csv(csv_file_path, header=None)

columns_to_sum = [7, 11, 13, 14, 15] # triply resistant clones
data['sum_values'] = data.iloc[:, columns_to_sum].sum(axis=1)

print(data['sum_values'])

plt.figure(figsize=(20, 10))
plt.plot(data.index, data['sum_values'])
plt.title('Frequency of triply resistant clones over generations')
plt.xlabel('Generation')
plt.ylabel('Frequency of triply resistant clones')
plt.grid(True)
plt.ylim(0, 1)
plt.show()
