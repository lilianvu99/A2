"""Write a Python module newtonraphson.py that contains
functions to find the roots of an equation for a polynomial in x using the
Newton-Raphson method. Your solution should have the following
signature:
def NewtonRaphson(fpoly, a, tolerance = .00001):
 Given a set of polynomial coefficients fpoly
 for a univariate polynomial function,
 e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
 find the real roots of the polynomial (if any)
 using the Newton-Raphson method.
 a is the initial estimate of the root and
 starting state of the search
 This is an iterative method that stops when the
 change in estimators is less than tolerance.

 coefficients should be an iterable (tuple or list) of coefficients for the
powers of x. As an example:
7𝑥𝑥4 + 3𝑥𝑥3 − 5𝑥𝑥2 + 32𝑥𝑥 − 7𝑥𝑥0 = 0
would be represented as [7, 3, −5, 32, −7]. Suggested examples for
trying:
NewtonRaphson( [7, 3, -5, 32, -7], 5) and
NewtonRaphson( [7, 3, -5, 32, -7], -50)
Note that only real roots will be returned when we start the search with a
real value. You may not use any library functions for taking
derivatives or evaluating polynomials. Write auxiliary functions (also in
newtonraphson.py):
def polyval(fpoly, x):
 polyval(fpoly, x)
 Given a set of polynomial coefficients from highest order to x^0,
 compute the value of the polynomial at x. We assume zero
 coefficients are present in the coefficient list/tuple.
 Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
 polyval([4, 0, 9, 3], 5))
 returns 548

def derivative(fpoly):
 derivative(fpoly)
 Given a set of polynomial coefficients from highest order to x^0,
 compute the derivative polynomial. We assume zero coefficients
 are present in the coefficient list/tuple.
 Returns polynomial coefficients for the derivative polynomial.
 Example:
 derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0
 returns: [6, 4] # 6 * x**1 + 4 * x**0

"""
import array

#fpoly = set of polynomial coefficients
"""algorithm:
    1. compute values of function and derivative for given function
    2. compute h: h = function / derivative
    3. while h is greater than allowed error e
        1. h = function / derivative
        2. x = x - h 
        """

def polyval(fpoly, x):
    outputFunct = 0
    count = len(fpoly) - 1
    for i in range(0, len(fpoly)):
        outputFunct = outputFunct + (fpoly[i] * (x**count))
        count = count - 1
        if count == -1:
            break
    return outputFunct

def derivative(fpoly): #takes tuple fpoly and takes the derivative and returns the value
    count = len(fpoly) - 1
    outputDeriv = []
    for i in range(0, len(fpoly)):
        outputDeriv.append(fpoly[i] * count)
        count = count - 1
        if count == 0:
            break
    return outputDeriv


def NewtonRaphson(fpoly, a, tolerance=0.00001):
    oldA = a
    newA = oldA - (polyval(fpoly, oldA) / polyval(derivative(fpoly), oldA))

    while abs(newA - oldA) > tolerance:
        oldA = newA
        newA = oldA - (polyval(fpoly, oldA) / polyval(derivative(fpoly), oldA))
    print("This is the root: ", newA)
    return newA

NewtonRaphson([4, 0, 9, 3], 5)