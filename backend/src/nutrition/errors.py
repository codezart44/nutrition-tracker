
class ValidationError(Exception): 
    pass

def validation_error(e: ValidationError):
    return {"error": str(e)}, 400
