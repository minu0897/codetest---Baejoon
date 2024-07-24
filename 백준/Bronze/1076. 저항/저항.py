import sys
lis = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

in1 = input()
in2 = input()
in3 = input()

print( ( lis.index(in1)*10 +  lis.index(in2) ) * (10**lis.index(in3) ))