import requests
from py_edamam import Edamam
from py_edamam import PyEdamam
import pandas as pd
import sqlalchemy as sql


e = Edamam(nutrition_appid='8fc07160',
           nutrition_appkey='cb8ac8e9448f890761714a683e86e240',
           recipes_appid='056336ac',
           recipes_appkey='8252aff0d13a79fe67887a832eaedb8c',
           food_appid='a25c4690',
           food_appkey='fa57309a6d35fd46058b6984e46b5333')



final_dict = {'Name' : [],
                'Health Labels' : [],
                'Size' : [],
                'Prep Time' : [],
                'Diet Labels' : [], 
                'Ingredients' : [], 
                'Calories' : [], 
                'Cuisine Type' : [], 
                'Meal Type' : [],
                'Fat Quantity' : [], 
                'Carb Quantity' : [], 
                'Protein Quantity' : [], 
                'Sugar Quantity' : [], 
                'Sodium Quantity' : [], 
                'Dish Type' : []
}

def show_options(item, idx):
        collection = e.search_recipe(item)
        name_var = collection['hits'][idx]['recipe']['label']
        health_var = ", ".join(collection['hits'][idx]['recipe']['healthLabels'])
        size_var = int(collection['hits'][idx]['recipe']['yield'])
        prep_var = ""
        prep_var += str(int(collection['hits'][idx]['recipe']['totalTime']/60)) + 'hr(s)' + ' and ' + str(int(collection['hits'][0]['recipe']['totalTime']%60)) + 'mins'
        diet_var = ", ".join(collection['hits'][idx]['recipe']['dietLabels'])
        ingred_var = " ".join(collection['hits'][idx]['recipe']['ingredientLines'])
        cal_var = int(collection['hits'][idx]['recipe']['calories'])
        cusine_var = ", ".join(collection['hits'][idx]['recipe']['cuisineType'])
        meal_var = ", ".join(collection['hits'][idx]['recipe']['mealType'])
        fat_var = int(collection['hits'][idx]['recipe']['totalNutrients']['FAT']['quantity'])
        carb_var = int(collection['hits'][idx]['recipe']['totalNutrients']['CHOCDF']['quantity'])
        protein_var = int(collection['hits'][idx]['recipe']['totalNutrients']['PROCNT']['quantity'])
        sugar_var = int(collection['hits'][idx]['recipe']['totalNutrients']['SUGAR']['quantity'])
        sodium_var = int(collection['hits'][idx]['recipe']['totalNutrients']['CA']['quantity'])
        dish_var = ", ".join(collection['hits'][idx]['recipe']['dishType'])

        final_dict['Name'].append(name_var), 
        final_dict['Health Labels'].append(health_var), 
        final_dict['Size'].append(size_var), 
        final_dict['Prep Time'].append(prep_var), 
        final_dict['Diet Labels'].append(diet_var), 
        final_dict['Ingredients'].append(ingred_var), 
        final_dict['Calories'].append(cal_var), 
        final_dict['Cuisine Type'].append(cusine_var), 
        final_dict['Meal Type'].append(meal_var),
        final_dict['Fat Quantity'].append(fat_var), 
        final_dict['Carb Quantity'].append(carb_var), 
        final_dict['Protein Quantity'].append(protein_var), 
        final_dict['Sugar Quantity'].append(sugar_var), 
        final_dict['Sodium Quantity'].append(sodium_var), 
        final_dict['Dish Type'].append(dish_var)

show_options("beef", 0)
show_options("chicken", 0)

df = pd.DataFrame.from_dict(final_dict)
print("Panda's DF: ", df)
engine = sql.create_engine('sqlite:///Lean_Green.db')
df.to_sql('lean_green', con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM lean_green;").fetchall()
print(query_result)ection['hits'][0]['recipe'])

col_names = ['Name', 'Health Labels', 'Size', 'Prep Time', 'Diet Labels', 
        'Ingredients', 'Calories', 'Cuisine Type', 'Meal Type',
        'Fat Quantity', 'Carb Quantity', 'Protein Quantity', 
        'Sugar Quantity', 'Sodium Quantity', 'Dish Type']