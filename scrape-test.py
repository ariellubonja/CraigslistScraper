from craigslistscraper import Searches

if __name__ == '__main__': # Required to run inside of "if name == main"

  filters = []#['&postedToday=1'] # Optional | Define your filters here

  cities = ['baltimore', 'philadelphia'] # Required | Define the cities you want to search

  # car_data=False by default and doesn't need to be defined explicitly.
  foo = Searches("macbook", cities, "sya", filters, car_data=False)

  foo.compile_search()
