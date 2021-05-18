import matplotlib.pyplot as p
import pandas
import seaborn as sns
import math
from scipy import stats

df = pandas.read_csv('db.csv', sep=',')

data = df['Масса']
dfr = pandas.DataFrame(data)
print (dfr.describe())

print(stats.kstest(df['Масса'], 'norm', (df['Масса'].mean(), df['Масса'].std()), N=len(df)))#Анализируются только результаты, номера экспериментов сюда не попадают.

#Анализ распределения с помощью pandas и теста Колмогорова-Смирнова



#
#
#
if 1:
    D = 0

    for da in data:#Среднее
        D+=1/50*da

    delta = 0
    for da in data:#Среднеквадратичное отклонение
        delta += 1/50*((D-da)*(D-da))
    delta = math.sqrt(delta)
    print('Среднеквадратичное отклонение:')
    print (delta)

    gauss = [i for i in range (16400, 16750)]
    g = [i/10000 for i in range (16400, 16750)]
    for ii in range (0,len(gauss)):
        i = gauss[ii]
        gauss[ii]=1/(delta *math.sqrt(2*3.14))*math.exp(-(i/10000-D)*(i/10000-D)/(2*delta*delta))#Нормальное распределение
    
    
#Обработка данных, построение нормального распределения

#
#
#



    
p.subplot(1,2,1) #Cлева строится распределение масс деталек (kde) с отображением гистограммы
p.ylim(0,175)
p.xlim(1.63,1.68)
sns_plot = sns.distplot(data, kde = 1,color = 'green')
fig = sns_plot.get_figure()
p.title('Гистограмма и плотность')

p.subplot(1,2,2)    #Справа строится распределение Гаусса с дисперсией и ожиданием, полученными обработкой экспериментальных данных
p.ylim(0,175)
p.xlim(1.63,1.68)
p.plot(g,gauss,color = 'green')
p.title('Нормальное распределение')

p.show()

"""''''''"""
