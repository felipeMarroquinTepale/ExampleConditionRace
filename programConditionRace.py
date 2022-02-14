import threading
import time


precioIva = 0
def generateIva(precioTotal):
    global precioIva
    porcentaje_Iva = 16
    
    aumento = precioTotal *(porcentaje_Iva/100)
    precioIva_local= precioTotal + aumento

    time.sleep(0.1)
    
    precioIva = precioIva_local

    print(f'precio original= {precioTotal} y precio con Iva= {precioIva}')
    
  

if __name__ == "__main__":        
    #Creamos hilos
    hilo1 = threading.Thread(target=generateIva, args=(10,))
    hilo2 = threading.Thread(target=generateIva, args=(20,))
    #Iniciamos hilos
    hilo1.start()
    hilo2.start()
    #esperamos a que se completen los hilos
    hilo1.join()
    hilo2.join()   
   
    print(f'Precio con Iva final {precioIva}')




#En este programa, ambos hilos 1 y 2 intentan modificar el valor de la variable precioIva al mismo tiempo
#El valor de la variable precioIva depende de que hilo se complete en ultimo lugar

#Si  el hilo 1 se completa antes hilo 2, vera el siguiente resultado
#precio con iva = 11.6
#precio con iva = 23.2
#El ultimo precio con iva es 23.6

#De lo contrario, se vera lo siguiente:
#precio con iva = 23.2
#precio con iva = 11.6
#El ultimo precio con iva es 11.6

#ejecutar varias veces para  ver lo anterior