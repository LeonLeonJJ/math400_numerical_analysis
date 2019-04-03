import math
import composite_integration
# 4.8 1.a  where f(x) = x*y^2
def f(x, y):
    return x * y**2

def simpson_double_itg(f, a, b, c, d, m, n):
    h = ((d-c)*(b-a))/9*m*n
    result = 0;

    result += composite_integration.comp_simpson_rule(a, b, f, n)

    result += composite_integration.comp_simpson_rule(c,d,f,m)

    return result

print(simpson_double_itg(f))