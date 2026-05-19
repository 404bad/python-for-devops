# instead of only printing,, logs are essential in production systems

import logging

logging.basicConfig(level=logging.ERROR)

try:
    x=10/0

except ZeroDivisionError as e:
    logging.error(e)


