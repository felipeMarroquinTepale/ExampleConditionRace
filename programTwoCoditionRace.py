import threading
import requests

#Ejecutar varias veces  para ver lo siguiente
# Se crean dos hilos t1 y t2 en la función main_task y la variable global usuariosViendo se establece en 0.
# Cada hilo tiene una función objetivo tarea hilo en la que la función de incremento_personas se llama 100000 veces para simular las personas que veran los datos de la peticion
# La función de incremento_personas incrementará la variable global usuariosViendo en 1 en cada llamada.
# El valor final esperado de usuarioViendo es 200000 pero lo que obtenemos en 10 iteraciones de la función main_task son algunos valores diferentes.

# Esto sucede debido al acceso simultáneo de hilos a la variable compartida usuariosViendo. El valor de usuariosViendo no se puede prever y esto es más que una condición de carrera.

usuariosViendo = 0 #variable global usuariosViendo para simular al numero de usuarios que veran los datos de la peticion

def incremento_personas():
	"""
	función para incrementar la variable global x cada vez que hace una
	"""
	global usuariosViendo  #Numeros de usuarios que veran los datos de la peticion
	usuariosViendo += 1    
       

def tarea_hilo():	
	# tarea para el metodo 
	# llama a la funcion de incremento_personas 100000 veces cada que hay una respuesta correcta en la peticion
	
    res = requests.get('https://www.youtube.com/')
    if res.status_code == 200: #Respuesta correcta en la peticion
        
	    for _ in range(100000):	
		    incremento_personas()
        

def main_task():
	global usuariosViendo
	# Establece la variable global x a 0
	usuariosViendo = 0

	# Creando hilos
	t1 = threading.Thread(target=tarea_hilo)
	t2 = threading.Thread(target=tarea_hilo)
	# comienza hilos
	t1.start()
	t2.start()
	# espera hasta que los hilos terminen su trabajo
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteracion",i," personas viendo = ",usuariosViendo)
