import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df_sorted = df.sort_values(by='km')

print(df_sorted)

plt.figure(figsize=(10, 6))
plt.plot(df_sorted['km'], df_sorted['price'], marker='o')
plt.title('Price vs Kilometers')
plt.xlabel('Kilometers (km)')
plt.ylabel('Price')
plt.grid(True)
plt.show()
