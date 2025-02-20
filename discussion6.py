import csv
import unittest
import os

def load_csv(f):
    '''
    Params: 
        f, name or path of CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    '''
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    data = {}  # Dictionary to store results

    with open(full_path, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # First row contains year headers

        years = headers[1:]  # Extract year headers (excluding "Month")
        
        for year in years:
            data[year] = {}  # Initialize dictionary for each year
        
        for row in reader:
            month = row[0]  # First column is the month name
            values = row[1:]  # Remaining columns are values for each year
            
            for i, year in enumerate(years):
                data[year][month] = values[i]  # Store values as strings (per instruction)

    return data

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: (year, month, max_value) 
    '''
    max_values = []

    for year, months in d.items():
        if not months:  # Skip years with no data
            continue

        max_month = max(months, key=lambda m: int(months[m]))  # Find month with max value
        max_val = int(months[max_month])  # Convert to int
        max_values.append((year, max_month, max_val))  # Store as tuple

    return max_values

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and values are floats rounded to nearest whole number
    '''
    avg_values = {}

    for year, months in d.items():
        if not months:  # Skip years with no data
            continue

        total = sum(int(value) for value in months.values())  # Convert to int and sum
        avg = round(total / len(months))  # Compute average and round
        avg_values[year] = avg  # Store in dictionary

    return avg_values

class dis7_test(unittest.TestCase):
    '''
    You should not change these test cases!
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
