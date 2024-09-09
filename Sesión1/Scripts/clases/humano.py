"""
Script para hacer la clase humano con:
Atributos: 
- nombre: [str]
- apellido_paterno: [str]
- apellido_materno: [str]
- año_nacimiento: [int]
- mes_nacimiento: [int]
- dia_nacimiento: [int]
"""

from datetime import date # esta librería nos va a ayudar al cálculo de Edad más adelante

class humano: # siempre después de 2 puntos va un indent en la siguiente línea, vsc los pone automáticamente
    
    def __init__(self, n=None, ap=None, am=None, año=None, mes=None, dia=None): # método para inicializar el objeto (cuando alguien define un objeto tipo humano qué es lo que debe mandar)
        self.nombre = n  # en self estamos utilizando el objeto mismo de esta clase
        self.apellido_paterno = ap
        self.apellido_materno = am
        self.año_nacimiento = año
        self.mes_nacimiento = mes
        self.dia_nacimiento = dia

    # nota: en los métodos podemos seguir definiendo atributos en el objeto self, estos primeros son los necesarios para generar el objeto

    # MÉTODOS
    def calculaEdad(self): # para hacer una función, utilizamos el comando def y también va a llevar : al final del paréntesis con su respectivo indent
        # en este caso, como todos los elementos para calcular Edad están "dentro" del objeto, no necesitamos mandar nada más a la función
        # obtenemos el día de hoy como referencia para el cálculo de edad
        hoy = date.today()
        años_edad = hoy.year - self.año_nacimiento
        meses_edad = hoy.month - self.mes_nacimiento
        dias_edad = hoy.day - self.dia_nacimiento
        if dias_edad < 0:
            dias_edad = 30 + dias_edad
            meses_edad = meses_edad - 1
        if meses_edad < 0:
            meses_edad = 12 + meses_edad
            años_edad = años_edad - 1

        edad = "La edad de {} es de {} años, {} meses y {} días".format(self.nombre, años_edad, meses_edad, dias_edad)

        return edad # todas las funciones puede tener o no un return y pueden regresar varios elementos así return elemento_1, elemento_2, elemento_3, ..., elemento_n

