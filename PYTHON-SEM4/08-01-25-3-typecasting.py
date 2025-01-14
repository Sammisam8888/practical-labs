#3. Demonstrate type casting.

a=25
b=2.5
c="25"
d=5+6j
print(f"The integer value of {b} is : ",int(b))
print(f"The float value of {a} is : ",float(a))
print(f'''The integer value of "{c}" is : ''',int(c))
print(f"The float value of real part of {d} is : ",float(d.real))
print(f"The float value of imaginary part of {d} is : ",float(d.imag))