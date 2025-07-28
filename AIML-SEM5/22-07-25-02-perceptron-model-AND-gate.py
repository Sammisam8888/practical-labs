wt1,wt2=1,1
wt0=-1.2
x0=1

def ANDgate(x1,x2):
    andgate=x0*wt0+x1*wt1+x2*wt2
    return int(andgate>0)

print("IDEAL AND gate values :")
print("x1 x2 Y = AND(x1,x2)")
print("0  0   0")
print("0  1   0")
print("1  0   0")
print("1  1   1")

print ("AND gate Output from Perceptron Model : ")
print("x1  x2  Y  W1  W2  X0   W0   AND(x1,x2)")
print(f"0   0   0  {wt1}   {wt2}    {x0}  {wt0}   {ANDgate(0,0)}")
print(f"0   1   0  {wt1}   {wt2}    {x0}  {wt0}   {ANDgate(0,1)}")
print(f"1   0   0  {wt1}   {wt2}    {x0}  {wt0}   {ANDgate(1,0)}")
print(f"1   1   1  {wt1}   {wt2}    {x0}  {wt0}   {ANDgate(1,1)}")