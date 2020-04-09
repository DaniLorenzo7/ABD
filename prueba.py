import numpy as np 
import random
from datetime import datetime

i=900.00;
salarios=[];
while i<3000.00:
    salarios.append(i);
    i+=50.00;

#print(np.random.choice(salarios))
#Selecciona un elemento aleatorio de la lista
nombre_hombre = ["ANTONIO", "JOSE", "MANUEL", "FRANCISCO", "DAVID",
            "JUAN", "JOSE ANTONIO", "JAVIER", "DANIEL", "JOSE LUIS", 
            "FRANCISCO JAVIER", "CARLOS", "JESUS", "ALEJANDRO", "MIGUEL",
            "JOSE MANUEL", "RAFAEL", "MIGUEL ANGEL", "PEDRO", "ANGEL", 
            "PABLO", "JOSE MARIA", "SERGIO", "FERNANDO", "LUIS", 
            "JORGE", "ALBERTO", "JUAN CARLOS", "ALVARO", "JUAN JOSE", 
            "ADRIAN", "DIEGO", "RAUL", "JUAN ANTONIO", "IVAN", 
            "ENRIQUE", "RUBEN", "RAMON", "OSCAR", "VICENTE", 
            "ANDRES", "JUAN MANUEL", "JOAQUIN", "SANTIAGO", "EDUARDO", 
            "VICTOR", "MARIO", "ROBERTO", "JAIME", "FRANCISCO JOSE"]
nombre_mujer = ["MARIA CARMEN", "MARIA", "CARMEN", "JOSEFA", "ANA MARIA", 
            "ISABEL", "MARIA PILAR", "MARIA DOLORES", "LAURA", "MARIA TERESA", 
            "ANA", "CRISTINA", "MARIA ANGELES", "MARTA", "FRANCISCA", 
            "ANTONIA", "MARIA ISABEL", "MARIA JOSE", "LUCIA", "DOLORES", 
            "SARA", "PAULA", "ELENA", "MARIA LUISA", "PILAR", 
            "RAQUEL", "ROSA MARIA", "CONCEPCION", "MANUELA", "MERCEDES", 
            "MARIA JESUS", "BEATRIZ", "JULIA", "ROSARIO", "NURIA", 
            "JUANA", "SILVIA", "TERESA", "ENCARNACION", "IRENE", 
            "ALBA", "PATRICIA", "MONTSERRAT", "ANDREA", "ROCIO", 
            "ROSA", "MONICA", "MARIA MAR", "ALICIA", "ANGELA"]

lista_apellidos = ["GARCIA", "GONZALEZ", "RODRIGUEZ", "FERNANDEZ", "LOPEZ",
                "MARTINEZ", "SANCHEZ", "PEREZ", "GOMEZ", "MARTIN",
                "JIMENEZ", "RUIZ", "HERNANDEZ", "DIAZ", "MORENO",
                "MUÑOZ", "ALVAREZ", "ROMERO", "ALONSO", "GUTIERREZ",
                "NAVARRO", "TORRES", "DOMINGUEZ", "VAZQUEZ", "RAMOS",
                "GIL", "RAMIREZ", "SERRANO", "BLANCO", "MOLINA",
                "MORALES", "SUAREZ", "ORTEGA", "DELGADO", "CASTRO",
                "ORTIZ", "RUBIO", "MARIN", "SANZ", "NUÑEZ",
                "IGLESIAS", "MEDINA", "GARRIDO", "CORTES", "CASTILLO",
                "SANTOS", "LOZANO", "GUERRERO", "CANO", "PRIETO",
                "CABRERA", "CAMPOS", "VEGA", "FUENTES", "CARRASCO",
                "DIEZ", "CABALLERO", "REYES", "NIETO", "AGUILAR",
                "PASCUAL", "SANTANA", "HERRERO", "LORENZO", "MONTERO",
                "HIDALGO", "GIMENEZ", "IBAÑEZ", "FERRER", "DURAN",
                "SANTIAGO","BENITEZ", "MORA", "VICENTE", "VARGAS"]

puesto = ["RECEPCIONISTA", "LIMPIEZA", "CAMARERO", "COCINERO", "CONSERJE", 
        "SEGURIDAD","CONTABLE", "MARKETING", "COMPRAS", "EVENTOS"]
pesos_puesto = [0.2, 0.1, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05]

localizacion = ["MADRID", "BARCELONA", "VALENCIA", "SEVILLA", "ALICANTE",
            "MALAGA", "MURCIA", "CADIZ", "VIZCAYA", "BALEARES", 
            "LA CORUÑA", "LAS PALMAS", "ASTURIAS", "TENERIFE", "ZARAGOZA",  
            "PONTEVEDRA", "GRANADA", "TARRAGONA", "CORDOBA", "GERONA", 
            "GUIPUZCOA", "ALMERIA", "TOLEDO", "BARAJOZ", "NAVARRA",  
            "JAEN", "CANTABRIA", "CASTELLON", "HUELVA", "VALLADOLID", 
            "CIUDAD REAL", "LEON", "LERIDA", "CACERES", "ALBACETE",  
            "BURGOS", "SALAMANCA", "LUGO", "ALAVA", "LA RIOJA", 
            "ORENSE", "GUADALAJARA", "HUESCA", "CUENCA", "ZAMORA",  
            "PALENCIA", "AVILA", "SEGOVIA", "TERUEL", "SORIA", "MELILLA", "CEUTA"]

aforo_max =[100,400]

eventos=["SI", "NO"]
pesos_eventos=[0.3, 0.7]

tipo_habitacion = ["INDIVIDUAL", "DOBLE", "TRIPLE", "TWIN", "SUITE"]
pesos_tipo_habitacion = [0.3, 0.5, 0.05, 0.1, 0.05]


tipo_baño = ["DUCHA", "BAÑERA", "JACUZZI"]
pesos_tipo_baño = [0.45, 0.45, 0.1]

inicio = datetime(2017, 1, 30)
final =  datetime(2017, 5, 28)

random_date = inicio + (final - inicio) * random.random()

print(random_date.day,"-",random_date.month,"-",random_date.year)
