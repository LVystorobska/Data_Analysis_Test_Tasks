import datetime
import random 
import pandas as pd

years_data = [2018, 2019, 2020, 2021]
cities_data = pd.read_csv('city_ua.csv')['city']
data_ranges = [300, 900, 2700]

def generate_date(start_year, end_year):
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def get_cities_list(iter_num, data):
    return list(data[:(3**iter_num)])


def generate_df_for_csv(df_raw, years, data_nums):
    generated_df = pd.DataFrame(columns=['departure-date', 'locality', 'order-number'])
    order_number = 0
    for ind, data_n in enumerate(data_nums):
        iter_n = (ind+1)
        cities = get_cities_list(3, df_raw)
        for i in range(data_n):
            random_index = random.randrange(0, (3**iter_n))
            to_append = [generate_date(years[ind], years[ind+1]), cities[random_index], order_number]
            a_series = pd.Series(to_append, index = generated_df.columns)
            generated_df = generated_df.append(a_series, ignore_index=True)
            order_number += 1
    return generated_df

df_new = generate_df_for_csv(cities_data, years_data, data_ranges)
df_new.to_csv('generated_locality.csv', index=False)