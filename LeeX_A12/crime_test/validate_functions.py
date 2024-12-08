
"""
Uses pandas dataframe to ensure Vict sex is not null and M or F
and Vict age is not null and ranges from 1 to 100 
"""

def validate_sex_age(data):
    validate_sex =  data['Vict sex'].isin(['M', 'F']) & data['Vict sex'].notnull()
    validate_age = data['Vict age'].notnull() & (data['Vict age'] >= 1) & (data['Vict age'] <= 100)

    return validate_sex.all() and validate_age.all()



