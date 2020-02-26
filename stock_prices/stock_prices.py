#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  maximum_profit = 0
  stock_cost = 0

  for cost in range(len(prices)):
    stock_cost = prices[cost]
    maximum_cost = prices[cost + 1 : ]
    
    for stock in range(len(maximum_cost)):
      profit = maximum_cost[stock] - stock_cost
      
      if (maximum_profit == 0):
        maximum_profit = profit

      if(profit > maximum_profit):
        maximum_profit = profit

  return maximum_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))