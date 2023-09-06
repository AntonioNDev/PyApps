#test1
from functools import cache, wraps, lru_cache
import sys

def memoize(func):
   cache = {}

   @wraps(func)
   def wrapper(*args, **kwargs):
      key = str(args) + str(kwargs)

      if key not in cache:
         cache[key] = func(*args, **kwargs)

      return cache[key]
   return wrapper

@cache
def fibonacci(n) -> int:
   if n < 2:
      return n
   return fibonacci(n-1) + fibonacci(n-2)



if __name__ == '__main__':
   sys.setrecursionlimit(10000)

   f = fibonacci(100)
   print(f)
