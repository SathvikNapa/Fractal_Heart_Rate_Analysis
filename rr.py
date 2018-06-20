##code to find RR interval

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


ecg=pd.read_csv("path")
time=ecg['time'].tolist()
mv=ecg['channel1'].tolist()

def rri():
	beatcount=0
	i=0
	rr=0

	rri=[]

	for k in range(2,len(mv)-1):
		if (mv[k]>mv[k-1] and mv[k]<mv[k+1] and mv[k]>0.25):
			beatcount=beatcount+1
			if 	beatcount==1:
				rr=0
			elif beatcount!=0:
				rr=k-i
				rri[k].append(rr)
				i=k

if __name__=='__main__':
	rri()