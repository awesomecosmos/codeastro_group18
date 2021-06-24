def calibrated_apparent_magnitude(instrumental_magnitude, zeropoint):
  """ 
  This function takes a measured instrumental magnitude, \
  and a zeropoint correction from standard stars in the fild \
  and outputs the calibrated apparent magnitude.
  """
  calibrated_apparent_magnitude = zeropoint + instrumental_magnitude
  
  return calibrated_apparent_magnitude
