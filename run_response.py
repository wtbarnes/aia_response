__author__ = 'tdwilkinson'

from sunpy.instr.aia import Response
import matplotlib.pyplot as plt
import numpy as np
from astropy.table import Table, Column
import pandas as pd


path = '/Users/willbarnes/Documents/gsoc/aia_response/ssw_aia_response_data/'

# channel center and parameter list needed for loading in data
channel_list = [94, 131, 171, 193, 211, 304, 335] # TODO: fix to where 1600, 1700 works

# properties = ['wave', 'effarea', 'geoarea', 'platescale',
#               'numfilters', 'wavemin', 'wavestep', 'wavenumsteps', 'wavelog',
#               'usecontam', 'contamthick', 'elecperdn', 'elecperev',
#               'useerror', 'fp_filter', 'ent_filter', 'primary', 'ccd', 'contam', 'secondary']#,  'elecperphot'
#


r = Response(path_to_genx_dir=path, version = 6, channel_list=channel_list )
c = Response(path_to_genx_dir=path, version = 6, channel_list=channel_list)
p = Response(path_to_genx_dir=path, version = 'preflight', channel_list=channel_list)

    # Figure 2
    # test transmittance -- transmittance vs wavelength
    # # # #########################################################
for i in channel_list:
    plt.plot(r.get_wavelength_range(i), r.get_channel_data(i)['focal_plane_filter_efficiency'], linestyle='-')
    plt.xlim(0, 400, 1)
    plt.ylim(0.0, 0.6, .1)
plt.xlabel('Wavelength (A)')
plt.ylabel('Transmittance')
# plt.title('Filterwheel Filter calibration')
plt.show()                                                         # -Works: shows top



    # Figure 4
    # test reflectance - reflectance vs wavelength
    # ########################################################
for i in channel_list:
    reflectance = [j * k for j, k in zip(r.get_channel_data(i)['primary_mirror_reflectance'], r.get_channel_data(i)['secondary_mirror_reflectance'])]
    plt.plot(r.get_wavelength_range(i), reflectance)
    plt.xlim(50, 350, 1)
plt.xlabel('Wavelength (A)')
plt.ylabel('Reflectance (primary x secondary)')
plt.show()                                                           # -- Works!!



    # Figure 5
    # Effective area vs wavelength
    # ###################################
    #Plotted individualy
for i in channel_list:
    plt.plot(r.get_wavelength_range(i), r.effective_area(i, total_range = True), linestyle='-')
    plt.xlim(i - 20, i + 20, 1)
    plt.title(str(i))
    plt.xlabel('Wavelength (A)')
    plt.ylabel('Effective Area (cm**2) ')
    plt.show()


    # Subplots

for i in channel_list:

    index = channel_list.index(i)
    ylim = [[0, .4], [0, 1.5], [0, 3.], [0, 2.], [0, 1.5], [0, 0.08], [0, 0.05]]
    xlim = [[90, 100], [120, 140], [160, 180], [180, 210], [200, 220], [280, 320], [300, 360]]

    # EFFECTIVE AREA VS WAVELENGTH: V6 and comparison to eff_area from .genx
    eff_area = r.effective_area(i, total_range = True)
    Beff_area = c.effective_area(i, total_range = True, use_genx_effarea=True)
    ax = plt.subplot(2, 7, index + 1)
    ax.plot(r.get_wavelength_range(i), eff_area, color='blue', linestyle = '-')
    ax.plot(c.get_wavelength_range(i), Beff_area, color='red', linestyle='--')
    ax.set_xlim(xlim[index])
    # ax.set_ylim(ylim[index])
    ax.set_xticks([xlim[index][0], i, xlim[index][1]])
    ax.set_title(i)

    # PREFLIGHT
    ax = plt.subplot(2, 7, index + 8)
    peff_area = p.effective_area(i, total_range = True)
    ax.plot(p.get_wavelength_range(i), peff_area, color='green', linestyle='-')
    ax.set_xlim(xlim[index])
    # ax.set_ylim(ylim[index])
    ax.set_xticks([xlim[index][0], i, xlim[index][1]])
    ax.set_title(i)

print('V6:', eff_area)
print('genx:', Beff_area)
print('pre:', peff_area)
print('ratio: ', np.mean(peff_area) / np.mean(eff_area))

plt.tight_layout()
plt.show()                                                 # works




    # Figure 6
    #  Quantum efficiency! vs wavelength
    ########################################
for i in channel_list:
    plt.plot(r.get_wavelength_range(i), r.get_channel_data(i)['quantum_efficiency_ccd'])
plt.xscale('log')
plt.title('ccd')
plt.ylabel('Quantum Efficiency')
plt.xlabel('Wavlength (A)')
plt.show()                                                 # -- Works




    # Figure 7
    # Contamination
    # ########################################
for i in channel_list:
    plt.plot(r.get_wavelength_range(i), r.get_channel_data(i)['ccd_contamination'])
plt.ylim(0, 1, .2)
plt.xlim(0, 400., 100.)
plt.title('Reproduction:Figure 7')
plt.ylabel('Transmittance')
plt.xlabel('Wavlength (A)')
plt.show()                                                      # -- Works





    #Instrument response
    # print array of instrument response values - NOT a plot
    #######################################################
print( r.get_wavelength_response(94, use_response_table2=True))
print( r.get_wavelength_response(94, use_genx_values=True))
print( r.get_wavelength_response(94, use_calc_effarea_table2_gain=True))
print( r.get_wavelength_response(94))

for i in channel_list:
    print( i, 'boerner table2:  ', r.get_wavelength_response(i, use_response_table2 = True))
    print( i, 'all genx values: ', r.get_wavelength_response(i, use_genx_values=True))
    print( i, 'ef_tot div plsc: ', r.effective_area(i, total_range=True)[i] / r.get_channel_data(i)['plate_scale'])
    print( i, 'ef_l w/ table2G: ', r.get_wavelength_response(i, use_calc_effarea_table2_gain = True))
    print( i, 'ef_l w/ calc g:  ', r.get_wavelength_response(i))
