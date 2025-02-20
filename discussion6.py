import csv
import unittest
import os


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    data = {}  # Dictionary to store the results

    with open(full_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row

        for row in reader:
            year, month, value = row  # Assume 3 columns: year, month, value

            if year not in data:
                data[year] = {}  # Create sub-dictionary for the year

            data[year][month] = value  # Store value as string (per instructions)

    return data

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    max_values = []

    for year, months in d.items():
        max_month = max(months, key=lambda m: int(months[m]))  # Find month with max value
        max_val = int(months[max_month])  # Convert to integer
        max_values.append((year, max_month, max_val))  # Store result as tuple

    return max_values
    pass

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    avg_values = {}

    for year, months in d.items():
        total = sum(int(value) for value in months.values())  # Convert and sum
        avg = round(total / len(months))  # Compute average and round
        avg_values[year] = avg  # Store in dictionary

    return avg_values
    pass

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
