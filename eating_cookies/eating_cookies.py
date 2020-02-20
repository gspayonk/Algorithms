#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  possibilities = [1,1,2]
  combinations = 0
  if n < 3: combinations = possibilities[n]
  else:
    for _ in range(3, n):
      possibilities.insert(3, possibilities[0] + possibilities[1] + possibilities[2])
      possibilities.pop(0)
    for n in possibilities:
      combinations += n
  return combinations

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')