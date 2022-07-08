import unittest
from recipes import *
random.seed(146) # for testing purposes

class Recipes_Tester(unittest.TestCase):

    def test_a_get_cal(self): # works fine
        print('\n\nTesting get_cal acceptable calories')
        observed = indices
        expected = get_cal(cal_count)
        self.assertEqual(observed, expected)

    def test_b_get_recipe(self): # works fine
        print('\nTesting get_recipe verify dictionary')
        observed = test_dict
        expected = get_final_dict()
        self.assertEqual(observed, expected)

    def test_c_dataframe(self): # works fine
        print('\nVerifying dictionary was converted to a DataFrame')
        observed = "<class 'pandas.core.frame.DataFrame'>"
        expected = str(type(df))
        self.assertEqual(observed, expected)

    def test_d_sql_engine(self): # works fine
        print('\nVerifying SQL engine was created')
        observed = "<class 'sqlalchemy.engine.base.Engine'>"
        expected = str(type(engine))
        self.assertEqual(observed, expected)

    def test_e_query_prep_result(self): # works fine
        print('\nTesting the accuracy of the prep query')
        observed = query_prep_result
        expected = engine.execute("SELECT Name,Prep,Size,Ingredients FROM lean_green;").fetchall()
        self.assertEqual(observed, expected)
    
    def test_f_query_meal_result(self): # works fine
        print('\nTesting the accuracy of the meal query')
        observed = query_meal_result
        expected = engine.execute("SELECT Name,Meal,Dish,Health,Diet,Cuisine,ID FROM lean_green;").fetchall()
        self.assertEqual(observed, expected)

    def test_g_query_nutrition_result(self): # works fine
        print('\nTesting the accuracy of the nutrition query')
        observed = query_nutrition_result
        expected = engine.execute("SELECT Name,Calories,Fat,Carbs,Protein,Sugar,Sodium FROM lean_green;").fetchall()
        self.assertEqual(observed, expected)

    def test_h_recipe_link(self): # works fine
        print('\nTesting recipe link')
        observed = recipe_link
        expected = collection["hits"][choice]["recipe"]["url"]
        self.assertEqual(observed, expected)


if __name__ == '__main__':
    unittest.main()




