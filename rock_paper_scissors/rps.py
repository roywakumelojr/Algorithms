#!/usr/bin/python

import sys
game_choices = [['rock'], ['paper'], ['scissors']]
def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  if n == 1:
    return game_choices
  
  result = []

  first_play = rock_paper_scissors( n - 1 )

  for new_game_choices in first_play:
    for move in game_choices:
      new_move = new_game_choices + move
      result.append(new_move)
  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')