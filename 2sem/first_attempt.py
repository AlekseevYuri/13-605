#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp
#Подключение готовых частей программы
if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]
#Диапазон значений переменной
    mpp.plot(
#Вызов графика по имени mpp
        arguments,
        [math.exp(-0.1*a)*a*a  for a in arguments]
#Вычисление значений функции для каждого значения переменной и добавление их в график
    )
    mpp.show()
#Вывод графика на экран
