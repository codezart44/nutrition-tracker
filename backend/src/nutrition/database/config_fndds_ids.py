
'''
fruits
vegetables
dairy_and_eggs
meat_and_poultry
seafood
grains_and_cereals
legumes_and_pulses
nuts_and_seeds
condiments_spices_and_oils
beverages
'''

fruits = {
    2344665: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Orange',},
    2344662: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Lemon',},
    2344664: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Lime',},
    2344659: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Grapefruit',},
    2344669: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Tangerine',},
    2344658: {'category': 'Fruits', 'subcategory': 'Citrus Fruits', 'item_name': 'Clementine',},

    2344777: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Strawberry'},
    2344769: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Blueberry'},
    2344775: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Raspberry'},
    2344767: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Blackberry'},
    2344773: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Cranberry'},
    2344732: {'category': 'Fruits', 'subcategory': 'Berries', 'item_name': 'Grape'},

    2344719: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Avocado'},
    2344720: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Banana'},
    2344755: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Pineapple'},
    2344737: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Mango'},
    2344765: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Watermelon'},
    2344722: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Cantaloupe'},
    2344736: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Honeydew melon'},
    2344741: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Papaya'},
    2344734: {'category': 'Fruits', 'subcategory': 'Tropical Fruits', 'item_name': 'Kiwi fruit'},

    2344711: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Apple'},
    2344744: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Peach'},
    2344749: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Pear'},
    2344760: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Plum'},
    2344740: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Nectarine'},
    2344717: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Apricot'},
    2344726: {'category': 'Fruits', 'subcategory': 'Stone Fruits', 'item_name': 'Cherry'},
}

vegetables = {
    2345120: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Spinach'},
    2345309: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Lettuce'},
    2345103: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Kale'},
    2345075: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Swiss Chard'},
    2345311: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Arugula'},
    2345077: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Collard Greens'},
    2345287: {'category': 'Vegetables', 'subcategory': 'Leafy Greens', 'item_name': 'Asparagus'},

    2345151: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Broccoli'},
    2345297: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Cauliflower'},
    2345292: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Brussels Sprouts'},
    2345295: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Red Cabbage'},
    2345293: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Green Cabbage'},
    2345294: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Bok Choy'},
    2345308: {'category': 'Vegetables', 'subcategory': 'Cruciferous Vegetables', 'item_name': 'Kohlrabi'},

    2345173: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Carrots'},
    2344876: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Potatoes'},
    2345210: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Sweet Potatoes'},
    2345323: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Radishes'},
    2345290: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Beets'},
    2345329: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Turnips'},
    # XXXXXXX: {'category': 'Vegetables', 'subcategory': 'Root Vegetables', 'item_name': 'Parsnips'},   # NOTE info about RAW as SR Legacy, or info about cooked in FNDDS

    ## NOTE CONVERT THESE TO THE FORMAT ABOVE!
    'Alliums': {
        'Onions': 2345315,                      # red by default, others can be foun in SR Legacy / Foundation
        'Garlic': 2345306,
        # 'Shallots': 1,                        # found in SR Legacy
        # 'Leeks': 1,                           # only cooked, otherwise SR legacy
        'Scallions': 2345314,
    },
    'Fruiting Vegetables': {
        'Tomatoes': 2345232,
        'Bell Peppers': 2345319,
        # 'Red chili': 1,                       # SR Legacy
        'Chili (Hot Pepper)': 2345623,          # General (actually jalapeno??)
        'Eggplant': 2345305,
        # 'Tomatillos': 1,                      # SR Legacy
        'Sweet Corn': 2345303,
    },
    'Legumes': {
        'Green Beans': 2345289,
        'Green Peas': 2345317,
        'Lentils': 2342898, 
        'Chickpeas': 2342889,
        'Kidney Beans': 2342854,
        'Black Beans': 2342834,
    },
    'Squash and Gourds': {
        'Zucchini (Green Squash)': 2345328, 
        'Yellow Squash': 2345327,
        'Winter Squash': 2345206,               # includes hubbard;gourd;acorn;pumpkin;butternut. More details in SR legacy
        # 'Butternut Squash': 1,
        # 'Acorn Squash': 1,
        # 'Pumpkin': 1,
        'Cucumbers': 2345304,
    },

}









###################################################################################################
###################################################################################################
###################################################################################################

fruits_structure = {
    'Citrus Fruits': {
        'Orange': 2344665,
        'Lemon': 2344662,
        'Lime': 2344664,
        'Grapefruit': 2344659,
        'Tangerine': 2344669,
        'Clementine': 2344658,
    },
    'Berries': {
        'Strawberry': 2344777,
        'Blueberry': 2344769,
        'Raspberry': 2344775,
        'Blackberry': 2344767,
        'Cranberry': 2344773,
        'Grape': 2344732,
    },
    'Tropical Fruits': {
        'Avocado': 2344719,
        'Banana': 2344720,
        'Pineapple': 2344755,
        'Mango': 2344737,
        'Watermelon': 2344765,
        'Cantaloupe': 2344722,
        'Honeydew melon': 2344736,
        'Papaya': 2344741,
        'Kiwi fruit': 2344734,
    },
    'Stone Fruits': {
        'Apple': 2344711,
        'Peach': 2344744,
        'Pear': 2344749,
        'Plum': 2344760,
        'Nectarine': 2344740,
        'Apricot': 2344717,
        'Cherry': 2344726,
    },
}

vegetables = {
    'Leafy Greens': {
        'Spinach': 2345120,
        'Lettuce': 2345309,
        'Kale': 2345103,
        'Swiss Chard': 2345075,
        'Arugula': 2345311,
        'Collard Greens': 2345077,
        'Asparagus': 2345287,
    },
    'Cruciferous Vegetables': {
        'Broccoli': 2345151,
        'Cauliflower': 2345297,
        'Brussels Sprouts': 2345292,
        'Red Cabbage': 2345295,
        'Green Cabbage': 2345293,
        'Bok Choy': 2345294,
        'Kohlrabi': 2345308,
    },
    'Root Vegetables': {
        'Carrots': 2345173,
        'Potatoes': 2344876,
        'Sweet Potatoes': 2345210,
        'Radishes': 2345323,
        'Beets': 2345290,
        'Turnips': 2345329,
        # 'Parsnips': 1,                        # NOTE info about RAW as SR Legacy, or info about cooked in FNDDS
    },
    'Alliums': {
        'Onions': 2345315,                      # red by default, others can be foun in SR Legacy / Foundation
        'Garlic': 2345306,
        # 'Shallots': 1,                        # found in SR Legacy
        # 'Leeks': 1,                           # only cooked, otherwise SR legacy
        'Scallions': 2345314,
    },
    'Fruiting Vegetables': {
        'Tomatoes': 2345232,
        'Bell Peppers': 2345319,
        # 'Red chili': 1,                       # SR Legacy
        'Chili (Hot Pepper)': 2345623,          # General (actually jalapeno??)
        'Eggplant': 2345305,
        # 'Tomatillos': 1,                      # SR Legacy
        'Sweet Corn': 2345303,
    },
    'Legumes': {
        'Green Beans': 2345289,
        'Green Peas': 2345317,
        'Lentils': 2342898, 
        'Chickpeas': 2342889,
        'Kidney Beans': 2342854,
        'Black Beans': 2342834,
    },
    'Squash and Gourds': {
        'Zucchini (Green Squash)': 2345328, 
        'Yellow Squash': 2345327,
        'Winter Squash': 2345206,               # includes hubbard;gourd;acorn;pumpkin;butternut. More details in SR legacy
        # 'Butternut Squash': 1,
        # 'Acorn Squash': 1,
        # 'Pumpkin': 1,
        'Cucumbers': 2345304,
    },
    # 'Mushrooms': {                            # SR Legacy for ALL mushrooms
    #     # 'Chanterelle Mushrooms': 1,
    #     # 'Button Mushrooms': 1,
    #     # 'Cremini Mushrooms': 1,
    #     # 'Portobello Mushrooms': 1,
    #     # 'Shiitake Mushrooms': 1,
    #     # 'Oyster Mushrooms': 1,
    #     # 'Enoki Mushrooms': 1,
    # },
}  

dairy_and_eggs = {
    'Milk': 2340761,                    # There are many varieties of Milk etc
    'Cheese, Brie': 2341111,            # Many more in SR Legacy, use SR rather than FNDDS
    'Cheese, Cheddar': 2341112,
    'Cheese, Feta': 2341117,
    'Cheese, Goat': 2341119,
    'Cheese, Swiss': 2341138,
    'Cheese, Ricotta': 2341153,
    'Yogurt': 2340795,
    'Butter': 2345703,
    'Eggs': 2342627,
}

meat_and_poultry = {
    'Beef': 2341227,
    'Beef Ground': 2341259,
    'Chicken (back)': 2341487,
    'Pork': 2341267,
    'Lamb': 2341311,
    'Turkey': 2341540,
    'Venison (Deer)': 2341319,
    'Rabbit': 2341318,
    # 'Duck': 1,                    # SR Legacy
    # 'Quail': 1,                   # SR Legacy
    'Bison': 2341326,
    # 'Elk': 1,                     # falls under Venison, otherwise SR Legacy
}

seafood = {
    'Seafood': {
        'Fish': {
            'Salmon': 2341700,
            'Tuna': 2341724,
            'Cod': 2341655,
            'Trout': 2341717,
            'Pike': 2341691,
            'Bass': 2341709,
            'Mackerel': 2341678,
        },
        'Shellfish': {
            'Shrimp': 2341775,
            'Crab': 2341759,
            'Lobster': 2341764,
            'Clams': 2341753,
            'Oyster': 2341766,
        },
    }
}


# Divide into, rice, pasta, flour (ground), and other (quinoa etc)
grains_and_cereals = {
    # 'Rice': 1,                # SR Legacy
    # 'Wheat': 1,               # SR Legacy Wheat Bran, crude
    'Oats': 2343973,
    # 'Barley': 1,
    'Quinoa': 2343884,
    # 'Pasta': 1,               # SR Legacy
    # 'Cornmeal': 1,
}

nuts_and_seeds = {
    'Almonds': 2342962,
    'Walnuts': 2343008,
    'Cashews': 2342970,
    'Sunflower Seeds': 2343060,
    'Chia Seeds': 2343065,
    'Flaxseeds': 2343063,
    'Pistachios': 2343004,
    'Pecans': 2342998,
    'Pumpkin Seeds (Pepitas)': 2343054,
    'Sesame Seeds': 2343061,
    # 'Hemp Seeds': 1,                          # SR Legacy
    # 'Poppy Seeds': 1,
}
    
condiments_spices_and_oils = {
    # 'Condiments and Spices': {        # SR Legacy
    #     # 'Salt': 1,
    #     'Pepper': 1,
    #     'Sugar': 1,
    #     'Vinegar': 1,
    #     'Mustard': 1,
    #     'Ketchup': 1,
    #     'Soy Sauce': 1,
    # },
    'Cooking Oils and Fats': {
        'Olive Oil': 2345743,
        'Canola Oil': 2345745,
        'Coconut Oil': 2345739,
        'Sesame Oil': 2345747,
        'Corn Oil': 2345740,
        'Almond Oil': 2345738,
        'Flaxseed Oil': 2345742,
        'Walnut Oil': 2345750,
        'Soybean Oil': 2345748,
        'Sunflower Oil': 2345749,
        'Vegetable Oil, NFS': 2345737,
    },
    'Sauces': {                         # These should be from Branded or homemade from fundamentals (Or add light, regular versions of generalized FNDDS)
        'Barbecue Sauce': 2345263,
        'Hot Pepper Sauce': 2345620,
        'Hot Thai Sauce': 2345257,
        'Worcestershire Sauce': 2342922,
        'Mayonnaise': 2345761,
        'Ranch Dressing': 2345769,
        'Caesar Dressing': 2345756,
        # 'Italian Dressing': 1,              # SR Legacy
        # 'Balsamic Vinaigrette': 1,
        'Salsa': 2345249,
        'Teriyaki Sauce': 2342920,
        'Hoisin Sauce': 2342916,
        'Pesto': 2345732,
    },
    # 'Herbs and Spices': {             # SR Legacy
    #     'Basil': 1,
    #     'Oregano': 1,
    #     'Rosemary': 1,
    #     'Cumin': 1,
    #     'Paprika': 1,
    #     'Turmeric': 1,
    #     'Cinnamon': 1,
    #     'Nutmeg': 1,
    #     'Chili Powder': 1,
    #     'Garlic Powder': 1,
    #     'Onion Powder': 1,
    #     'Curry Powder': 1,
    # },
}

# maybe add alcoholic drinks, like wine and beer (should not promote alchohol though)
beverages = {
    'Water': 1,
    'Juice': 1,
    'Soft Drinks': 1,
    'Tea': 1,
    'Coffee': 1,
}

# NOTE add later on, already included in vegetables
# legumes_and_pulses = {
#     'Lentils': 1,
#     'Chickpeas (Garbanzo Beans)': 1,
#     'Black Beans': 1,
#     'Kidney Beans': 1,
#     'Navy Beans': 1,
#     'Pinto Beans': 1,
#     'Split Peas': 1,
#     'Green Peas': 1,
#     'Fava Beans': 1,
#     'Adzuki Beans': 1,
#     'Lima Beans': 1,
#     'Mung Beans': 1,
#     'Black-eyed Peas': 1,
#     'Soybeans': 1,
#     'Edamame (Young Soybeans)': 1,
#     'Tofu': 1,
#     'Miso': 1,
#     'Soy Milk': 1,
# }






# meat_and_poultry = {
#     'Beef': {
#         'Ground Beef': 1,
#         'Steak (e.g., Ribeye, Sirloin, Filet Mignon)': 1,
#         'Roast (e.g., Chuck Roast, Brisket)': 1,
#         'Beef Ribs': 1,
#         'Beef Offal (e.g., Liver, Kidneys)': 1,
#     },
#     'Chicken': {
#         'Whole Chicken': 1,
#         'Chicken Breasts': 1,
#         'Chicken Thighs': 1,
#         'Chicken Drumsticks': 1,
#         'Chicken Wings': 1,
#         'Ground Chicken': 1,
#         'Chicken Offal (e.g., Liver, Hearts, Gizzards)': 1,
#     },
#     'Pork': {
#         'Pork Chops': 1,
#         'Pork Tenderloin': 1,
#         'Pork Ribs': 1,
#         'Pork Shoulder (Pork Butt)': 1,
#         'Ground Pork': 1,
#         'Bacon': 1,
#         'Ham': 1,
#         'Sausages (e.g., Breakfast Sausage, Italian Sausage)': 1,
#     },
#     'Lamb': {
#         'Lamb Chops': 1,
#         'Lamb Shoulder': 1,
#         'Ground Lamb': 1,
#         'Lamb Shank': 1,
#         'Lamb Ribs': 1,
#         'Lamb Offal (e.g., Liver, Kidneys)': 1,
#     },
#     'Turkey': {
#         'Whole Turkey': 1,
#         'Turkey Breast': 1,
#         'Ground Turkey': 1,
#         'Turkey Drumsticks': 1,
#         'Turkey Sausage': 1,
#         'Turkey Offal (e.g., Liver, Hearts, Gizzards)': 1,
#     },
#     'Game Meats': {
#         'Venison (Deer)': 1,
#         'Rabbit': 1,
#         'Duck': 1,
#         'Quail': 1,
#         'Bison': 1,
#         'Elk': 1,
#     },
# }
