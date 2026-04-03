

base_url = 'https://api.nal.usda.gov/fdc/v1'
url = f'{base_url}/foods/search'

api_key = "nII37x9hx8niOAs7MWNOYjaOgzFQ9hdFEs9L6e8g"

fdc_id_test = 2341112

fdc_parameters = {
    'api_key': api_key,
    'query': None,
    'dataType': 'Survey (FNDDS)',
    # 'numberOfResultsPerPage': 1,
    # 'pageNumber': 1,
    # 'pageSize': 1,
    # 'requireAllWords': False,
}


# foods_fndds: fdc_id, NOTE item_name, description, additional_description, data_type, published_date, NOTE category, NOTE subcategory, fndds_subcategory, fndds_subcategory_id
# nutrients_fndds: fdc_id, nutrient_id, 
# 
# measures_fndds: 

# water, energy, protein, fat, carbohydrate, fiber, sugars, calcium, iron, magnesium, phosphorus, potassium, sodium, zinc, copper, selenium, vitamin_C, thiamin, riboflavin, niacin, vitamin_B6, folate_total, folic_acid, folate_food, folate_DFE, choline_total, vitamin_B12, vitamin_B12_added, vitamin_A, retinol, carotene_beta, carotene_alpha, cryptoxanthin_beta, lycopene, lutein_zeaxanthin, vitamin_E, vitamin_E_added, vitamin_D, vitamin_K, sfa_tot, mufa_tot, pufa_tot, cholesterol, alcohol, caffeine, theobromine

