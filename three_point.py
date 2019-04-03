import math
# construct the end point formula for easier access
def end_point_formula(f, x, h):
    return 1/(2*h) * (-3*f(x) + 4*f(x+h) - f(x+2*h))

# construct the mid point formula for easier access
def mid_point_formula(f, x, h):
    return 1/(2*h) * (f(x+h) - f(x-h))

def three_pt_eval(f, x):
    answers = []
    errors = []
    error_bound = []
    # define h as a positive value for now, will evaluate both + and - and choose a more accurate value
    h = abs(x[0] - x[1])
    # the actual value of f(x)

    for i in x:
        # compare either the end point or mid point result is smaller, then store into the answer list
        if(abs(f_6a_derivative(i) - end_point_formula(f, i, h)) < abs(f_6a_derivative(i) - mid_point_formula(f, i, h))):
            answers.append(end_point_formula(f, i, h)) # answers
            errors.append(f_6a_derivative(i) - end_point_formula(f, i, h)) # error
        else:
            answers.append(mid_point_formula(f, i, h))
            errors.append(f_6a_derivative(i) - mid_point_formula(f, i, h))
        if(i is not 0):
            error_bound.append(abs(h / (2 * (i ** 2))))  # error bound
        else:
            error_bound.append(0)

    for i, aswr, err, e_bound in zip(x, answers, errors, error_bound):
        print("f'(",i,") = " ,aswr, 'and the error is ', err, 'while the error bound is', e_bound)

# question 6a where f(x) = e^2x - cos(2x)
def f_6a(x):
    return math.e**(2*x) - math.cos(2*x)
# manually define the derivative function of f, only for getting the actual value and fine error
def f_6a_derivative(x):
    return math.e**x + x*math.e**x
x_6a = [-0.3, -0.2, -0.1, 0]
print('4.2 #6.a')
three_pt_eval(f_6a,x_6a)