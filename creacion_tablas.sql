CREATE TABLE PERSONAL                                                              
(id_personal NUMBER(5) CONSTRAINT personal_cp PRIMARY KEY,                         
nombre VARCHAR2(25),                                                               
apellidos VARCHAR2(50),                                                            
puesto VARCHAR2(20),                                                               
salario NUMBER(7,2));     


CREATE TABLE HOTEL                                                                 
(id_hotel NUMBER(4) CONSTRAINT hotel_cp PRIMARY KEY,                               
localizacion VARCHAR2(30),                                                         
aforoMax NUMBER(3),                                                                
eventos VARCHAR2(2),                                                               
director NUMBER(5),                                                                
CONSTRAINT hotel_cf_director FOREIGN KEY (director) REFERENCES PERSONAL(id_personal)); 


CREATE TABLE HORAS_TRABAJADAS                                                      
(id_personal NUMBER(5),                                                            
hotel NUMBER(4),                                                                
horas NUMBER(10),                                                                  
CONSTRAINT horasTrabj_cp PRIMARY KEY (id_personal, id_hotel));                     


CREATE TABLE HABITACION                                                            
(id_habitacion NUMBER(4) CONSTRAINT hab_cp PRIMARY KEY,                            
tipoHab VARCHAR2(15),                                                              
tipoBaño VARCHAR2(15),                                                             
cocina VARCHAR2(2),                                                                
hotel NUMBER(4),                                                                
CONSTRAINT habit_cp_hotel FOREIGN KEY (id_hotel) REFERENCES HOTEL(id_hotel));      


CREATE TABLE RESERVA                                                               
(id_reserva NUMBER(10),                                                            
hab NUMBER(4),                                                                  
fechaInicio DATE,                                                                  
fechaFin DATE,                                                                     
regimen VARCHAR2(20),                                                              
CONSTRAINT reserva_cp PRIMARY KEY (id_reserva),                                    
CONSTRAINT reserva_cf_hab FOREIGN KEY (id_hab) REFERENCES HABITACION(id_habitacion));

