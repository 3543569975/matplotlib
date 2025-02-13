import pandas as pd
import random as r
import matplotlib.pyplot as plt

num1 = []
num2 = []
r.seed(9)

for i in range(100):
    y = r.gauss(10,4)
    x = r.gauss(10,4)
    y1 = r.vonmisesvariate(0,1)*4
    x1 = r.vonmisesvariate(0,1)*4
    #y2 = r.gauss(-10,10)
    #x2 = r.gauss(70,10)

    num1.append([y,y1])
    num2.append([x,x1])

plt.figure()
plt.scatter(num2,num1)
plt.show()

'''
df = pd.DataFrame({'Exam1': num1, 'Exam2': num2,'Pass': num3,})
df = df.set_index('Exam1')
df.to_excel('examdata.xlsx')


from sklearn.datasets import make_regression
x,y = make_regression(n_samples=100,n_features=1,n_targets=1,noise=15,random_state=100)


data = pd.read_excel('examdata.xlsx')
ls = []
ll = []

 

for index,row in data.iterrows():
    column1_value = row['Exam1']
    column2_value = row['Exam2']
    ll.append(column2_value)
    if 60 <= int(column1_value) and 60 <= int(column2_value):
        ls.append(1)
    else:
        ls.append(0)
print(ll[1])
df = pd.DataFrame({'Exam1': num1, 'Exam2': num2,'Pass': ls,})
df = df.set_index('Exam1')
df.to_excel('examdata.xlsx')

print(data.index())
ll = []
for index,row in data.iterrows():
    column1_value = row['Exam1']
    column2_value = index['Exam1']
    ll.append(column2_value)
    if 60 <= int(column1_value):
        ls.append(1)
    else:
        ls.append(0)
print(ll[1])
'''