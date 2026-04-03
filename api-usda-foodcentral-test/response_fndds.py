

import requests
import numpy as np
import json
import sqlite3
from pprint import pprint


from CONFIG.config_data_formatting import (
    chosen_attributes, 
    nutrient_attributes, 
    nutrition_template,
)

from DB.functional_queries import (
    get_col_names,
    insert_row,
    delete_row,
)

from CONFIG.config_api_setup import (
    url, 
    fdc_parameters,
    # fdc_id_test,                # fdc id for Cheddar cheese
)

from CONFIG.config_fndds_ids import (
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




def store_fdc_item(fdc_id:int, params:dict, con:sqlite3.Connection):
    '''
    Get, reformat and store USDA fdc FNDDS items locally
    '''
    # query id to avoid ambiguous result
    params['query'] = fdc_id

    row_data = __unpack_single_item_response(params=params)

    table_name = 'food_items'
    col_names = get_col_names(table_name=table_name, con=con)
    insert_row(table_name=table_name, col_names=col_names, row=row_data, con=con)           # NOTE inserts 


def remove_fdc_item(fdc_id:int, con:sqlite3.Connection):
    '''
    To quickly remove items from the database
    '''

    table_name = 'food_items'
    delete_row(table_name=table_name, row_id=fdc_id, con=con)                               # NOTE deletes


def __unpack_single_item_response(params:dict):
    '''
    Establish response and handle potential errors
    '''
    response = requests.get(url=url, params=params)

    if is_error(response=response):
        raise ApiError(response=response, verbose=True)

    data = response.json()

    # assert a single result
    assert len(data['foods']) == 1

    # get first result (should only be one in list)
    food_item = data['foods'][0]

    # reformat information about food item
    item_reformatted = __reformat_data(food_item=food_item)
    
    # add food information to list
    row_data = [item_reformatted[attr] for attr in item_reformatted]
    row_data.append(np.nan)                                                     # add Nan for food_icon (added later on)

    # assert no missing data
    assert len(row_data) == 10

    return row_data

    
def __reformat_data(food_item:list):
    '''
    Adjust, sort and filter out useful data (to facilitate handling later on)
    '''
    item_reformatted = {}

    for attr in chosen_attributes:
        food_info = food_item[attr]

        if attr == 'foodNutrients':
            info_reformatted = __reformat_nutrition(food_nutrients=food_info)
            item_reformatted[attr] = json.dumps(info_reformatted)

        elif attr == 'foodMeasures':
            # info_reformatted = __reformat_measure(food_measures=food_info)                # NOTE decided against
            info_reformatted = food_info
            item_reformatted[attr] = json.dumps(info_reformatted)
        
        else:
            item_reformatted[attr] = json.dumps(food_info)
    
    return item_reformatted


def __reformat_nutrition(food_nutrients):
    '''
    Adjust and filter nutrional information about food
    '''
    nutrition_reformatted = nutrition_template.copy()     ## NOTE ANVÄND DETTA I SCHACKSPELET!!! FÖR BRÄDET OCH GHOST MOVE

    for nutrient in food_nutrients:

        nutrient_name = nutrient['nutrientName']
        for group_name in ['Proximates','Carbohydrates', 'Minerals', 'Vitamins', 'Other Components']:
            
            nutritional_group = nutrition_reformatted[group_name]
            if nutrient_name in nutritional_group:

                insert_data = {
                    'column_name': nutritional_group[nutrient_name],
                    'nutrient_id': nutrient['nutrientId'],
                    'nutrient_name': nutrient['nutrientName'],
                    'value': nutrient['value'],
                    'unit_name': nutrient['unitName'],
                }
                nutritional_group[nutrient_name] = insert_data
        
    return nutrition_reformatted
            

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
    

def get_fdc_ids(food_group:dict) -> list[int]:
    
    stack = [food_group]
    fdc_ids = []

    while stack:
        curr = stack.pop(0)
        for value in curr.values():
            if isinstance(value, int):
                fdc_ids.append(value)
            if isinstance(value, dict):
                stack.append(value)

    return fdc_ids


def __main():
    fdc_ids = get_fdc_ids(food_group=fruits)


    con = sqlite3.connect('DB/food.db')
    for fdc_id in fdc_ids:
        store_fdc_item(fdc_id=fdc_id, params=fdc_parameters, con=con)
        # remove_fdc_item(fdc_id=fdc_id, con=con)
    con.close()


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




