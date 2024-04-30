from multiprocessing import Pool
import time

def example(x):
    print("Process "+str(x)+" starting...")
    time.sleep(1)
    print("Process "+str(x)+" finished!")

#Chronimy punkt wejscia do programu - multiprocessing na Windows dziala poprzez import programu jako modul - nie chcemy, aby kazdy proces od nowa wykonywal caly kod.
#Na Linuxie nie jest to konieczne, poniewaz Linux jest dobrym systemem.
if __name__ == '__main__':

    #Tworzymy ProcessPool z maksymalna liczna 4 watkow.
    with Pool(4) as processPool:
        
        #Wykonujemy obliczenia, na przyklad za pomoca funkcji map() - zarzadzanie procesami odbywa sie w pelni automatycznie.
        processPool.map(example, range(10))
