def calibrated_apparent_magnitude(instrumental_magnitude, zeropoint):
  
  '''
  This function calculates the calibrated apparent magnitude of an object,
  given its measured instrumental magnitude and a zeropoint correction 
  from standard stars in the field. 
  
  Parameters
  ----------
  
  zeropoint: int
    zeropoint correction from observations of standard stars in the field 
  
  instrumental_magnitude: int
    measured instrumental magnitude of the object
  
  Returns
  -------
  
  calibrated_apparent_magnitude: int
    calibrated apparent magnitude of the object
 '''
  
  calibrated_apparent_magnitude = zeropoint + instrumental_magnitude
  
  return calibrated_apparent_magnitude
