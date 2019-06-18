from matplotlib import pyplot
import pandas as pd

xls = pd.ExcelFile('./data_analysis_lab.xlsx')
df = pd.read_excel(xls, 'Data')

years = list(df['Годы'])
temp = list(df['Относит. температура'])
activity = list(df['Активность'])

pyplot.plot(years, activity, label='Активность солнца')
pyplot.plot(years, temp, label='Относит темп.')

pyplot.xlabel('Годы')
pyplot.ylabel('Темп/Активность')
pyplot.legend(loc='upper left')

pyplot.show()
