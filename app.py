from configparser import ConfigParser
  
configur = ConfigParser()
print (configur.read('config.ini'))
  
print ("Sections : ", configur.sections())
print ("General timeout : ", configur.getint('General','timeout'))
print ("System ssh_access : ", configur.getboolean('System','ssh_access'))
print ("Database ssh_accusernameess : ", configur.get('Database','username'))


import numpy as np
import pandas as pd
import pyarrow as pa

# df = pd.DataFrame({'one': [-1, np.nan, 2.5],
#                    'two': ['foo', 'bar', 'baz'],
#                    'three': [True, False, True]},
#                    index=list('abc'))

df = pd.DataFrame({'DEV': [{'timeout':configur.getint('General','timeout')},{'timeout':200} ,{'timeout':100}],
                   'TEST': [{'authentication_level':configur.getint('System','port')}, {'authentication_level':2}, {'authentication_level':3}],
                   'PROD': [{'endpoint':configur.get('General','endpoint')},{'endpoint':"https://test.nubeera.com"},{'endpoint':"https://prod.nubeera.com"}]},
                   index=list('abc'))


table = pa.Table.from_pandas(df)
import pyarrow.parquet as pq
pq.write_table(table, 'config.parquet')
table2 = pq.read_table('config.parquet', columns=['DEV','TEST','PROD'])

# from IPython.display import HTML
# print(table2.to_pandas().to_html())
# pd.set_option('max_colwidth', None)
###########           OR

def display_full(x):
    with pd.option_context('display.max_rows', None,
                           'display.max_columns', None,
                           'display.width', 2000,
                           'display.float_format', '{:20,.2f}'.format,
                           'display.max_colwidth', None):
        print(x)

display_full(table2.to_pandas())