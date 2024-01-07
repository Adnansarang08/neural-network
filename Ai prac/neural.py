#simple neural network
x = float(input("Enter the value of x: "))
w = float(input("Enter the value of w: "))
b = float(input("Enter the value of b: "))
net = int(w*x+b)
if(net<0):
    out = 0
elif((net>=0) & (net<=1)):
    out = net
else:
    out = 1
    print("net = ",net)
    print("output = ",out)
    
    
# number of the elements as input
n = int(input("Enter the number of elements: "))
print("Enter the inputs")
inputs = []
for i in range(0,n):
    ele=float(input())
    inputs.append(ele)
    print(inputs)
    
print("Enter the weights")
weights = []
for i in range(0,n):
    ele=float(input())
    weights.append(ele)
    print(weights)
    
    
print("The net input can be calculated as Yin =x1w1 + x2w2 +x3w3")
#In[5]
Yin = []
for i in range(0,n):
    Yin.append(inputs[i]*weights[i])
    print(round(sum(Yin),3))  