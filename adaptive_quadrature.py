import math
import composite_integration
# 4.6 2.h where f(x) = cos(x)^2
def f(x):
    return math.cos(x)**2

# define the integral of f to calculate the actual value and then the error
def f_integral(a, b):
    return ((b + 0.5*math.sin(2*b))/2) - ((a + 0.5*math.sin(2*a))/2)

print('4.6 2.h')
# for 4.6 2.h , first need to solve this by composite simpsons rule,
app1 = composite_integration.comp_simpson_rule(0, math.pi/4, f, 2)
print('The approximation of S(a,b) is: ', app1)

# again use composite simpsons rule to calculate the approximation respectively from a to (a+b)/2, and
# (a+b)/2 to b, then sum to get the final approximation
app2 = composite_integration.comp_simpson_rule(0, (math.pi/4)/2, f, 4) + \
    composite_integration.comp_simpson_rule((math.pi/4)/2,math.pi/4, f, 4)
print('The approximation of S(a,(a+b)/2)+S((a+b)/2, b) is: ', app2)

# compare the absolute value of the actual - the second approximation and 10^-3
min( abs(f_integral(0,math.pi/4)-app2), 0.001 )
print('The difference between app2 and the actual value is:', abs(f_integral(0,math.pi/4)-app2), \
      'which is within ',10**-3)