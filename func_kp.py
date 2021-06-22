import numpy as np 

def luminosity_calculator(abs_mag): 
  '''
  This function calculates the luminosity of an object given its absolute magnitude. 
  
  Parameters
  ----------
  
  abs_mag: int
    absolute magnitude of an object 
  
  Returns
  -------
  
  luminosity: int
    luminosity of an object in Watts
  
 '''
  #constants
  luminosity_sun = 3.68e26 #Watts
  abs_mag_sun = 4.83
  
  return luminosity_sun * 10**((abs_mag_sun - abs_mag) / 2.5) 
