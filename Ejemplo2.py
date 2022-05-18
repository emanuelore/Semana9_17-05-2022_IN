import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_excel('BI_Clientes09.xlsx')
print(data.shape)
print(data.groupby('BikeBuyer').size())
sb.catplot('Gender', data=data,kind="count")
plt.show()
sb.catplot('SpanishOccupation',data=data,kind="count" ,aspect=2)
plt.show()
sb.catplot('Region',data=data, hue='BikeBuyer', kind='count')
plt.show()
sb.catplot('SpanishEducation',data=data,hue='BikeBuyer',kind='count',aspect=3)
plt.show()
sb.catplot('YearOfFirstPurchase',data=data,hue='BikeBuyer',kind='count',aspect=3)
plt.show()