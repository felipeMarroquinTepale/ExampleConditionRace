from threading import Thread, Lock
import time
#En este programa, ambos hilos 1 y 2 intentan modificar el valor de la variable precioIva al mismo tiempo
#El valor de la variable precioIva depende de que hilo se complete en ultimo lugar

#Si el hilo 1 se completa antes hilo 2, vera el siguiente resultado
#precio con iva = 11.6
#precio con iva = 23.2
#El ultimo precio con iva es 23.6

#De lo contrario, se vera lo siguiente:
#precio con iva = 23.2
#precio con iva = 11.6
#El ultimo precio con iva es 11.6

#ejecutar varias veces para  ver lo anterior


class Iva:
    def __init__(self):
        self.precioIva = 0
        self.lock = Lock()  #Creamos lock

    def generateIva(self,precioTotal):
        self.lock.acquire()     #Adquiere bloqueo
            
        porcentaje_Iva = 16    
        aumento = precioTotal *(porcentaje_Iva/100)
        precioIva_local= precioTotal + aumento

        time.sleep(0.1)
        self.precioIva = precioIva_local
        print(f'precio original= {precioTotal} y precio con Iva= {self.precioIva}')
        
        
        self.lock.release() #liberammos bloqueo una vez que el hilo termine de cambiar la variable compartida

       
  
if __name__ == "__main__":      
    iva = Iva()

    #Creamos hilos
    hilo1 = Thread(target=iva.generateIva, args=(10,))
    hilo2 = Thread(target=iva.generateIva, args=(20,))
    #Iniciamos hilos
    hilo1.start()
    hilo2.start()
    #esperamos a que se completen los hilos
    hilo1.join()
    hilo2.join()   
   
    print(f'Precio con Iva final {iva.precioIva}')
