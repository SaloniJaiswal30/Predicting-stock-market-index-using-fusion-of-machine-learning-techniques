import csv
import numpy
import pandas

def LoadCsv(filename):
    file=open(filename,"r")
    reader=csv.reader(file)
    next(reader)
    dataset=[r for r in reader]
    return dataset

def str_to_float(dataset):
    print(len(dataset))
    for i in range(len(dataset)):
        for j in range(1,len(dataset[i])):
            dataset[i][j]=float(dataset[i][j])
    return dataset

def simple_moving_average(dataset):
    moving_average=[]
    for i in range(9,len(dataset)):
        temp=0
        for j in range(i-9,i+1):
            #print(j,")",dataset[j][4])
            temp=temp+dataset[j][4]
            #print(temp)
        temp=temp/10
        #print(temp)
        #print("----------")
        moving_average.append(temp)
    return moving_average

def weighted_moving_average(dataset):
    weighted_average=[]
    for i in range(9,len(dataset)):
        temp=0
        k=1
        for j in range(i-9,i+1):
            #print(j,")",k,"*",dataset[j][4])
            temp=temp+k*dataset[i][4]
            k+=1
        temp=temp/(55)
        weighted_average.append(temp)
    return weighted_average

def momentum(dataset):
    mome=[]
    for i in range(9,len(dataset)):
        temp=dataset[i][4]-dataset[i-9][4]
        mome.append(temp)
    return mome

def stochastic_k(dataset):
    stoc=[]
    for i in range(9,len(dataset)):
        data=[j[2] for j in dataset[i-9:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-9:i+1]]
        ll=min(data)
        temp=((dataset[i][4]-ll)/(hh-ll))*100
        stoc.append(temp)
    return stoc

def stochastic_d(stochastick):
    stocd=[]
    for i in range(9,len(stochastick)):
        temp=0
        for j in range(i-9,i+1):
            temp=temp+stochastick[j]
        temp=temp/10
        stocd.append(temp)
    return stocd

def relative_strength_index(dataset):
    #window_length=10
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    delta=close.diff()
    delta=delta[1:]
    up,down=delta.copy(),delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up2 = up.rolling(window=10,center=False).mean()
    roll_down2 = down.abs().rolling(window=10,center=False).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))
    return RSI2
    
def moving_average_convergence_divergence(dataset):
    data=pandas.DataFrame(dataset)
    close=data.iloc[:,4]
    ewma26= close.ewm(span=26,min_periods=26,adjust=True,ignore_na=False).mean()
    ewma12= close.ewm(span=12,min_periods=12,adjust=True,ignore_na=False).mean()
    #print(ewma12)
    macd= (ewma26 - ewma12)
    #print(macd)
    final=[]
    for i in range(9,len(macd)):
        temp=-1*(macd[i-1]+(2/(11))*(macd[i]-macd[i-1]))
        final.append(temp)
    return final
    
def larry_william_R(dataset):
    r=[]
    for i in range(9,len(dataset)):
        data=[j[2] for j in dataset[i-9:i+1]]
        hh=max(data)
        data=[j[3] for j in dataset[i-9:i+1]]
        ll=min(data)
        temp=((hh-dataset[i][4])/(hh-ll))*(-100)
        r.append(temp)
    return r

def accumlation_distributor_oscillator(dataset):
    aco=[]
    for i in range(1,len(dataset)):
        temp=((dataset[i][2]-dataset[i][4])/(dataset[i][2]-dataset[i][3]))*100
        aco.append(temp)
    return aco

def commodity_channel_index(dataset):
    data=pandas.DataFrame(dataset)
    high=data.iloc[:,2]
    low=data.iloc[:,3]
    close=data.iloc[:,4]
    TP = (high + low + close) / 3 
    CCI = pandas.Series((TP - TP.rolling(window=10,center=False).mean()) / (0.015 * TP.rolling(window=10,center=False).std()), name = 'CCI_' + str(10)) 
    return CCI

def normalize(array):
    data=pandas.DataFrame(array)
    data_norm=(data-data.mean())/(data.max()-data.min())
    return data_norm

def classlabel(dataset):
    date=[]
    label=[]
    for i in range(len(dataset)):
        date.append(dataset[i][0])
        diff=dataset[i][4]-dataset[i][1]
        if(diff>0):
            temp="Up"
        elif(diff<0):
            temp="Down"
        else:
            temp="No change"
        label.append(temp)
    date=pandas.DataFrame(date)
    label=pandas.DataFrame(label)
    return date,label
        
        
    
dataset=LoadCsv("nifty.csv")
dataset=str_to_float(dataset)
sma=simple_moving_average(dataset)
ema=weighted_moving_average(dataset)
mom=momentum(dataset)
stck=stochastic_k(dataset)
stcd=stochastic_d(stck)
rsi=relative_strength_index(dataset)
macd=moving_average_convergence_divergence(dataset)
lwr=larry_william_R(dataset)
ado=accumlation_distributor_oscillator(dataset)
cci=commodity_channel_index(dataset)
#print(numpy.max(sma))
#print(numpy.min(sma))
#print(numpy.mean(sma))
#print(numpy.std((sma)))
"""print(sma)
print("-----")
print(ema)
print("-----")
print(mom)
print("-----")
print(stck)
print("-----")
print(stcd)
print("-----")
print(rsi)
print("-----")
print(macd)
print("-----")
print(lwr)
print("-----")
print(ado)
print("-----")
print(cci)
print("-----")
print(len(dataset))"""
sma=sma[len(sma)-len(stcd):]
ema=ema[len(ema)-len(stcd):]
mom=mom[len(mom)-len(stcd):]
stck=stck[len(stck)-len(stcd):]
rsi=rsi[len(rsi)-len(stcd):]
macd=macd[len(macd)-len(stcd):]
lwr=lwr[len(lwr)-len(stcd):]
ado=ado[len(ado)-len(stcd):]
cci=cci[len(cci)-len(stcd):]
cci.index=numpy.arange(0,len(cci))
rsi.index=numpy.arange(0,len(rsi)) 
"""print(sma)
print("-----")
print(ema)
print("-----")
print(mom)
print("-----")"""
#print(len(sma),len(ema),len(mom),len(stck),len(stcd),len(rsi),len(macd),len(lwr),len(ado),len(cci))
sma_norm=pandas.Series(sma)
ema_norm=pandas.Series(ema)
mom_norm=pandas.Series(mom)
stck_norm=pandas.Series(stck)
stcd_norm=pandas.Series(stcd)
rsi_norm=pandas.Series(rsi)
macd_norm=pandas.Series(macd)
lwr_norm=pandas.Series(lwr)
ado_norm=pandas.Series(ado)
cci_norm=pandas.Series(cci)
date,label=classlabel(dataset)
date=date[len(date)-len(stcd):]
date.index=numpy.arange(0,len(date))
label=label[len(label)-len(stcd):]
label.index=numpy.arange(0,len(label))
"""print(sma_norm)
print("-----")
print(ema_norm)
print("-----")
print(mom_norm)
print("-----")"""

final=pandas.concat([date,sma_norm,ema_norm,mom_norm,stck_norm,stcd_norm,rsi_norm,macd_norm,lwr_norm,ado_norm,cci_norm,label],axis=1)
final.to_csv("paramdataset.csv",encoding="UTF-8",index=False,header=False)