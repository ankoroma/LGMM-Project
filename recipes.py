import requests
from py_edamam import Edamam
from py_edamam import PyEdamam
import pandas as pd
import sqlalchemy as sql
import random


random.seed(146)   # for testing purposes only


# Authentication
e = Edamam(
    nutrition_appid="26d80d09",
    nutrition_appkey="33fa304b7f52b8f304123a71ee739bfd",
    recipes_appid="a643e9ab",
    recipes_appkey="0a83d44746617752c2968dd4bb4aa8f0",
    food_appid="dc3a13bb",
    food_appkey="ad3d860e92f5789744ffa1d6579f7c9f",
)

# Search prompt:
print("Welcome to the Lean Green Meal Machine!")
main_ingred = input("Input up to 2 main items you want in your meal: ")

# Take input about calorie count
cal_count = input("Input the maximum number of calories you would like in your meal: ")

# Collection of Recipes
collection = e.search_recipe(main_ingred)

# Dictionary containing items for recipe
final_dict = {
    "Name": [],
    "Health": [],  # Meal Facts
    "Size": [],  # Prep Facts
    "Prep": [],  # Prep Facts
    "Diet": [],  # Meal Facts
    "Ingredients": [],  # Prep Facts
    "Calories": [],  # Nutrition Facts
    "Cuisine": [],  # Meal Facts
    "Meal": [],  # Meal Facts
    "Fat": [],  # Nutrition Facts
    "Carbs": [],  # Nutrition Facts
    "Protein": [],  # Nutrition Facts
    "Sugar": [],  # Nutrition Facts
    "Sodium": [],  # Nutrition Facts
    "Dish": [],  # Meal Facts
    "ID": [],
}


def get_cal(cal_max):
    rec_idx_list = []
    while len(rec_idx_list) < 8:
        max = len(collection["hits"]) - 1
        idx = random.randint(0, max)
        serving = int(collection["hits"][idx]["recipe"]["yield"])
        if serving > 0:

            calories = int((collection["hits"][idx]["recipe"]["calories"]) / serving)
        else:
            serving = 2
            calories = int((collection["hits"][idx]["recipe"]["calories"]) / serving)

        if calories < int(cal_max):
            rec_idx_list.append(idx)

    return set(rec_idx_list)


def get_recipe(item, idx):
    name_var = collection["hits"][idx]["recipe"]["label"]
    health_var = ", ".join(collection["hits"][idx]["recipe"]["healthLabels"])
    size_var = int(collection["hits"][idx]["recipe"]["yield"])
    prep_var = ""
    prep_var += (
        str(int(collection["hits"][idx]["recipe"]["totalTime"] / 60))
        + "hr(s)"
        + " and "
        + str(int(collection["hits"][0]["recipe"]["totalTime"] % 60))
        + "mins"
    )
    diet_var = ", ".join(collection["hits"][idx]["recipe"]["dietLabels"])
    ingred_var = ", ".join(collection["hits"][idx]["recipe"]["ingredientLines"])
    cal_var = int((collection["hits"][idx]["recipe"]["calories"]) / size_var)
    cusine_var = ", ".join(collection["hits"][idx]["recipe"]["cuisineType"])
    meal_var = ", ".join(collection["hits"][idx]["recipe"]["mealType"])
    fat_var = (
        str(
            int(collection["hits"][idx]["recipe"]["totalNutrients"]["FAT"]["quantity"])
            // size_var
        )
        + "g"
    )
    carb_var = (
        str(
            int(
                collection["hits"][idx]["recipe"]["totalNutrients"]["CHOCDF"][
                    "quantity"
                ]
            )
            // size_var
        )
        + "g"
    )
    protein_var = (
        str(
            int(
                collection["hits"][idx]["recipe"]["totalNutrients"]["PROCNT"][
                    "quantity"
                ]
            )
            // size_var
        )
        + "g"
    )
    sugar_var = (
        str(
            int(
                collection["hits"][idx]["recipe"]["totalNutrients"]["SUGAR"]["quantity"]
            )
            // size_var
        )
        + "g"
    )
    sodium_var = (
        str(
            int(collection["hits"][idx]["recipe"]["totalNutrients"]["CA"]["quantity"])
            // size_var
        )
        + "mg"
    )
    dish_var = ", ".join(collection["hits"][idx]["recipe"]["dishType"])

    final_dict["Name"].append(name_var),
    final_dict["Health"].append(health_var),
    final_dict["Size"].append(size_var),
    final_dict["Prep"].append(prep_var),
    final_dict["Diet"].append(diet_var),
    final_dict["Ingredients"].append(ingred_var),
    final_dict["Calories"].append(cal_var),
    final_dict["Cuisine"].append(cusine_var),
    final_dict["Meal"].append(meal_var),
    final_dict["Fat"].append(fat_var),
    final_dict["Carbs"].append(carb_var),
    final_dict["Protein"].append(protein_var),
    final_dict["Sugar"].append(sugar_var),
    final_dict["Sodium"].append(sodium_var),
    final_dict["Dish"].append(dish_var)
    final_dict["ID"].append(idx)


# Runs get_recipe() to create a selection of 5 food items that can go in our recipe table


def create_selection(idx_list, item):
    for i in idx_list:
        get_recipe(item, i)


indices = get_cal(cal_count)
create_selection(indices, main_ingred)


def get_final_dict():  # for testing
    return final_dict


test_dict = get_final_dict()  # testing var

# Create the data frame/table
df = pd.DataFrame.from_dict(final_dict)
engine = sql.create_engine("sqlite:///Lean_Green.db")
df.to_sql("lean_green", con=engine, if_exists="replace", index=False)

# Divide the table into 3 for the different table categories
query_prep_result = engine.execute(
    "SELECT Name,Prep,Size,Ingredients FROM lean_green;"
).fetchall()
query_meal_result = engine.execute(
    "SELECT Name,Meal,Dish,Health,Diet,Cuisine,ID FROM lean_green;"
).fetchall()
query_nutrition_result = engine.execute(
    "SELECT Name,Calories,Fat,Carbs,Protein,Sugar,Sodium FROM lean_green;"
).fetchall()

prep_df = pd.DataFrame(query_prep_result)
meal_df = pd.DataFrame(query_meal_result)
nutrition_df = pd.DataFrame(query_nutrition_result)

prep_df.columns = ["Name", "Prep Time", "Serving Size", "Ingredients"]
meal_df.columns = [
    "Name",
    "Meal Type",
    "Dish Type",
    "Health Label",
    "Diet Label",
    "Cuisine",
    "Meal ID",
]
nutrition_df.columns = [
    "Name",
    "Calories",
    "Fat",
    "Carbs",
    "Protein",
    "Sugar",
    "Sodium",
]

# Print results
print("Meal Information:", "\n", meal_df, "\n\n")
print("Preparation: ", "\n", prep_df, "\n\n")
print("Nutrition Facts:", "\n", nutrition_df)

choice = int(
    input(
        "Enter the Meal ID of the recipe you want to make (located on the far right of the Meal Info table): "
    )
)
recipe_link = collection["hits"][choice]["recipe"]["url"]
print("Here is the link to the full recipe:", "\n", recipe_link)