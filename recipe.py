# -*- coding: utf-8 -*-
import sys

recipe_file = sys.argv[1]
file_object = open(recipe_file,"r")

for recipe_data in file_object:
    print (recipe_data),
