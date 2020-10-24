# Simple fibonacci function

def fibonacci(max_value):
  """ Prints Fibonacci numbers until max value """
  a, b = 0, 1
  while a < max_value:
    print(a, end = " ")
    a, b = b, a + b

fibonacci(100)

# You can find more details here: 
# en.wikipedia.org/wiki/Fibonacci_number
