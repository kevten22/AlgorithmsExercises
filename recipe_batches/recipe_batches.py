#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = ingredients[(list(recipe.keys())[0])] // recipe[(list(recipe.keys())[0])]
  for i in recipe.keys():
    if i not in ingredients:
      return 0
    elif ingredients[i] // recipe[i] < batches:
      batches = ingredients[i] // recipe[i]

  return batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))