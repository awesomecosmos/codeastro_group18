def mass_galaxy(luminosity_galaxy, exponent_factor):
  '''
  This function calculates the mass of the galaxy, based on a mass-to-light ratio.
  
  Parameters
  ----------
  
  luminosity_galaxy: int
    luminosity of the object (units of solar luminosities)
    
  exponent_factor: int
    exponent factor (alpha) value (unitless) in the mass-to-light ratio (M/L = L**alpha)
  
  Returns
  -------
  
  mass_galaxy: int
    mass of the object in solar masses
 '''
  
  
  mass_galaxy = luminosity_galaxy**(exponent_factor+1)
  
  return mass_galaxy
