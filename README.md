## Nutrition Tracker

![build](https://img.shields.io/badge/nutrution-tracker-grey)


### Description
A simple app to show the macro and micro nutional facts about every day foods and what nutrition composites of foods hold. 

### Data
All data is publically available via United States Department of Agriculture (USDA) and can be downloaded [here](https://fdc.nal.usda.gov/download-datasets).

- Duplicates by description in Foundation, keep most recent entry by publication date
- Inconsistent naming of nutrients between Foundation and SR Legacy, leading bland spaces (removed, use Foundation nutrition names - most up to date)
- Nutrient with nutrient_id = 2066 is missing, but still present in food_nutrients (only nan values however), dropped from the dataset
- When combining Foundation and SR Legacy, there are duplicates between the two, keep the most recent entry, but impute nans with values from the records that are about to be dropped (essentially merge the two records, favour the most recent one)
