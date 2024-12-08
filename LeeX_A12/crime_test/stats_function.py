# Uses pandas dataframe to find mean and median of 'Vict age'

def age_stats(data):
    if data.empty:
        return "Empty dataframe"

    mean_age = data['Vict age'].mean()
    median_age = data['Vict age'].median()

    return f"The mean victim age is {mean_age} and the median victim age is {median_age}"
