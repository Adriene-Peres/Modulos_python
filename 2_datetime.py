# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# istalar pip python-dateutil types-python-dateutil
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = timedelta(days=10, hours=2)
print(data_fim - delta)
print(data_fim + relativedelta(seconds=60, minutes=10))

delta = relativedelta(data_fim, data_inicio)
print(delta)


# delta = data_fim - data_inicio

# print(delta.days, delta.seconds)
# print(delta.total_seconds())

# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)
