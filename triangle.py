'''Is this a triangle?

Implement a method that accepts 3 integer values a, b, c.
The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).'''

'''The triangle inequality theorem states that the sum of the lengths of any two sides 
of a triangle must be greater than the length of the third side'''

def is_triangle(a, b, c):
   if a + b > c and b + c > a and c + a > b :
    return True
   else :
    return False
