import matplotlib.pyplot as plt 
import numpy as np 
import plotly
import pandas as pd
k=[]
j=[]

for i in range(200,300):
	d=(i)**2 + 2
	#print(k)
	k.append(d)
	#print(k)
	j.append(i)
	#print(d)
j=i
#print(k)
p=pd.DataFrame(data=k,columns=['Values'])
p['time']=d

p.to_csv('fracs.csv',sep=',')

plt.show(plt.plot(k,np.sin(k),color='red'))
