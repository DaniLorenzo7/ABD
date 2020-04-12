load data                                                                                                               
infile 'tabla_hotel.dat'                                                                                                
into table hotel                                                                                                        
(id_hotel position(1:4) integer external,                                                                               
localizacion position(6:35) char,                                                                                       
aforoMax position(37:39) integer external,                                                                              
eventos position(41:42) char,
director position(44:48) integer external)