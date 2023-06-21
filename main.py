from sympy import *
from math import *
import cmath
import matplotlib.pyplot as plt
import numpy as np

def z_function(coeff_list, func_type, time_shift):
    z = Symbol('z')
    shift = lambda x: z**(x);
    power_step = lambda a: (z/(z-a));
    cosine = lambda omega, a: ((z**2)-(z*a*cos(omega)))/((z**2)-(2*a*z*cos(omega))+(a**2))
    sine = lambda omega, a: ((z**2)-(z*a*sin(omega)))/((z**2)-(2*a*z*cos(omega))+(a**2))

    terms = []
    k = 0
    for i in func_type:
        if i == 'delta':
            if time_shift[k] == 0:
                terms.append(coeff_list[k])
            else:
                terms.append(coeff_list[k]*shift(time_shift[k]))
        elif i == '(a^n)u[n]':
            a = float(input('What is the coefficient value raised to a power n?\n'))
            if time_shift[k] != 0:
                terms.append(coeff_list[k]*power_step(a))
            else:
                terms.append(coeff_list[k]*power_step(a)*shift(time_shift[k]))
        elif i == 'u[n]':
            if time_shift[k] == 0:
                terms.append((coeff_list[k]*z)/(z-1))
            else:
                terms.append(((coeff_list[k] * z) / (z - 1))*shift(time_shift[k]))
        elif i == '(a^2)sin(omega*n)u[n]':
            omega = round(eval(input('What is the discrete angular frequency? \n'),{'pi':pi}),6)
            a = float(eval(input('What is the coefficient value "a" raised to a power n?\n')))
            if time_shift[k] == 0:
                terms.append(coeff_list[k] * sine(omega, a))
            else:
                terms.append(coeff_list[k] * sine(omega, a)*shift(time_shift[k]))
        elif i == '(a^2)cos(omega*n)u[n]':
            omega = round(eval(input('What is the discrete angular frequency? \n'),{'pi':pi}),6)
            a = float(eval(input('What is the coefficient value "a" raised to a power n?\n')))
            if time_shift[k] == 0:
                terms.append(coeff_list[k] * cosine(omega, a))
            else:
                terms.append(coeff_list[k] * cosine(omega, a)*shift(time_shift[k]))
        k += 1
    return sum_terms(terms)

def sum_terms(terms):
    i = 0
    H_z = 0
    while i < len(terms):
        H_z += terms[i]
        i+=1
    return simplify(H_z)

def file_input(input_file):
    file_open = open(input_file)
    param = file_open.read()
    print('H_z = ', z_function(param[0], param[1], param[2]))

def main():
    user_input = ''
    while user_input != '3':
        menu()
        user_input = input('Enter a choice')
        if user_input == '1':
            file = input('Enter the file name (please ensure they are in the same directory as main.py)')
            file_input(file)
        elif user_input == '2':
            prompt_1 = input('Enter the coefficients of each term (separate each value with a space bar)').split()
            prompt_2 = input('Enter the type of function of each term (separate each value with a space bar)').split()
            prompt_3 = input('Enter the time shift of each term (separate each value with a space bar)').split()
            print('H_z = ', z_function(prompt_1, prompt_2, prompt_3))
        else:
            print('Invalid entry, please try again')
def menu():
    print('1. File input\n', '2. Manual input\n', '3. Exit\n')

if __name__ == '__main__':
    main()



