#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    move_select = ['rock', 'paper', 'scissors']
    hands = []

    def rps_fun(num, list=[]):
        if num == 0:
            return hands.append(list)
        else:
            for i in range(len(move_select)):
                rps_fun(num - 1, list + [move_select[i]])

        return [hands]
        
    rps_fun(n)

    return hands
  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')