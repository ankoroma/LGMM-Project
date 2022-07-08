import unittest
from recipes import *
random.seed(146)

class Recipes_Tester(unittest.TestCase):

    def test_get_cal(self): # works fine
        print('\nTesting get_cal acceptable calories')
        observed = indices
        expected = get_cal(cal_count)
        self.assertEqual(observed, expected)

    def test_get_recipe(self): # works fine
        print('\nTesting get_recipe verify dictionary')
        observed = test_dict
        expected = get_final_dict()
        self.assertEqual(observed, expected)

    '''
    def test_dataframe(self):
        print('\nTesting dataframe type')
        observed = '<class 'pandas.core.frame.DataFrame'>'
        expected = type(df)
        self.assertEqual(observed, expected)
    '''

    def test_sql_engine(self):
        pass

    def test_query_prep_result(self):
        pass
    
    def test_query_meal_result(self):
        pass

    def test_query_nutrition_result(self):
        pass



if __name__ == '__main__':
    unittest.main()




