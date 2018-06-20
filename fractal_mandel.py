import matplotlib.pyplot as plt 
import numpy as np 
import plotly
import math

k=[]
d=[]
for i in range(1,600):
	d=(math.sin(math.radians(i))+math.exp(i)+1)
	round(d,3)
	d.append(i)
	#print(d)
	#print(k)
	k.append(d)
j=i
#print(k)
p=pd.DataFrame(data=k,columns=['Values'])
p['time']=d

p.to_csv('fracs.csv',sep=',')
plt.show(plt.plot(k,np.sin(k),color='red'))
