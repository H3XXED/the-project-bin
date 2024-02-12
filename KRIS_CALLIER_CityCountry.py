
def format_city_country_string(city, country):
    if not type(city) is str:
        raise TypeError("City must be in string form.")
    if not type(country) is str:
        raise TypeError("Country must be in string form.")
    if len(city) == 0:
        raise Exception("No city input given.")
    if len(country) == 0:
        raise Exception("No country input given.")

    format_string = city + ", " + country
    return format_string
