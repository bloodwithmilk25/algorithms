cache = {}
def fib(n):
  if n not in cache:
    cache[n] = _fib(n)
  return cache[n]

def _fib(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)