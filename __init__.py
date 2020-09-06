from math import log2;from functools import reduce
def ham(x:list,PlaceHolder=0): #size of 2^n-n-1
    new=[PlaceHolder];index=0
    for i in range(1,len(x)+int.bit_length(len(x))+1):
        if log2(i).is_integer():new+=[PlaceHolder]
        else:new+=[x[index]];index+=1
    return new
def encode(x:list):
    for i in range(int.bit_length(len(x))-1):
        if sum([sum(x[2**i+j::2**(i+1)]) for j in range(2**i)])%2==1:x[2**i]=1-x[2**i]
    if sum(x)%2==1:x[0]=1-x[0]
    return x
def decode(x:list):
    index=0
    for i in range(int.bit_length(len(x))-1):
        if sum([sum(x[2**i+j::2**(i+1)]) for j in range(2**i)])%2==1:index+=2**i
    if sum(x)%2==1:x[index]=1-x[index]
    return x
def decode2(x:list):index=reduce(lambda x,y:x^y,[i for i,logic in enumerate(x) if logic]);x[index]=1-x[index];return x #smaller version of decode
def encode2(x:list): #smaller version of encode
    for i in range(int.bit_length(len(x))-1):logic=(sum([sum(x[2**i+j::2**(i+1)]) for j in range(2**i)])%2==1);x[2**i]=(1-x[2**i])*logic+x[2**i]*(1-logic)
    logic=sum(x)%2==1;x[0]=(1-x[0])*logic+x[0]*(1-logic);return x
def ham2(x:list,PlaceHolder=0,new=[0],index=0): #smaller version of ham
    for i in range(1,len(x)+int.bit_length(len(x))+1):logic=log2(i).is_integer();new+=[PlaceHolder*logic+x[index]*(1-logic)];index+=1-logic
    return new
PreHammedList=[1,0,1,0]
print(ham(PreHammedList))
InitialList=ham(PreHammedList)
print(encode(InitialList))
CorruptedList=encode(InitialList)
CorruptedList[4]=1-CorruptedList[4]
print(decode(CorruptedList))
