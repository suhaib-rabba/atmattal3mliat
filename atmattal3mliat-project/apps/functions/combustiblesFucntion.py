

def tamem_diesel_year(year, diesel_tamem):
    if year == 2019:
        diesel_tamem = diesel_tamem.dieselTamem_2019
    elif year == 2020:
        diesel_tamem = diesel_tamem.dieselTamem_2020
    elif year == 2021:
        diesel_tamem = diesel_tamem.dieselTamem_2021
    elif year == 2022:
        diesel_tamem = diesel_tamem.dieselTamem_2022
    return diesel_tamem
