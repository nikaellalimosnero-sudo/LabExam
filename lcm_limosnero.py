#lcm_limosnero

def gcd(a, b):
  if b == 0:
    return a
  else:
      return gcd(b,a % b)

def lcm(x, y):
    return (x * y) // gcd( x, y)

# Main program
while True:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter value for y: "))
    print(f"The LCM of {x} and {y} is = {lcm(x, y)}")
else:
    print("Please enter positve non-zero integers ")




