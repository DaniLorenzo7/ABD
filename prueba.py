import numpy as np 
import random
import datetime

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
nombres = nombre_hombre+nombre_mujer
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

puestos = ["RECEPCIONISTA", "LIMPIEZA", "CAMARERO", "COCINERO", "CONSERJE", 
        "SEGURIDAD","CONTABLE", "MARKETING", "COMPRAS", "EVENTOS"]
pesos_puesto = [0.1, 0.2, 0.25, 0.05, 0.1, 0.05, 0.05, 0.05, 0.1, 0.05]

localizaciones = ["MADRID", "BARCELONA", "VALENCIA", "SEVILLA", "ALICANTE",
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

eventos_cocina=["SI", "NO"]
pesos_eventos=[0.3, 0.7]

pesos_cocina=[0.2,0.8]

tipos_habitaciones = ["INDIVIDUAL", "DOBLE", "TRIPLE", "TWIN", "SUITE"]
pesos_tipos_habitaciones = [0.3, 0.5, 0.05, 0.1, 0.05]


tipos_baños = ["DUCHA", "BAÑERA", "JACUZZI"]
pesos_tipos_baños = [0.45, 0.45, 0.1]

regimenes = ["ALOJAMIENTO", "DESAYUNO", "MEDIA PENSION", "PENSION COMPLETA", "TODO INCLUIDO" ]
pesos_regimenes = [0.35, 0.35, 0.15, 0.1, 0.05]

inicio = datetime.datetime(2017, 1, 1)
final =  datetime.datetime(2020, 1, 1)

random_date = inicio + (final - inicio) * random.random()
aux_date= str(random_date.day),"-",str(random_date.month),"-",str(random_date.year)
date= ''.join(aux_date)

j=0

################# PERSONAL #################
print("CREATE SEQUENCE sqc_personal INCREMENT BY 1 START WITH 1;")
while j<200:
    nombre = np.random.choice(nombres)
    apellido = np.random.choice(lista_apellidos)
    aux_puesto = random.choices(population=puestos, weights=pesos_puesto, k=1)
    puesto = ''.join(aux_puesto)
    salario = np.random.choice(salarios)
    
    print("INSERT INTO PERSONAL VALUES(sqc_personal.NEXTVAL, '",
        nombre,"','",apellido,"','",puesto,"',",salario,");"
        )

    j+=1



################# HOTEL #################
# while j<127:
#     localizacion = np.random.choice(localizaciones)
#     aux_aforo_max = random.randint(100,400)
#     aforo_max = str(aux_aforo_max)
#     aux_evento = random.choices(population=eventos_cocina, weights=pesos_eventos, k=1)
#     evento = ''.join(aux_evento)
#     director = random.randint(1,120)

#     print(localizacion,(20-len(localizacion))*" ",
#         aforo_max,12*" ",
#         evento,(15-len(evento))*" ",
#         director,(10-len(str(director)))*" "
#         )

#     j+=1



################# HABITACION #################
# id_hotel=0
# while j<6000:
#     id_hotel+=1
#     num_habitaciones=[20, 30, 40, 50, 60, 70, 80];
#     pesos_habitaciones=[0.1,0.15,0.2,0.2,0.2,0.1,0.05]
#     aux=random.choices(population=num_habitaciones, weights=pesos_habitaciones, k=1)
#     i=0
#     if (id_hotel==127):
#         aux[0]=6000-j
#     while (i<aux[0] and j<6000):
#         aux_tipo_habitacion = random.choices(population=tipos_habitaciones, weights=pesos_tipos_habitaciones, k=1)
#         tipo_habitacion= ''.join(aux_tipo_habitacion)
#         aux_tipo_baño = random.choices(population=tipos_baños, weights=pesos_tipos_baños, k=1)
#         tipo_baño = ''.join(aux_tipo_baño)
#         aux_cocina = random.choices(population=eventos_cocina, weights=pesos_cocina, k=1)
#         cocina = ''.join(aux_cocina)
#         print(tipo_habitacion,(15-len(tipo_habitacion))*" ",
#         tipo_baño,(10-len(tipo_baño))*" ",
#         cocina,12*" ",
#         id_hotel,(7-len(str(id_hotel)))*" "
#         )
#         i+=1
#         j+=1


################# RESERVA #################
# while j<12000:
#     aux_fecha_inicio = inicio + (final - inicio) * random.random()
#     aux_fecha_inicio_1= str(aux_fecha_inicio.day),"-",str(aux_fecha_inicio.month),"-",str(aux_fecha_inicio.year)
#     fecha_inicio= ''.join(aux_fecha_inicio_1)

#     duracion= random.randint(1,15)

#     aux_fecha_fin = aux_fecha_inicio + datetime.timedelta(days=duracion)
#     aux_fecha_fin_1= str(aux_fecha_fin.day),"-",str(aux_fecha_fin.month),"-",str(aux_fecha_fin.year)
#     fecha_fin= ''.join(aux_fecha_fin_1)

#     aux_regimen = random.choices(population=regimenes, weights=pesos_regimenes, k=1)
#     regimen = ''.join(aux_regimen)

#     id_habitacion = random.randint(1,6000)

#     print(id_habitacion, (7-len(str(id_habitacion)))*" ",
#         fecha_inicio,(15-len(fecha_inicio))*" ",
#         fecha_fin,(15-len(fecha_fin))*" ",
#         regimen,(15-len(regimen))*" ",
#         )

#     j+=1
