

import requests
import numpy as np
import pandas as pd
import json
import sqlite3
import os
from pprint import pprint


from config_data_formatting import (
    chosen_item_attributes, 
    nutrient_attributes, 
    nutrient_categories,
    measure_attributes,
)

from functional_queries import (
    get_col_names,
    insert_row,
    insert_multiple_rows,
    delete_row,
)

from config_api_setup import (
    url, 
    fdc_parameters,
    # fdc_id_test,                # fdc id for Cheddar cheese
)

from config_fndds_ids import (
    fruits,
    vegetables,
    dairy_and_eggs,
    meat_and_poultry,
    seafood,
    grains_and_cereals,
    # legumes_and_pulses,
    nuts_and_seeds,
    condiments_spices_and_oils,
    # beverages,
)

class FNDDSObj:
    def __init__(self, con:sqlite3.Connection, params:dict) -> None:
        self.table_item = 'fndds_items'
        self.table_nutrient = 'fndds_nutrients'
        self.table_measure = 'fndds_measures'

        self.con = con
        self.params = params



    def store_fdc_item(self, fdc_id:int, taxonomy:dict):
        '''
        Get, reformat and store USDA fdc FNDDS items locally
        '''
        
        (row_item, rows_nutrient, rows_measure) = self.__unpack_single_item_response(fdc_id=fdc_id, taxonomy=taxonomy)


        columns_item = get_col_names(table_name=self.table_item, con=self.con)
        columns_nutrient = get_col_names(table_name=self.table_nutrient, con=self.con)
        columns_measure = get_col_names(table_name=self.table_measure, con=self.con)

        insert_row(table_name=self.table_item, col_names=columns_item, row=row_item, con=self.con)           # NOTE inserts 
        insert_multiple_rows(table_name=self.table_nutrient, col_names=columns_nutrient, rows=rows_nutrient, con=self.con)
        insert_multiple_rows(table_name=self.table_measure, col_names=columns_measure, rows=rows_measure, con=self.con)


    def remove_fdc_item(self, fdc_id:int):
        '''
        To quickly remove items from the database
        '''
        delete_row(table_name=self.table_item, row_id=fdc_id, con=self.con)                               # NOTE deletes



    def pprint_fdc_item(self, fdc_id:int, taxonomy:dict):
        '''
        Get, reformat and pprint USDA fdc FNDDS items
        '''
        (row_item, rows_nutrient, rows_measure) = self.__unpack_single_item_response(fdc_id=fdc_id, taxonomy=taxonomy)

        pprint(row_item)
        pprint(rows_nutrient)
        pprint(rows_measure)


    def __unpack_single_item_response(self, fdc_id:int, taxonomy:dict):
        '''
        Establish response and handle potential errors
        re: fndds_items, fndds_nutrients, fndds_measures
        '''
        # query id to avoid ambiguous result
        self.params['query'] = fdc_id
        response = requests.get(url=url, params=self.params)
        if is_error(response=response):
            raise ApiError(response=response, verbose=True)

        data = response.json()
        assert len(data['foods']) == 1  # assert a single result

        # get first result (should only be one in list)
        food_data: dict = data['foods'][0]

        # reformat information about food item
        row_item = self.__reformat_base_info(food_data=food_data, taxonomy=taxonomy)
        rows_nutrient = self.__reformat_nutrition_info(food_data=food_data)
        rows_measure = self.__reformat_measure_info(food_data=food_data)

        # assert no missing data
        assert len(row_item) == 10
        for row in rows_nutrient:
            assert len(row) == 8
        for row in rows_measure:
            assert len(row) == 4

        return (row_item, rows_nutrient, rows_measure)




    def __reformat_base_info(self, food_data: dict, taxonomy: dict):
        ''''''
        fndds_item: dict = {k: food_data[k] for k in chosen_item_attributes}
        (category, subcategory, item_name) = list(taxonomy.values())
        
        data_row = list(fndds_item.values())
        # Complement with information not included in fndds response
        data_row.insert(1, item_name)
        data_row.insert(6, category)
        data_row.insert(7, subcategory)

        return data_row


    def __reformat_nutrition_info(self, food_data: dict):
        '''
            food_nutrient_id
            fdc_id
            nutrient_id
            nutrient_name
            nutrient_number
            nutrient_category
            unit_name
            value
        '''
        fdc_id = food_data['fdcId']
        fndds_nutrients: list = food_data['foodNutrients']
        rows_nutrient = []

        for nutrient in fndds_nutrients:            # list of nutrient objects (dicts)
            nutrient: dict
            name = nutrient['nutrientName']
            if name in list(nutrient_categories.keys()):    # all wanted nutrients...
                data_row = [nutrient[k] for k in nutrient_attributes]
                data_row.insert(1, fdc_id)
                data_row.insert(5, nutrient_categories[name]['nutrientCategory'])       # add nutrient category as a new attribute
                rows_nutrient.append(data_row)

        return rows_nutrient

        
    def __reformat_measure_info(self, food_data: dict):
        ''''''
        fdc_id = food_data['fdcId']
        fndds_measures: list = food_data['foodMeasures']
        rows_measure = []
        
        for measure in fndds_measures:
            measure: dict
            data_row = [measure[k] for k in measure_attributes]
            data_row.insert(1, fdc_id)
            rows_measure.append(data_row)
        
        return rows_measure



def is_error(response) -> None:
    if response.status_code != 200:
        return True


class ApiError(Exception):
    def __init__(self, response:dict, verbose=False) -> None:
        self.errorCode = response.json()['error']['code']
        self.errorStatusCode = response.status_code
        self.errorMessage = response.json()['error']['message']

        message = self.message() if not verbose else self.verboseMessage()

        super().__init__(message)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def message(self):
        return f'{self.errorCode} [{self.errorStatusCode}]'
    
    def verboseMessage(self):
        return f'{self.errorCode} [{self.errorStatusCode}] : {self.errorMessage}'
    







def __main():
    con = sqlite3.connect(os.path.dirname(__file__)+'/food.db')
    fndds_obj = FNDDSObj(con=con, params=fdc_parameters)

    # df_fruits = pd.DataFrame.from_dict(data=fruits, orient='index')
    # print(df_fruits)
    
    for (fdc_id, taxonomy) in fruits.items():       # taxonomy refers to the science of naming, describing and classifying
        # fndds_obj.pprint_fdc_item(fdc_id=fdc_id, taxonomy=taxonomy)
        fndds_obj.store_fdc_item(fdc_id=fdc_id, taxonomy=taxonomy)
        # fndds_obj.remove_fdc_item(fdc_id=fdc_id)
    quit()

   
    



if __name__=='__main__':
    __main()

















# {'code': 'API_KEY_INVALID', 'message': 'An invalid api_key was supplied. Get one at https://api.nal.usda.gov:443'}

'''
Error Code	            HTTP Status Code	Description
API_KEY_MISSING 	    403	                An API key was not supplied. See API key usage for details on how to pass your API key to the API.
API_KEY_INVALID 	    403	                An invalid API key was supplied. Double check that the API key being passed in is valid, or signup for an API key.
API_KEY_DISABLED    	403	                The API key supplied has been disabled by an administrator. Please contact us for assistance.
API_KEY_UNAUTHORIZED    403	                The API key supplied is not authorized to access the given service. Please contact us for assistance.
API_KEY_UNVERIFIED  	403	                The API key supplied has not been verified yet. Please check your e-mail to verify the API key. Please contact us for assistance.
HTTPS_REQUIRED  	    400	                Requests to this API must be made over HTTPS. Ensure that the URL being used is over HTTPS.
OVER_RATE_LIMIT 	    429	                The API key has exceeded the rate limits. See rate limits for more details or contact us for assistance.
NOT_FOUND   	        404	                An API could not be found at the given URL. Check your URL.
'''



FdcApiErrorCodes = {
    'API_KEY_MISSING':      {'httpStatusCode': 403, 'description': 'An API key was not supplied. See API key usage for details on how to pass your API key to the API.'},
    'API_KEY_INVALID':      {'httpStatusCode': 403, 'description': 'An invalid API key was supplied. Double check that the API key being passed in is valid, or signup for an API key.'},
    'API_KEY_DISABLED':     {'httpStatusCode': 403, 'description': 'The API key supplied has been disabled by an administrator. Please contact us for assistance.'},
    'API_KEY_UNAUTHORIZED': {'httpStatusCode': 403, 'description': 'The API key supplied is not authorized to access the given service. Please contact us for assistance.'},
    'API_KEY_UNVERIFIED':   {'httpStatusCode': 403, 'description': 'The API key supplied has not been verified yet. Please check your e-mail to verify the API key. Please contact us for assistance.'},
    'HTTPS_REQUIRED':       {'httpStatusCode': 400, 'description': 'Requests to this API must be made over HTTPS. Ensure that the URL being used is over HTTPS.'},
    'OVER_RATE_LIMIT':      {'httpStatusCode': 429, 'description': 'The API key has exceeded the rate limits. See rate limits for more details or contact us for assistance.'},
    'NOT_FOUND':            {'httpStatusCode': 404, 'description': 'An API could not be found at the given URL. Check your URL.'},
}


## deprecated XXX

# class FdcApiRequest:
#     def __init__(self, api_key) -> None:
#         self.__url = 
#         self.__api_key = api_key

#         self.__query = None

#         self.__params = {
#             'api_key': self.__api_key,
#             'query': self.__query,
#         }

#     def getApiKey(self):
#         # getter function, api key should be immutable
#         return self.__api_key
    
#     def setQuery(self, query):
#         # setter function, should be fdc_id or keyword e.g. 'apple, raw'
#         self.__query = query

#     def requestFdc(self):
#         # 
#         response = requests.get(url=self.__url, params=self.__params)

#         # handling API error 
#         if response.status_code != 200:
#             raise ApiError(response, verbose=True)




    # def __reformat_data(self, food_item:list):
    #     '''
    #     Adjust, sort and filter out useful data (to facilitate handling later on)
    #     '''
    #     item_reformatted = {}

    #     for attr in chosen_base_attributes:
    #         food_info = food_item[attr]

    #         if attr == 'foodNutrients':
    #             info_reformatted = self.__reformat_nutrition(nutrient_items=food_info)
    #             item_reformatted[attr] = json.dumps(info_reformatted)

    #         elif attr == 'foodMeasures':
    #             # info_reformatted = __reformat_measure(food_measures=food_info)                # NOTE decided against
    #             info_reformatted = food_info
    #             item_reformatted[attr] = json.dumps(info_reformatted)
            
    #         else:
    #             item_reformatted[attr] = food_info
        
    #     return item_reformatted



    # def __reformat_nutrition(self, nutrient_items):
    #     '''
    #     Adjust and filter nutrional information about food

    #     nutrient categories: ['Proximates','Carbohydrates', 'Minerals', 'Vitamins', 'Other Components']

    #     {
    #         'foodNutrientId': 28794413,
    #         'indentLevel': 1,
    #         'nutrientCategory': 'Other Component',      # NOTE added!
    #         'nutrientId': 1293,
    #         'nutrientName': 'Fatty acids, total polyunsaturated',
    #         'nutrientNumber': '646',
    #         'rank': 12900,
    #         'unitName': 'G',
    #         'value': 0.025
    #     }
    #     '''
    #     nutrient_selections = []
 
    #     for item in nutrient_items:            # list of nutrient objects (dicts)
    #         name = item['nutrientName']

    #         if name in list(nutrient_categories.keys()):    # all nutrients...
    #             item['nutrientCategory'] = nutrient_categories[name]['nutrientCategory']        # add nutrient category as a new attribute
    #             nutrient_selections.append(item)            # add to selected

    #     return nutrient_selections
                

# def __reformat_measure(food_measures):
#     '''
#     Adjust and filter information about food measures
#     '''
#     measures_reformatted = []

#     for measure in food_measures:

#         insert_data = {
#             'measureUnitAbbreviation': measure['measureUnitAbbreviation'],
#             'gramWeight': measure['gramWeight'],
#         }
#         dissemmination_text = measure['disseminationText']
#         measures_reformatted[dissemmination_text] = insert_data
    
#     return measures_reformatted
