import os
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

def weierstrass(x):
	a= [i for i in np.arange(0.1,1.0,0.1)]
	b=7
	e=0
	count=0
	g=[]
	for n in range(0,300):
		for j in a:
			if j*b>(1+1.5*3.14):
				d=(j)**n 
				c=np.cos((b**n) * 3.14 * x)
				#print(e)
				e=e+(d*c)
				g.append(e)
				count=count+1
	print(count)		
	plt.show(plt.plot(g))
	k=pd.DataFrame(data=g,columns=['Values'])
	k.to_csv('weierstrass.csv')

if __name__== '__main__':
	weierstrass(100)
