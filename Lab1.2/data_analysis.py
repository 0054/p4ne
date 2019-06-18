from matplotlib import pyplot as plt
from openpyxl import load_workbook

plt.style.use('ggplot')

data = load_workbook('./data_analysis_lab.xlsx')['Data']


years = [x.value for x in data['A'][1:]]
temp = [x.value for x in data['C'][1:]]
activity = [x.value for x in data['D'][1:]]

plt.plot(years, temp, label='Относит. темп')
plt.plot(years, activity, label='Активность Солнца')

plt.xlabel('Годы')
plt.ylabel('Темп/Активн. Солнца')
plt.legend(loc='upper left')

plt.show()

