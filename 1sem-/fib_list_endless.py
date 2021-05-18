import numpy
import itertools
spisok  = [1,1,2,3,5,8,13,21,34,55,89]
class el:    
  
    
    class _el_iter:

        def __init__(self):
            self.i = 0
            self.els = spisok
        def __next__(self):
            if self.i > 10:#Если список кончился, он продлевается при итерации.
                self.els +=[spisok[-1]+spisok[-2]]
                j = self.i
                self.i += 1
                return (str(self.i)+") "+str(self.els[j]))
            else:#eсли не кончился, двигаемся по нему
                j = self.i
                self.i += 1
                return (str(self.i)+") "+str(self.els[j]))
#Используется тот же код, что и в блокноте на сайте.            
    def __iter__(self):
        return el._el_iter()
n = 30 #Количество чисел.
f6 = el()

for i, f in zip(
    itertools.count(1),
    itertools.islice(f6, n)
):
    print(f)

