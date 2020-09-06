def encode(x:list):
    for i in range(int.bit_length(len(x))-1):
        z=[]
        for j in range(2**i):z+=x[2**i+j::2**(i+1)]
        if sum(z)%2==1:x[2**i]=1-x[2**i]
    if sum(x)%2==1:x[0]=1-x[0]
    return x
def decode(x:list):
    index=0
    for i in range(int.bit_length(len(x))-1):
        z=[]
        for j in range(2**i):z+=x[2**i+j::2**(i+1)]
        if sum(z)%2==1:index+=2**i
    if sum(x)%2==1:x[index]=1-x[index]
    return x
InitialList=[1,1,1,1,1,0,1,0]
print(encode(InitialList))
CorruptedList=encode(InitialList)
CorruptedList[4]=1-CorruptedList[4]
print(decode(CorruptedList))
