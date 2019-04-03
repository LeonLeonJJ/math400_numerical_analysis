import math

# f(x) = cos^2(x)
def f(x):
    #return 2 + math.sin(2*math.sqrt(x))
    return math.cos(x)**2

# trapezoidal
def comp_trapezoidal_rule(a, b, f, n):
    h = (b-a)/n
    result = (h/2) * (f(a) + f(b))
    # j begins at 1
    for j in range(n-1):
        result += (2*h/2)*(f(a+(j+1)*h)) #j+1 because j start at 1
    return result
# 4.4  2.a f(x) = cos^2(x)
print('4.4 2.a\nComposite Trapezoidal rule:', comp_trapezoidal_rule(-0.5, 0.5, f, 4),'\n')


# simpson
def comp_simpson_rule(a, b, f, n):
    h = (b - a) / n
    result = (h/3) * (f(a) + f(b))
    for j in range(int(n/2-1)):
        result += (2*h/3) * (f(a+2*(j+1)*h)) #j+1 because j start at 1
    for j in range(int(n/2)):
        result += (4*h/3) * (f(a+(2*(j+1)-1)*h)) #j+1 because j start at 1
    return result

print("4.4 4.a\nComposite Simpson's rule:", comp_simpson_rule(-0.5, 0.5, f, 4),'\n')

# midpoint
def comp_midpoint_rule(a,b,f,n):
    h = (b-a)/n
    result=0
    for j in range(n):
        result += h * f(a + (j+1-0.5)*h)
    return result

print("4.4 6.a\nComposite Midpoint rule:", comp_midpoint_rule(-0.5, 0.5, f, 4),'\n')

