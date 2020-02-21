#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  baking = []

  if len(recipe) != len(ingredients):
    return 0

  for contents in recipe:
    for elements in ingredients:
      if ( contents == elements):
        baking.append(ingredients[elements] // recipe[contents])

  maximum_batches = min(baking)

  return maximum_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 352, 'butter': 198, 'flour': 291 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))