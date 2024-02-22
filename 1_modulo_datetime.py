# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone


# data = datetime(2024, 2, 20)
# print(data)

# data = datetime(2024, 2, 20, 13, 37, 23)
# print(data)

# data_str_data = '2024-02-20 13:37:23'
# # data_str_data_br = '12/02/2024 13:37:23' # '%d/%m/%Y %H:%M:%S'
# data_str_formato = '%Y-%m-%d %H:%M:%S'

# data = datetime.strptime(data_str_data, data_str_formato)
# print(data)

data = datetime.now(timezone('Asia/Tokyo'))
print(data)

data = datetime(2024, 2, 20, 13, 37, 23, tzinfo=timezone("Asia/Tokyo"))
print(data)

print(data.timestamp())
print(datetime.fromtimestamp(1708402703.0))
