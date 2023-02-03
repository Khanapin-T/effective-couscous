import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Space_Corrected.csv')

#df.info()

'''ГИПОТЕЗА 1'''
#    'У компании (SpaceX) на счету (100) ракет. Из них большая часть в отставке (62)'
# inform = df[df['Company Name']=='SpaceX']['Status Rocket'].value_counts()
# inform.plot(kind = 'barh')
# plt.show()

'''ГИПОТЕЗА 2'''
#     'Компания (Boeing) - самая успешная. Среди всех запусков практически все миссии закончились успехом.'
#     'Однако компания (MHI) имеет более низкое соотношение (40) успехов / фэйлов.'
# inform2a = df[df['Company Name']=='Boeing']['Status Mission'].value_counts()
# inform2b = df[df['Company Name']=='MHI']['Status Mission'].value_counts()
# inform2a.plot(kind = 'barh')
# plt.show()

'''ГИПОТЕЗА 3'''
#     'В Казахстане распологалось две крупных компаний: (RVSN USSR) и (Roscosmos).'
#     'Преобладает компания (RVSN USSR)'
# temp = df[df['Location']=='Site 1/5, Baikonur Cosmodrome, Kazakhstan']['Company Name']
# temp = temp.to_frame()
# print(list(temp.columns))
# inform3 = temp['Company Name'].value_counts()
# inform3.plot(kind = 'barh')
# plt.show()

''' ДОПОЛНИТЕЛЬНО '''