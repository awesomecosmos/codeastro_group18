# importing functions
from func_zeropoint import calibrated_apparent_magnitude
from func import distance_to_parsec
from func_kp import luminosity_calculator
from func_mass import mass_galaxy

# ask user to input galaxy data
photometric_band = input()
instrumental_magnitude = input()
zeropoint = input()
distance = input()


#step1. calculate the calibrated apparent magnitude galaxy
gal_calibrated_app_mag = calibrated_apparent_magnitude(instrumental_magnitude, zeropoint)

#step2. calculate the absolute magnitude of the galaxy
gal_abs_mag = distance_to_parsec(distance)

#step3. calculate the luminosity of the galaxy
gal_lum = luminosity_calculator(gal_abs_mag)


