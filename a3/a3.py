"""CSCA08: Fall 2022 -- Assignment 3: Hypertension and Low Income

Starter code.

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Jacqueline Smith, David Liu, and Anya Tafliovich

"""

from typing import TextIO
import statistics

from constants import (CityData, ID, HT, TOTAL, LOW_INCOME,
                       SEP, HT_ID_COL, LI_ID_COL,
                       HT_NBH_NAME_COL, LI_NBH_NAME_COL,
                       HT_20_44_COL, NBH_20_44_COL,
                       HT_45_64_COL, NBH_45_64_COL,
                       HT_65_UP_COL, NBH_65_UP_COL,
                       POP_COL, LI_POP_COL,
                       HT_20_44_IDX, HT_45_64_IDX, HT_65_UP_IDX,
                       NBH_20_44_IDX, NBH_45_64_IDX, NBH_65_UP_IDX
                       )
SAMPLE_DATA = {
    'West Humber-Clairville': {
        'id': 1,
        'hypertension': [703, 13291, 3741, 9663, 3959, 5176],
        'total': 33230, 'low_income': 5950},
    'Mount Olive-Silverstone-Jamestown': {
        'id': 2,
        'hypertension': [789, 12906, 3578, 8815, 2927, 3902],
        'total': 32940, 'low_income': 9690},
    'Thistletown-Beaumond Heights': {
        'id': 3,
        'hypertension': [220, 3631, 1047, 2829, 1349, 1767],
        'total': 10365, 'low_income': 2005},
    'Rexdale-Kipling': {
        'id': 4,
        'hypertension': [201, 3669, 1134, 3229, 1393, 1854],
        'total': 10540, 'low_income': 2140},
    'Elms-Old Rexdale': {
        'id': 5,
        'hypertension': [176, 3353, 1040, 2842, 948, 1322],
        'total': 9460, 'low_income': 2315}
}

SAMPLE_2 = {
    'Halifax': {
        'id': 1,
        'hypertension': [345, 4234, 532, 3452, 6254, 25895],
        'total': 35156, 'low_income': 7638},
    'Bedford': {
        'id': 2,
        'hypertension': [23, 453, 1234, 6735, 34, 566],
        'total': 8000, 'low_income': 5000},
    'Sackville': {
        'id': 3,
        'hypertension': [34, 65, 345, 533, 4352, 5543],
        'total': 6200, 'low_income': 4932}
}

SAMPLE_3 = {
    'Mile-End': {
        'id': 1,
        'hypertension': [2345, 6357, 3445, 4668, 45, 78],
        'total': 11300, 'low_income': 8000},
    'Montreal': {
        'id': 2,
        'hypertension': [3749, 6739, 465, 678, 8374, 10093],
        'total': 18000, 'low_income': 15739},
    'Plato': {
        'id': 3,
        'hypertension': [44, 245, 8473, 9384, 3845, 4975],
        'total': 15500, 'low_income': 12938},
    'Centre': {
        'id': 4,
        'hypertension': [374, 3749, 4654, 5946, 4834, 5738],
        'total': 15500, 'low_income': 13948}
    }

EPSILON = 0.005


def get_hypertension_data(city_data: CityData, ht_file: TextIO) -> None:
    """Modify the ht_data dictionary so that it contains the hypertension data
    from ht_file. Update the hypertension data if the neighbourhood in the file
    is already in ht_data, else, add it.
    """

    general_ht = data_list(ht_file)
    for city_info in general_ht:
        if city_info[HT_NBH_NAME_COL] not in city_data:
            num_list = []
            num_list.extend(city_info[HT_20_44_COL:])
            nbh_data = {}
            nbh_data[ID] = int(city_info[HT_ID_COL])
            nbh_data[HT] = str_to_int(num_list)
            city_data[city_info[HT_NBH_NAME_COL]] = nbh_data
        else:
            num_list = []
            num_list.extend(int(city_info[HT_20_44_COL:]))
            city_data[city_info[HT_NBH_NAME_COL]][HT] = num_list


def str_to_int(num_list: list[str]) -> list[int]:
    """Return the a new num_list with each string as an integer.

    Precondition: each item in the list is a number in from of a string.

    >>> str_to_int(['32', '3', '64'])
    [32, 3, 64]

    >>> str_to_int(['53', '2'])
    [53, 2]

    >>> str_to_int(['5873', '54', '422', '1'])
    [5873, 54, 422, 1]
    """

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list


def data_list(file: TextIO) -> list[list[str]]:
    """Return a list of lists each containing the hypertension data from the
    file ht_file as elements.
    """

    data = []
    for line in file.readlines()[1:]:
        info = line.strip().split(SEP)
        data.append(info[:])
    return data


def get_low_income_data(city_data: CityData, low_file: TextIO) -> None:
    """Modify the ht_data dictionary so that it contains the low income data in
    the file low_file. Update the low income file if the neighbourhood in the
    file is already in ht_data, else, add it.
    """

    general_low = data_list(low_file)
    for city_info in general_low:
        if city_info[HT_NBH_NAME_COL] not in city_data:
            nbh_data = {}
            nbh_data[ID] = int(city_info[LI_ID_COL])
            nbh_data[TOTAL] = int(city_info[POP_COL])
            nbh_data[LOW_INCOME] = int(city_info[LI_POP_COL])
            city_data[city_info[HT_NBH_NAME_COL]] = nbh_data
        else:
            city_data[city_info[LI_NBH_NAME_COL]][TOTAL] = int(city_info[
                POP_COL])
            city_data[city_info[LI_NBH_NAME_COL]][LOW_INCOME] = int(city_info[
                LI_POP_COL])


def get_bigger_neighbourhood(city_data: CityData, nbh1: str, nbh2: str) -> str:
    """Return the name of the neighbourhood that has a higher population
    between nbh1 and nbh2 according to the low income data. Assume a
    neighbourhood has a population of 0 if it is not in the dictionary.
    Return the first name in case of a tie.

    Precondition: the two neighbourhood names are different.

    >>> get_bigger_neighbourhood(SAMPLE_DATA, 'West Humber-Clairville',
    ...                         'Elms-Old Rexdale')
    'West Humber-Clairville'

    >>> get_bigger_neighbourhood(SAMPLE_2, 'Bedford', 'Halifax')
    'Halifax'

    >>> get_bigger_neighbourhood(SAMPLE_3, 'Mile-End', 'Halifax')
    'Mile-End'
    """

    if nbh1 in city_data.keys():
        if nbh2 in city_data.keys():
            if city_data[nbh1][TOTAL] >= city_data[nbh2][TOTAL]:
                return nbh1
        if nbh2 not in city_data.keys():
            return nbh1
    elif (nbh1 and nbh2) not in city_data.keys():
        return nbh1
    return nbh2


def get_high_hypertension_rate(city_data: CityData, treshold: float) -> list[
                                                        tuple[str, float]]:
    """Return a list of tuples representing all neighbourhoods with a
    hypertension rate greater than or equal to the treshold.

    >>> get_high_hypertension_rate(SAMPLE_DATA, 0.3)
    [('Thistletown-Beaumond Heights', 0.31797739151574084),\
 ('Rexdale-Kipling', 0.3117001828153565)]

    >>> get_high_hypertension_rate(SAMPLE_2, 0.6)
    [('Sackville', 0.7703957010258915)]

    >>> get_high_hypertension_rate(SAMPLE_3, 0.5)
    [('Mile-End', 0.5255336395568765), ('Montreal', 0.7189034837235865),\
 ('Plato', 0.8464804163242947), ('Centre', 0.639020281215577)]
    """

    new = []
    for city in city_data:
        if ht_rate(city_data, city) >= treshold:
            new.append((city, ht_rate(city_data, city)))
    return new


def ht_rate(city_data: CityData, nbh_name: str) -> float:
    """Return the hypertension rate for the given neighbourhood in the given
    city_data dictionary.

    Precondition: nbh_name is a key in city_data.

    >>> ht_rate(SAMPLE_2, 'Bedford')
    0.16649471240649988

    >>> ht_rate(SAMPLE_DATA, 'Thistletown-Beaumond Heights')
    0.31797739151574084

    >>> ht_rate(SAMPLE_3, 'Montreal')
    0.7189034837235865
    """

    total = 0
    hypertension = 0
    for i in range(0, len(city_data[nbh_name][HT]), 2):
        hypertension += city_data[nbh_name][HT][i]
    for i in range(1, len(city_data[nbh_name][HT]) + 1, 2):
        total += city_data[nbh_name][HT][i]
    return hypertension/total


def li_rate(city_data: CityData, nbh_name: str) -> float:
    """Return the low income rate for the given neighbourhood in the given
    city_data dictionary.

    Precondition: city is a key in city_data.

    >>> li_rate(SAMPLE_DATA, 'Elms-Old Rexdale')
    0.24471458773784355

    >>> li_rate(SAMPLE_2, 'Sackville')
    0.795483870967742

    >>> li_rate(SAMPLE_3, 'Centre')
    0.8998709677419355
    """

    return city_data[nbh_name][LOW_INCOME] / city_data[nbh_name][TOTAL]


def get_ht_to_low_income_ratios(city_data: CityData) -> dict[str, float]:
    """Return a dictionary where the keys are the same as in city_data, and the
    values are the ratio of the hypertension rate to the low income rate for
    that neighbourhood.

    Precondition: no neighbourhood has 0 population.

    >>> get_ht_to_low_income_ratios(SAMPLE_DATA)
    {'West Humber-Clairville': 1.6683148168616895,\
 'Mount Olive-Silverstone-Jamestown': 0.9676885451091314,\
 'Thistletown-Beaumond Heights': 1.6438083107534431, 'Rexdale-Kipling':\
 1.5351962275111484, 'Elms-Old Rexdale': 1.1763941257986577}

    >>> get_ht_to_low_income_ratios(SAMPLE_2)
    {'Halifax': 0.9774096296410832, 'Bedford': 0.2663915398503998,\
 'Sackville': 0.968461749059312}

    >>> get_ht_to_low_income_ratios(SAMPLE_3)
    {'Mile-End': 0.742316265874088, 'Montreal': 0.822178201094387,\
 'Plato': 1.0141015963075102, 'Centre': 0.7101243446258562}
    """

    new_dict = {}
    for city in city_data:
        new_dict[city] = ht_rate(city_data, city) / li_rate(city_data, city)
    return new_dict


def calculate_ht_rates_by_age_group(city_data: CityData, nbh_name: str
                                    ) -> tuple[float, float, float]:
    """Return a tuple of the hypertension rate for each of the three age groups
    in the neighborhood as a percentage.

    Precondition: nbh_name is a key in CityData.

    >>> calculate_ht_rates_by_age_group(SAMPLE_DATA, 'Elms-Old Rexdale')
    (5.24903071875932, 36.593947923997185, 71.70953101361573)

    >>> calculate_ht_rates_by_age_group(SAMPLE_2, 'Halifax')
    (8.14832309872461, 15.41135573580533, 24.15138057540066)

    >>> calculate_ht_rates_by_age_group(SAMPLE_3, 'Montreal')
    (55.631399317406135, 68.58407079646017, 82.96839393639156)
    """

    ht_rate1 = (city_data[nbh_name][HT][0]/city_data[nbh_name][HT][1])*100
    ht_rate2 = (city_data[nbh_name][HT][2]/city_data[nbh_name][HT][3])*100
    ht_rate3 = (city_data[nbh_name][HT][4]/city_data[nbh_name][HT][5])*100

    return (ht_rate1, ht_rate2, ht_rate3)


# This function is provided for use in Task 3. You do not need to
# change it.  Note the use of EPSILON constant (similar to what we had
# in assignment 2) for testing.

def get_age_standardized_ht_rate(city_data: CityData, nbh_name: str) -> float:
    """Return the age standardized hypertension rate from the
    neighbourhood in city_data with neighbourhood name nbh_name.

    Precondition: nbh_name is in city_data

    >>> abs(get_age_standardized_ht_rate(SAMPLE_DATA, 'Elms-Old Rexdale') -
    ...     24.44627) < EPSILON
    True
    >>> abs(get_age_standardized_ht_rate(SAMPLE_DATA, 'Rexdale-Kipling') -
    ...     24.72562) < EPSILON
    True

    """

    rates = calculate_ht_rates_by_age_group(city_data, nbh_name)

    # These rates are normalized for only 20+ ages, using the census data
    # that our datasets are based on.
    canada_20_44 = 11_199_830 / 19_735_665   # Number of 20-44 / Number of 20+
    canada_45_64 = 5_365_865 / 19_735_665    # Number of 45-64 / Number of 20+
    canada_65_plus = 3_169_970 / 19_735_665  # Number of 65+ / Number of 20+

    return (rates[0] * canada_20_44 + rates[1] * canada_45_64 +
            rates[2] * canada_65_plus)


def get_correlation(city_data: dict) -> float:
    """Return the correlation between age standardised hypertension rates and
    low income rates across all neighbourhoods.

    >>> get_correlation(SAMPLE_DATA)
    0.28509539188554994

    >>> get_correlation(SAMPLE_2)
    0.6791142794076196

    >>> get_correlation(SAMPLE_3)
    -0.04406912121515742
    """

    age_stand_hp = []
    low_rate = []

    for city in city_data:
        age_stand_hp.append(get_age_standardized_ht_rate(city_data, city))
        low_rate.append(li_rate(city_data, city))

    return statistics.correlation(age_stand_hp, low_rate)


def order_by_ht_rate(city_data: dict) -> list[str]:
    """Return a list of the names of the neighbourhoods, ordered from lowest to
    highest age-standarised hypertension rate.

    >>> order_by_ht_rate(SAMPLE_DATA)
    ['Elms-Old Rexdale', 'Rexdale-Kipling', 'Thistletown-Beaumond Heights',\
 'West Humber-Clairville', 'Mount Olive-Silverstone-Jamestown']

    >>> order_by_ht_rate(SAMPLE_2)
    ['Bedford', 'Halifax', 'Sackville']

    >>> order_by_ht_rate(SAMPLE_3)
    ['Centre', 'Plato', 'Mile-End', 'Montreal']
    """

    age_stand_hp = []
    ordered_cities = []

    for city in city_data:
        age_stand_hp.append(get_age_standardized_ht_rate(city_data, city))
    age_stand_hp.sort()

    for value in age_stand_hp:
        for city in city_data:
            if get_age_standardized_ht_rate(city_data, city) == value:
                ordered_cities.append(city)
    return ordered_cities


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Uncomment when ready to test:
    # Using the small data files:
    small_data = {}
    # add hypertension data
    with open('../data/hypertension_data_small.csv') as ht_small_f:
        get_hypertension_data(small_data, ht_small_f)
    # add low income data
    with open('../data/low_income_small.csv') as li_small_f:
        get_low_income_data(small_data, li_small_f)

    print(small_data)
    print('Did we build the dict correctly?', small_data == SAMPLE_DATA)
    # print('Correlation in small data file:', get_correlation(small_data))

    # Using the example data files:
    example_neighbourhood_data = {}
    # add hypertension data
    with open('../data/hypertension_data_2016.csv') as ht_example_f:
        get_hypertension_data(example_neighbourhood_data, ht_example_f)
    # add low income data
    with open('../data/low_income_2016.csv') as li_example_f:
        get_low_income_data(example_neighbourhood_data, li_example_f)
    # print('Correlation in example data file:',
    #      get_correlation(example_neighbourhood_data))
