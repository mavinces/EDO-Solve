""" Aqui vamos a trabajar con diferentes metodos numericos para
 la solución de Ecuaciones diferenciales. En concreto trabajaremos con:
 1. Euler:          1 Orden
 2. Heun:           2. Orden
 3. Runge-Kutta4:   4 orden
 5. Runge-Kutta23:  2 y 3 orden
 6. Runge-Kutta45:  4 y 5 orden
 7. Runge-Kutta adaptativo (RKF - Rugen Kutta Fehlberg): 4 y 5 orden
 """

 # Solucion para ecuaciones por el método de Euler
def euler_method(f,x0,y0,h,n):
  print("Soy metodo de euler")
def euler_imp_method(f,x0,y0,h,n):
  print("Soy metodo de euler mejorado")
def euler_mod_method(f,x0,y0,h,n):
  print("Soy metodo de euler modificado")

 # Solucion para ecuaciones por el método Runge-Kutta
def runge_kutta2(f, x0, y0, h, n):
  print("Runge-Kutta de segundo orden")
def runge_kutta3(f, x0, y0, h, n):
  print("Runge-Kutta de tercer orden")
def runge_kutta4(f, x0, y0, h, n):
  print("Runge-Kutta de cuarto orden")
def runge_kutta45(f, x0, y0, h, n):
  print("Runge-Kutta-Fehlberg")
 
# Solucion para ecuaciones por el método Adam Bashforth
def adam_bashfort2(f, x0, y0, h, n):
  print("Adams-Bashforth de segundo orden")
def adam_bashfort3(f, x0, y0, h, n):
  print("Adams-Bashforth de segundo orden")
def adam_bashfort4(f, x0, y0, h, n):
  print("Adams-Bashforth de segundo orden")

met_seleccionado = int(input("Ingrese el método a utilizar (1 para Euler, 2 para RK4, etc.): "))
met_empleados = {
    1: ('Euler', euler_method),
    2: ('Euler mejorado', euler_imp_method),
    3: ('Euler modificado', euler_mod_method),
    4: ('Runge-Kutta de segundo orden', runge_kutta2),
    5: ('Runge-Kutta de tercer orden', runge_kutta3),
    6: ('Runge-Kutta de cuarto orden', runge_kutta4),
    7: ('Runge-Kutta-Fehlberg', runge_kutta45),
    8: ('Adams-Bashforth de segundo orden', adam_bashfort2),
    9: ('Adams-Bashforth de tercer orden', adam_bashfort3),
    10: ('Adams-Bashforth de cuarto orden', adam_bashfort4),
}

print("El método que se va a emplear será " + met_empleados[met_seleccionado][0] + ". ¿Está seguro? (Presione Enter para continuar)")
input()
