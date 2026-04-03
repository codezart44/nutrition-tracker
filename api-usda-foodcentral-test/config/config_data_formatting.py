
chosen_attributes = [
    'fdcId',
    'description',
    'additionalDescriptions',
    'dataType',
    'publishedDate',
    'foodCategory',
    'foodCategoryId',
    'foodNutrients', 
    'foodMeasures', 
]

nutrient_attributes = {
    'nutrientId',
    'nutrientName',
    'unitName',
    'value',
}

# USDA fdc FNDDS database nutrient names to column names in local database
nutrition_template = {
    'Proximates': {
        'Water':'water',
        'Energy':'energy',
        'Protein':'protein',
        'Total lipid (fat)':'fat',
    },
    'Carbohydrates': {
        'Carbohydrate, by difference':'carbohydrate',
        'Fiber, total dietary':'fiber',
        'Sugars, total including NLEA':'sugars',
    },
    'Minerals': {
        'Calcium, Ca':'calcium',
        'Iron, Fe':'iron',
        'Magnesium, Mg':'magnesium',
        'Phosphorus, P':'phosphorus',
        'Potassium, K':'potassium',
        'Sodium, Na':'sodium',
        'Zinc, Zn':'zinc',
        'Copper, Cu':'copper',
        'Selenium, Se':'selenium',
    },
    'Vitamins': {
        'Vitamin C, total ascorbic acid':'vitamin_C',
        'Thiamin':'thiamin',
        'Riboflavin':'riboflavin',
        'Niacin':'niacin',
        'Vitamin B-6':'vitamin_B6',
        'Folate, total':'folate_total',
        'Folic acid':'folic_acid',
        'Folate, food':'folate_food',
        'Folate, DFE':'folate_DFE',
        'Choline, total':'choline_total',
        'Vitamin B-12':'vitamin_B12',
        'Vitamin B-12, added':'vitamin_B12_added',
        'Vitamin A, RAE':'vitamin_A',
        'Retinol':'retinol',
        'Carotene, beta':'carotene_beta',
        'Carotene, alpha':'carotene_alpha',
        'Cryptoxanthin, beta':'cryptoxanthin_beta',
        'Lycopene':'lycopene',
        'Lutein + zeaxanthin':'lutein_zeaxanthin',
        'Vitamin E (alpha-tocopherol)':'vitamin_E',
        'Vitamin E, added':'vitamin_E_added',
        'Vitamin D (D2 + D3)':'vitamin_D',
        'Vitamin K (phylloquinone)':'vitamin_K',
    },
    'Other Components': {
        'Fatty acids, total saturated':'sfa_tot',
        'Fatty acids, total monounsaturated':'mufa_tot',
        'Fatty acids, total polyunsaturated':'pufa_tot',
        'Cholesterol':'cholesterol',
        'Alcohol, ethyl':'alcohol',
        'Caffeine':'caffeine',
        'Theobromine':'theobromine',
    }
}
