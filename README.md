## Nutrition Tracker

![build](https://img.shields.io/badge/nutrution-tracker-grey)
![build](https://img.shields.io/badge/nutrution-grey)

### Description
A simple app to show the macro and micro nutional facts about every day foods and nutritional content of composites of foods. 

### Data
All data is publically available via United States Department of Agriculture (USDA) and can be downloaded [here](https://fdc.nal.usda.gov/download-datasets).

### Setup Backend
```zsh
cd backend
python -m venv .venv
source .venv/bin/acivate
pip install -r requirements.txt
pip install -e .  # for pyproject "nutrition"
```
Add `scripts/env.sh` to store environment secrets. Use the following to generate and set SECRET_KEY in env for backend.
```zsh
python -c "import secrets; print(secrets.token_hex(32))"
export SECRET_KEY="<Your Secret Key>"  # part of env.sh
```

### Setup Frontend
```zsh
cd frontend
npm install
```

### Run
```zsh
source scripts/env.sh  # export to env
source scripts/backend_run.sh
source scripts/frontend_run.sh
```

### Developer Notes
- Duplicates by description in Foundation, keep most recent entry by publication date
- Inconsistent naming of nutrients between Foundation and SR Legacy, leading bland spaces (removed, use Foundation nutrition names - most up to date)
- Nutrient with nutrient_id = 2066 is missing, but still present in food_nutrients (only nan values however), dropped from the dataset
- When combining Foundation and SR Legacy, there are duplicates between the two, keep the most recent entry, but impute nans with values from the records that are about to be dropped (essentially merge the two records, favour the most recent one)
- Use inkscape to divide sheet of icons into separate .svg files. Convert .png files to .svg?? 
- Remove background and make svgs transparen outside of the actual icon by editing the file content and removing the background path block.
- Crop in either inkscape (keep tight) or programatically in file, can be tricky if not centered however. 
- Scale and adjust boarders / background color via CSS. Use svgs only.
