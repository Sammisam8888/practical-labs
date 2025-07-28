wt1, wt2 = -0.5, -0.5
wt0 = -0.4
x0 = 1
lr = 0.1
target = [0, 0, 0, 1]
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

def step(n):
    return 1 if n > 0 else 0

def ANDgate(epoch=0):
    global wt0, wt1, wt2
    total_error = 0
    print(f"Epoch {epoch + 1}")
    
    for i, (x1, x2) in enumerate(inputs):
        net = x0 * wt0 + x1 * wt1 + x2 * wt2
        out = step(net)
        error = target[i] - out
        total_error += abs(error)

        wt1 += lr * error * x1
        wt2 += lr * error * x2
        wt0 += lr * error * x0

        print(f"{x1}  {x2}     {target[i]}       {out}      {error}    {round(wt1,2)}    {round(wt2,2)}    {round(wt0,2)}")

    if total_error != 0:
        ANDgate(epoch + 1)

print("Training Perceptron for AND Gate")
print("x1 x2  target   out   error  wt1    wt2    wt0")
ANDgate()

print("Final weights:")
print(f"wt1 = {round(wt1,2)}, wt2 = {round(wt2,2)}, wt0 = {round(wt0,2)}")

print("AND gate outputs from perceptron model:")
for x1, x2 in inputs:
    net = x0 * wt0 + x1 * wt1 + x2 * wt2
    out = step(net)
    print(f"{x1} AND {x2} = {out}")