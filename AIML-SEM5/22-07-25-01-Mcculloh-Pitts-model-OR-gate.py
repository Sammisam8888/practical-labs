wt1,wt2=1,1
wt0=-0.4
x0=1

def ORgate(x1,x2):
    orgate=x0*wt0+x1*wt1+x2*wt2
    return int(orgate>0)

print("IDEAL OR gate values :")
print("x1 x2 Y=OR(x1,x2)")
print("0  0   0")
print("0  1   1")
print("1  0   1")
print("1  1   1")

print ("OR gate Output from Mcculloh Pitts Model : ")
print("x1  x2  Y  W1  W2  X0   W0   OR(x1,x2)")
print(f"0   0   0  {wt1}   {wt2}    {x0}  {wt0}   {ORgate(0,0)}")
print(f"0   1   1  {wt1}   {wt2}    {x0}  {wt0}   {ORgate(0,1)}")
print(f"1   0   1  {wt1}   {wt2}    {x0}  {wt0}   {ORgate(1,0)}")
print(f"1   1   1  {wt1}   {wt2}    {x0}  {wt0}   {ORgate(1,1)}")
