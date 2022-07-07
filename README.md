# Lean Green Meal Machine
## Installations & Imports
### Edamam Site:
For this program, you will need to create an accounts on https://www.edamam.com/, the website for the API. Once you have created an account, you must make three applications:
* Nutrition API Analysis
* Recipe Search API
* Food Databse API

Each app comes with an app_id and an app_key. After you have created the applications and saved these access tokens, you can begin programming.

### Terminal and Code
To begin you must first install the Edamam API:
```python
pip install py_edamam
```

Afterwards, you must import the following libraries
```python
import requests # Parse through libraries
from py_edamam import Edamam  # Access to Edamam API
from py_edamam import PyEdamam # Access to Edamam API
import pandas as pd # Create a dataframe
import sqlalchemy as sql # Create a database
import random # Obtain random integers
```

## Environment Functions and Important Variables

### Important Variables
* `e` – Edamam object that lets you use Edamam object functions 
* `main_ingred` – user input for up to 2 ingredients the user wants in recipe 
* `cal_count` – user input maximum amount of calories user wants in recipe
* `collection` – list of recipes that contains the main ingredients user wants
* `final_dict` – dictionary containing recipes that match user's desire
* `indices` – list of indices of recipes within `collection` that adhere to the user's max calorie request 
* `df` – pandas dataframe of all the recipes within `final_dict`
* `choice` – user input for the recipe they wish to make
* `recipe_link` – link containing recipe user wants to make

### Functions
* `Edamam()` – takes in all of the access tokens from your Edamam applications as parameters and returns an object in the Edamam Database
* `.search()` – takes in `main_ingred` as a parameter and returns a dictionary of recipes with names containing the term from the Edamam Database
* `get_cal()` – takes in `cal_count` and returns list of indices of recipes within `collection` that adhere to the user's max calorie request 
* `get_recipe()` – takes in `main_ingred` and an index, uses `collection` to get key information about the recipe at the given index, then adds this information to the `final_dict` dictionary
* `create_selection()` – takes in the `indices` list and `main_ingred` and then runs `get_recipe()` for each value in `indices`

## How recipes.py Works
`recipes.py` is where the Lean Green Meal Machine lives. Upon running it, the user will receive 2 prompts requesting input:
```python
main_ingred = input("Welcome to the Lean Green Meal Machine! Input up to two main ingredients that you want in your meal: ")
cal_count = input("Input the maximum number of calories you would like in your meal: ")
```
After receiving the user's input, the Lean Green Meal Machine begins searching for meals that match the user's needs. When it finds these meals, it prints out the following tables with details for each option:

##### Meal information
|  | Name | Meal Type | Dish Type | Health Label | Diet Label | Cuisine | Meal ID
|-| ---- | --------- | --------- | ------------ | ---------- | ------- | -------
|0| Chicken Paprikash | lunch/dinner | main course | "Egg-Free"... | Low-Carb | Central Europe | 1

##### Preparation
|  | Name | Prep Time | Serving Size | Ingredients |
|-| ---- | --------- | --------- | ------------ | 
|0| Chicken Paprikash |  0hr(s) and 0mins | 4 | 640 grams chicken - drumsticks and thighs ( 3 ...
##### Nutrition Facts
|  | Name | Calories | Fat | Carbs | Protein | Sugar | Sodium
|-| ---- | --------- | --------- | ------------ | ---------- | ------- | -------
|0| Chicken Paprikash | 758 | 52g | 11g | 59g | 4g | 81mg

The user can use these tables to see which recipe they want to make. Once the user has done so, they will respond to the prompt:
```python
choice = int(input("Enter the Meal ID of the recipe you want to make (located on the far right of the Meal Info table): "))
```
After they have responded, the user will receive a link to the recipe they have chosen for a full guide to the recipe they chose.
```
http://norecipes.com/recipe/chicken-paprikash/
```