from math import log2
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
PreHammedList=[1,0,1,0]
print(ham(PreHammedList))
InitialList=ham(PreHammedList)
print(encode(InitialList))
CorruptedList=encode(InitialList)
CorruptedList[4]=1-CorruptedList[4]
print(decode(CorruptedList))
