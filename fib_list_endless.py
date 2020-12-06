import numpy
import itertools
spisok  = [1,1]
class el:    
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""
    
    class _el_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.els = spisok # они у нас выше были
        def __next__(self):
            if self.i>=n:
                print("DONE!")
                raise StopIteration()
            else:
                if self.i >= 2:#Если список кончился, он продлевается при итерации.
                    self.els +=[spisok[-1]+spisok[-2]]
                    j = self.i
                    self.i += 1
                    return (str(self.i)+") "+str(self.els[j]))
                else:
                    j = self.i
                    self.i += 1
                    return (str(self.i)+") "+str(self.els[j]))
#Используется тот же код, что и в блокноте на сайте.            
    def __iter__(self):
        """Создать и вернуть итератор"""
        return el._el_iter()
n = 10
e = el()
for w in e:
    print( w)

