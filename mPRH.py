from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

def conv_csv():
    ppg=[]
    with open("/home/sathvik/Documents/CEERI/PHASE 2/PPG data.txt","r") as text_data:
        for i in text_data:
          ppg.append(i.strip("\n"))
          ppg=list(map(float,ppg))  
    #print(ppg)    
    return ppg

def butterworth(data):
    data=[]
    fs = 25  # Sampling frequency
# Generate the time vector properly
    t = np.arange(1000) / fs
    signala = np.sin(2*np.pi*100*t) # with frequency of 100
    plt.plot(t, signala, label='a')


    signalc = signala
    plt.plot(t, signalc, label='c')

    fc = 4  # Cut-off frequency of the filter
    w = fc / (fs / 2) # Normalize the frequency
    b, a = signal.butter(3, w, 'low')
    output = signal.filtfilt(b, a, signalc)
    plt.plot(t, output, label='filtered')
    plt.legend()
    plt.show()
    data=output
    return data

peak_height=[]
def mPRH(pat1):
    crests=[]
    troughs=[]
    t=[i for i in range(0,8)]
    left=1
    while (left+10)<999:
        curdata=pat1[left:left+10]
        #print(len(curdata))
        crest=np.max(curdata)
        #print(crest)
        crests.append(crest)
        trough=min(list(map(float,curdata)))
        #print(trough)
        troughs.append(trough)
        peak_rise = np.subtract(crest,trough)
        #print(peak_rise)
        peak_height.append(peak_rise)
        left=left+128
    #print(crests)   
    plt.plot(t,crests,label='crests')
    plt.plot(t,troughs,label='troughs')
    plt.show()
    mPRH=np.median(peak_height)  
    return mPRH

if __name__=="__main__":
    data=[]
    filtlist=[]
    data=conv_csv()
    filtered=butterworth(i.split() for i in data)
    print(len(filtered))
    for i in filtered:
        filtlist.append(i)
    #print(filtlist)
    df=pd.DataFrame({'Filtered':filtlist})
    df.to_csv("/home/sathvik/Documents/CEERI/PHASE 2/filtered.csv")
    print(mPRH(filtlist))
