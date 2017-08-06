#
#  Arctic Key-Value store
#

from arctic import Arctic
from datetime import datetime as dt
import pandas as pd


# Connect to the mongo-host / cluster
mongo_host = "127.0.0.1 "
store = Arctic(mongo_host)

# Data is grouped into 'libraries'.
# Users may have one or more named libraries:
a = store.list_libraries()
print(a)

# Create a library
a= store.initialize_library('my_lib')


# Get a library
# library = m['username.<library>']
library = store['my_lib']

print(library)

# Store some data in the library
df = pd.DataFrame({'prices': [1, 2, 3]},
                  [dt(2014, 1, 1), dt(2014, 1, 2), dt(2014, 1, 3)])
print(df)
library.write('SYMBOL', df)
a = library.read('SYMBOL')
print("a", a)
library.append('SYMBOL', df)

# Read some data from the library
# (Note the returned object has an associated version number and metadata.)
a = library.read('SYMBOL')
print("a", a)
print("a.data", a.data)

# Store some data into the library
library.write('MY_DATA', library.read('SYMBOL').data)

# What symbols (keys) are stored in the library
a = library.list_symbols()
print("library.list_symbols()", a)

# Delete the data item
library.delete('MY_DATA')


# Other library functionality

# Store 'metadata' alongside a data item
library.write('MY_DATA', library.read('SYMBOL').data, metadata={'some_key': 'some_value'})
a = library.read('MY_DATA')
print("MY_DATA", a)

# Query avaialable symbols based on metadata
a = library.list_symbols(some_key='some_value')
print("library.list_symbols()", a)
a = library.list_symbols()
print("library.list_symbols()", a)

import pprint
# Find available versions of a symbol
a = list(library.list_versions('SYMBOL'))
print("list(library.list_versions('SYMBOL'))", a)

# Snapshot a library
#  (Point-in-time named reference for all symbols in a library.)
library.snapshot('snapshot_name')
a = library.list_symbols()
print("library.list_symbols()", a)

# Get an old version of a symbol
a = library.read('SYMBOL', as_of=1)
print("library.read('SYMBOL', as_of=1)", a)
# Geta version given a snapshot name

a = library.read('SYMBOL', as_of='snapshot_name')
print("library.read('SYMBOL', as_of='snapshot_name')", a)

# Delete a snapshot
library.delete_snapshot('snapshot_name')
a = library.list_symbols()
print("library.list_symbols()", a)

a = library.read('SYMBOL')
print("MY_DATA", a)