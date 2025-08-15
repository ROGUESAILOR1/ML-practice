import numpy as np,seaborn as sns
from numpy import random as ran
import matplotlib.pyplot as plt,csv
random_sizes=ran.randint(5,50,50)
random_numbers = random_sizes * 2_000_000 + (random_sizes ** 1.5) * 500_000 + ran.randint(0, 1_000_000, 50)

random_sizes=random_sizes.tolist()
random_numbers=random_numbers.tolist()
datapairs=list(zip(random_sizes,random_numbers))
datapairs.sort(key=lambda x:x[0])
sorted_sizes,sorted_numbers=map(list,zip(*datapairs))
sorted_numbers.insert(0,"Price(PKR)")
sorted_sizes.insert(0,"Size(Marla)")

with open(r"C:\Users\PC\Desktop\data.csv","w",newline='')as file:
  writer=csv.writer(file)
  #writer.writerow(['Size(Marla)', 'Price(PKR)'])
  for s,p in zip(sorted_sizes,sorted_numbers):
    writer.writerow([s,p])

with open(r"C:\Users\PC\Desktop\data.csv","r",newline='')as file:
  reader=csv.DictReader(file)
  data=list(reader)

sizes=[]
prices=[]
for row in data:
  s_val=int(row['Size(Marla)'])
  p_val=float(row['Price(PKR)'])
  sizes.append(s_val)
  prices.append(p_val)
x_train=np.array(sizes)
y_train=np.array(prices)

sum_sizes=np.sum(x_train)
sum_prices=np.sum(y_train)
squared_sizes=np.sum(x_train**2)
sum_xy=np.sum(x_train*y_train)
N=len(sizes)
avg_sizes=sum_sizes/N
avg_prices=sum_prices/N
weight=(N*sum_xy-(sum_sizes*sum_prices))/(N*squared_sizes-sum_sizes**2)
bias=avg_prices-(weight*avg_sizes)

plt.scatter(x_train,y_train , marker='x', c='r')
plt.plot(x_train,y_train ,c='g')
plt.plot(x_train,weight*x_train+bias,c='b')

plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel(f'Price (PKR)')
# Set the x-axis label
plt.xlabel('Size (Marla)')
plt.show()
def predict(x):
  return weight*x+bias
x=float(input("Enter the size(Marlas) to estimate the price: "))
print(f"The estimated price for size:{x} Marlas is:{predict(x):.2f}")
