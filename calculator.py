# importing functions
import numpy as np
from astropy.io import ascii
import pandas as pd
from func_zeropoint import calibrated_apparent_magnitude
from func import distance_to_parsec
from func_kp import luminosity_calculator
from func_mass import mass_galaxy

def calculator(table):
    '''
    This function reads in the given data to perform all the calculations. 

    Parameters
    ----------
    table: str
        table containing 
    '''
    data = ascii.read(table)
    df = data.to_pandas()
    print(df)
    object_id = df['id']
    band = df['band']
    inst_mag = df['m']
    delta_zp = df['delta_zp']
    z = df['z']
    dist_l = df['d_l']
    
    '''
    #step1. calculate the calibrated apparent magnitude galaxy
    gal_calibrated_app_mag = calibrated_apparent_magnitude(inst_mag, delta_zp)

    #step2. calculate the absolute magnitude of the galaxy
    gal_abs_mag = distance_to_parsec(dist_l)

    #step3. calculate the luminosity of the galaxy
    gal_lum = luminosity_calculator(gal_abs_mag)

    #step4. calculate the mass of the galaxy
    gal_mass = mass_galaxy(gal_lum, exponent_factor)
    '''


    
calculator('table.txt')
# # ask user to input galaxy data
# photometric_band = input()
# instrumental_magnitude = input()
# zeropoint = input()
# distance = input()
# exponent_factor = input()

# #step1. calculate the calibrated apparent magnitude galaxy
# gal_calibrated_app_mag = calibrated_apparent_magnitude(instrumental_magnitude, zeropoint)

# #step2. calculate the absolute magnitude of the galaxy
# gal_abs_mag = distance_to_parsec(distance)

# #step3. calculate the luminosity of the galaxy
# gal_lum = luminosity_calculator(gal_abs_mag)

# #step4. calculate the mass of the galaxy
# gal_mass = mass_galaxy(gal_lum, exponent_factor)

# np.savetxt('galaxy_mass_out.table', gal_mass)



