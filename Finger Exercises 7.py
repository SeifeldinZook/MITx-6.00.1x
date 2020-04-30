def maxOfThree(a, b, c):
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger


def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)






def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers
try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')