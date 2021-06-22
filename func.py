import numpy as np
from astropy import units as u

def distance_to_parsec(distance,input_unit=u.meter):
    """
    This function converts a distance  in units of UNIT to parsec.

    Parameters
    ----------
    
    distance : int
        Distance of object, in UNIT.
        
    input_unit : astropy.units.Quantity 
        Unit of input. Default is meter.
    
    Returns
    -------
    
    distance_pc : int
        Distance of object, in parsec.
        
    """
    distance_unit = distance * input_unit
    distance_pc = distance_unit.to(u.pc)
    return distance_pc

def absolute_magnitude_calculator(apparent_mag,distance,input_unit=u.meter):
    """
    This function calculates the absolute magnitude for an object, given its apparent magnitude and distance.

    Parameters
    ----------
    
    apparent_mag : int
        Apparent magnitude of object.
    
    distance : int
        Distance of object, in UNIT.
    
    Returns
    -------
    
    absolute_mag : int
        Absolute magnitude of object.
    """
    distance_pc = distance_to_parsec(distance,input_unit=u.meter)
    absolute_mag = apparent_mag - 2.5 * np.log((distance_pc.value / 10) **2 )
    return absolute_mag
