
chosen_item_attributes = [
    'fdcId',
    'description',
    'additionalDescriptions',
    'dataType',
    'publishedDate',
    'foodCategory',
    'foodCategoryId',
]
    # 'foodNutrients', 
    # 'foodMeasures', 


nutrient_attributes = [
    'foodNutrientId',
    'nutrientId',
    'nutrientName',
    'nutrientNumber',
    'unitName',
    'value',
]

measure_attributes = [
    'id',
    'disseminationText',
    'gramWeight',
    # 'measureUnitAbbreviation',
    # 'measureUnitId',
    # 'measureUnitName',
]

# USDA fdc FNDDS database nutrient names to column names in local database
nutrient_categories = {
    # Proximates
    'Water': {'nutrientCategory': 'Proximates', 'nutrientName': 'water'},
    'Energy': {'nutrientCategory': 'Proximates', 'nutrientName': 'energy'},
    'Protein': {'nutrientCategory': 'Proximates', 'nutrientName': 'protein'},
    'Total lipid (fat)': {'nutrientCategory': 'Proximates', 'nutrientName': 'fat'},

    # Carbohydrates
    'Carbohydrate, by difference': {'nutrientCategory': 'Carbohydrates', 'nutrientName': 'carbohydrate'},
    'Fiber, total dietary': {'nutrientCategory': 'Carbohydrates', 'nutrientName': 'fiber'},
    'Sugars, total including NLEA': {'nutrientCategory': 'Carbohydrates', 'nutrientName': 'sugars'},

    # Minerals
    'Calcium, Ca': {'nutrientCategory': 'Minerals', 'nutrientName': 'calcium'},
    'Iron, Fe': {'nutrientCategory': 'Minerals', 'nutrientName': 'iron'},
    'Magnesium, Mg': {'nutrientCategory': 'Minerals', 'nutrientName': 'magnesium'},
    'Phosphorus, P': {'nutrientCategory': 'Minerals', 'nutrientName': 'phosphorus'},
    'Potassium, K': {'nutrientCategory': 'Minerals', 'nutrientName': 'potassium'},
    'Sodium, Na': {'nutrientCategory': 'Minerals', 'nutrientName': 'sodium'},
    'Zinc, Zn': {'nutrientCategory': 'Minerals', 'nutrientName': 'zinc'},
    'Copper, Cu': {'nutrientCategory': 'Minerals', 'nutrientName': 'copper'},
    'Selenium, Se': {'nutrientCategory': 'Minerals', 'nutrientName': 'selenium'},

    # Vitamins
    'Vitamin C, total ascorbic acid': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_C'},
    'Thiamin': {'nutrientCategory': 'Vitamins', 'nutrientName': 'thiamin'},
    'Riboflavin': {'nutrientCategory': 'Vitamins', 'nutrientName': 'riboflavin'},
    'Niacin': {'nutrientCategory': 'Vitamins', 'nutrientName': 'niacin'},
    'Vitamin B-6': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_B6'},
    'Folate, total': {'nutrientCategory': 'Vitamins', 'nutrientName': 'folate_total'},
    'Folic acid': {'nutrientCategory': 'Vitamins', 'nutrientName': 'folic_acid'},
    'Folate, food': {'nutrientCategory': 'Vitamins', 'nutrientName': 'folate_food'},
    'Folate, DFE': {'nutrientCategory': 'Vitamins', 'nutrientName': 'folate_DFE'},
    'Choline, total': {'nutrientCategory': 'Vitamins', 'nutrientName': 'choline_total'},
    'Vitamin B-12': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_B12'},
    'Vitamin B-12, added': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_B12_added'},
    'Vitamin A, RAE': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_A'},
    'Retinol': {'nutrientCategory': 'Vitamins', 'nutrientName': 'retinol'},
    'Carotene, beta': {'nutrientCategory': 'Vitamins', 'nutrientName': 'carotene_beta'},
    'Carotene, alpha': {'nutrientCategory': 'Vitamins', 'nutrientName': 'carotene_alpha'},
    'Cryptoxanthin, beta': {'nutrientCategory': 'Vitamins', 'nutrientName': 'cryptoxanthin_beta'},
    'Lycopene': {'nutrientCategory': 'Vitamins', 'nutrientName': 'lycopene'},
    'Lutein + zeaxanthin': {'nutrientCategory': 'Vitamins', 'nutrientName': 'lutein_zeaxanthin'},
    'Vitamin E (alpha-tocopherol)': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_E'},
    'Vitamin E, added': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_E_added'},
    'Vitamin D (D2 + D3)': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_D'},
    'Vitamin K (phylloquinone)': {'nutrientCategory': 'Vitamins', 'nutrientName': 'vitamin_K'},

    # Other Components
    'Fatty acids, total saturated': {'nutrientCategory': 'Other Components', 'nutrientName': 'sfa_tot'},
    'Fatty acids, total monounsaturated': {'nutrientCategory': 'Other Components', 'nutrientName': 'mufa_tot'},
    'Fatty acids, total polyunsaturated': {'nutrientCategory': 'Other Components', 'nutrientName': 'pufa_tot'},
    'Cholesterol': {'nutrientCategory': 'Other Components', 'nutrientName': 'cholesterol'},
    'Alcohol, ethyl': {'nutrientCategory': 'Other Components', 'nutrientName': 'alcohol'},
    'Caffeine': {'nutrientCategory': 'Other Components', 'nutrientName': 'caffeine'},
    'Theobromine': {'nutrientCategory': 'Other Components', 'nutrientName': 'theobromine'},
}

# for item in list(nutrient_categories.values()):
#     print(item['nutrientName'])




# USDA fdc FNDDS database nutrient names to column names in local database
# nutrition_template = {
#     'Proximates': {
#         'Water':'water',
#         'Energy':'energy',
#         'Protein':'protein',
#         'Total lipid (fat)':'fat',
#     },
#     'Carbohydrates': {
#         'Carbohydrate, by difference':'carbohydrate',
#         'Fiber, total dietary':'fiber',
#         'Sugars, total including NLEA':'sugars',
#     },
#     'Minerals': {
#         'Calcium, Ca':'calcium',
#         'Iron, Fe':'iron',
#         'Magnesium, Mg':'magnesium',
#         'Phosphorus, P':'phosphorus',
#         'Potassium, K':'potassium',
#         'Sodium, Na':'sodium',
#         'Zinc, Zn':'zinc',
#         'Copper, Cu':'copper',
#         'Selenium, Se':'selenium',
#     },
#     'Vitamins': {
#         'Vitamin C, total ascorbic acid':'vitamin_C',
#         'Thiamin':'thiamin',
#         'Riboflavin':'riboflavin',
#         'Niacin':'niacin',
#         'Vitamin B-6':'vitamin_B6',
#         'Folate, total':'folate_total',
#         'Folic acid':'folic_acid',
#         'Folate, food':'folate_food',
#         'Folate, DFE':'folate_DFE',
#         'Choline, total':'choline_total',
#         'Vitamin B-12':'vitamin_B12',
#         'Vitamin B-12, added':'vitamin_B12_added',
#         'Vitamin A, RAE':'vitamin_A',
#         'Retinol':'retinol',
#         'Carotene, beta':'carotene_beta',
#         'Carotene, alpha':'carotene_alpha',
#         'Cryptoxanthin, beta':'cryptoxanthin_beta',
#         'Lycopene':'lycopene',
#         'Lutein + zeaxanthin':'lutein_zeaxanthin',
#         'Vitamin E (alpha-tocopherol)':'vitamin_E',
#         'Vitamin E, added':'vitamin_E_added',
#         'Vitamin D (D2 + D3)':'vitamin_D',
#         'Vitamin K (phylloquinone)':'vitamin_K',
#     },
#     'Other Components': {
#         'Fatty acids, total saturated':'sfa_tot',
#         'Fatty acids, total monounsaturated':'mufa_tot',
#         'Fatty acids, total polyunsaturated':'pufa_tot',
#         'Cholesterol':'cholesterol',
#         'Alcohol, ethyl':'alcohol',
#         'Caffeine':'caffeine',
#         'Theobromine':'theobromine',
#     }
# }
