'''
def validate(age, state, zip_code):
    validity_flag = False
    if age > 18 and state in ['FL', 'GA', "TN", "NC"]:
        validity_flag = True
    return validity_flag
'''

def validate(age, *args, **kwargs):
    validity_flag = False
    errorMsg = []
    print(type(args))
    for eachVar in args:
        print(eachVar)
    print(type(kwargs))
    for key,value in kwargs.items():
        if key == "zip_code":
            errrMessage = validate_zipcode(value)
            if len(errrMessage) > 0:
                errorMsg.append(errrMessage)
        if key == "store_loc":
            validate_store_loc(value)


def validate_zipcode(zipCode):
    errorMessage = ""
    if not len(str(zipCode).strip()) == 5:
        errorMessage = "Inalid zip code"
    return errorMessage

def validate_store_loc(value):
    print("Validation")

validate(45, "Name", "State", "English", zip_code = "30080", store_loc = "3310 Park Street")