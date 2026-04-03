
import requests
from pprint import pprint

from CONFIG.config_api_setup import (
    url, 
    fdc_parameters
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

from response_fndds import (
    store_fdc_item,
)

for group_name in fruits:
    group = fruits[group_name]
    for fruit_name in group:
        fndds_id = group[fruit_name]
        print(fruit_name, fndds_id)

        fdc_id = fndds_id

        fdc_parameters['query'] = fdc_id
        # fdc_parameters['dataType'] = 'SR Legacy'

        response = requests.get(url=url, params=fdc_parameters)

        if response.status_code == 200:
            data = response.json()
            food_item = data['foods'][0]
            # for attr in food_item:
            #     print(attr)

            food_description = food_item['description']
            print(food_description, fdc_id)
            store_fdc_item(fdc_id=fdc_id, )

            # food_nutrients = food_item['foodNutrients']
            # food_measures = food_item['foodMeasures']

        else:
            print("Request failed with status code:", response.status_code)


'''
Survey (FNDDS)

fdcId
description
commonNames XXX
additionalDescriptions
dataType
foodCode
publishedDate
foodCategory
foodCategoryId
allHighlightFields XXX
score XXX
microbes XXX
foodNutrients 
finalFoodInputFoods XXX
foodMeasures 
foodAttributes XXX
foodAttributeTypes XXX
foodVersionIds XXX
'''

'''
NOTE FNDDS:
fdcId
description
scientificName
commonNames
additionalDescriptions
dataType
ndbNumber
publishedDate
foodCategory
mostRecentAcquisitionDate
allHighlightFields
score
microbes
foodNutrients
finalFoodInputFoods
foodMeasures
foodAttributes
foodAttributeTypes
foodVersionIds

NOTE SR Legacy
fdcId
description
scientificName
commonNames
additionalDescriptions
dataType
ndbNumber
publishedDate
foodCategory
allHighlightFields
score
microbes
foodNutrients
finalFoodInputFoods
foodMeasures
foodAttributes
foodAttributeTypes
foodVersionIds
'''

'''
totalHits
currentPage
totalPages
pageList
foodSearchCriteria
foods
aggregations
'''