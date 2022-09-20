

from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator
from task3 import show
from math import sqrt
from math import factorial
from task4 import decorator_4

lambda_f1 = decorator_1(lambda x:print(x))

lambda_f2 = decorator_1(lambda x:print(x,"2"))

@decorator_2
def quad_eq_sol(a,b,c):
    '''this function solves quadretic equations'''
    delta = b**2 - 4*a*c
    if delta<0:
        print("no solution")
    elif delta>=0:
        return (-b-sqrt(delta)/(2*a)), (-b+sqrt(delta)/(2*a))



@decorator
def print_lablas_tri(n):
    '''I print lablas triangle'''
    for i in range(n):
        for j in range(n-i+1):    
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
        print()

@decorator_4
def buggy_function():
    print(a)

lambda_f1(2)
lambda_f1(3)
lambda_f2(2)
lambda_f2(3)
quad_eq_sol(1,1,1)
quad_eq_sol(1,2,1)
show()
print_lablas_tri(5)
buggy_function()
