cache = {}
def _fib(n):
  if n not in cache:
    cache[n] = fib(n)
  return cache[n]

def fib(n):
  if n < 2:
    return n
  return _fib(n-1) + _fib(n-2)
