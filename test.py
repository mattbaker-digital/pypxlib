# Must remain compatible with python 2.7
import sys
import os
from pypxlib import Table

if __name__ == '__main__':
  # Print Python version and bitness
  print ('Python ' + \
          str(sys.version_info.major) + '.' + \
          str(sys.version_info.minor) + '.' + \
          str(sys.version_info.micro) + ' ' + \
          str(sys.maxsize.bit_length() + 1) + '-bit'
        )
  basePath = os.path.dirname(__file__) or '.'
  tablePath = os.path.join(basePath, 'test/resources/examples/CUSTOMER.DB')
  print(tablePath)
  table = Table(tablePath)
  fields = table.fields
  for fieldName in fields.keys():
    print(fieldName + ' : ' + str(table[0][fieldName]))
  table.close()