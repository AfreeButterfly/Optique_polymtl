import sympy
import numpy
from sympy import Matrix

#Variables
pinhole=1
f=1
distance_lentilles=1
distance_planfocal=1




M1=Matrix([[1,distance_planfocal],
           [0,1]])

M2=Matrix([[1,0],
           [f,1]])

M3=Matrix([[1,distance_lentilles],
           [0,1]])

x=M3.inv()



