#name:make_figures.py
#author:Will Barnes
#Description: make some figures useful to notes on AIA response functions

import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns

def display_aia_response_control_flow():
    """Show the control flow of the IDL programs used to compute AIA response functions"""

def plot_aia_response_functions(raw_response_file,fix_response_file):
    """Plot AIA temperature response functions as computed by SSW"""

    #Load data
    raw_tresp,fix_tresp = np.loadtxt(raw_response_file),np.loadtxt(fix_response_file)

    #set labels
    aia_labs = [r'$94\,\,\AA$',r'$131\,\,\AA$',r'$171\,\,\AA$',r'$193\,\,\AA$',r'$211\,\,\AA$',r'$335\,\,\AA$']

    #Create figure
    fig,ax = plt.subplots(1,2,figsize=(16,8))
    for i in range(1,7):
        #unnormalized
        ax[0].plot(10**raw_tresp[:,0],raw_tresp[:,i],linewidth=2,linestyle='-',color=sns.color_palette('deep')[i-1],label=aia_labs[i-1])
        ax[0].plot(10**fix_tresp[:,0],fix_tresp[:,i],linewidth=2,linestyle='--',color=sns.color_palette('deep')[i-1])
        #normalized
        ax[1].plot(raw_tresp[:,0],raw_tresp[:,i]/np.max(raw_tresp[:,i]),linewidth=2,linestyle='-',color=sns.color_palette('deep')[i-1])
        ax[1].plot(fix_tresp[:,0],fix_tresp[:,i]/np.max(fix_tresp[:,i]),linewidth=2,linestyle='--',color=sns.color_palette('deep')[i-1])

    #set plot options
    ax[0].set_xscale('log')
    ax[0].set_yscale('log')
    ax[0].set_xlim([10**5.,10**8.])
    ax[0].set_ylim([1e-28,1e-23])
    ax[1].set_xlim([5,8])
    ax[1].set_ylim([0,1])

    #labels
    ax[0].set_xlabel(r'$T\,\,\mathrm{(K)}$',fontsize=22)
    ax[0].set_ylabel(r'Temperature Response $(\mathrm{DN}\,\mathrm{cm}^{-5}\,\mathrm{s}^{-1}\,\mathrm{pix}^{-1})$',fontsize=22)
    ax[1].set_xlabel(r'$\log{T}\,\,\mathrm{(K)}$',fontsize=22)
    ax[1].set_ylabel(r'Normalized Temperature Response',fontsize=22)
    #legend
    ax[0].legend(loc='best',fontsize=14)

    plt.tight_layout()
    plt.savefig('figures/aia_response_functions.eps',format='eps')

if __name__=='__main__':
    plot_aia_response_functions('aia_sample_data/aia_tresponse_raw.dat','aia_sample_data/aia_tresponse_fix.dat')
