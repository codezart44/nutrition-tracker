

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

