def mass_galaxy(luminosity_galaxy, exponent_factor):
  """
  This function calculates the mass of the galaxy, based on a mass-to-light ratio.
  The unit of the luminosity of the galaxy is solar luminosities (L_solar).
  The unit of the mass of the galaxy is solar mass (M_solar).
  The exponent factor is unitless.
  """
  
  mass_galaxy = luminosity_galaxy**(exponent_factor+1)
  
  return mass_galaxy
