********************************************************************************************************
aia_response: Calculate the *SDO/AIA* temperature response functions with SunPy and ChiantiPy
********************************************************************************************************

Here are some preliminary notes on implementing the AIA response functions with ChiantiPy and SunPy.
Currently, the only way to calculate these is with the routines provided in SSW. There is little
supporting documentation for these routines.

**GOAL:** Implement AIA temperature response functions using the tools
provided by SunPy and ChiantiPy, providing adequate documentation and benchmarking.

We'll rely primarily on two papers for looking at the AIA response functions:

* `Boerner et al. (2012) <http://adsabs.harvard.edu/abs/2012SoPh..275...41B>`_
* `Boerner et al. (2014) <http://adsabs.harvard.edu/abs/2014SoPh..289.2377B>`_

.. figure:: aia_sample_data/aia_response_functions.png
   :scale: 100 %
   :alt: SDO/AIA temperature response functions

   SDO/AIA temperature response functions unnormalized (left) and normalized right for
   the six EUV channels as calculated by the aia_get_response function in SSW. The dashed lines
   are the response functions calculated with the Chianti correction as discussed in Boerner et al. (2014).

Formalism
##########

For a given position in the image plane :math:`\mathbf{x}` and wavelength channel
:math:`i`, the pixel values can be expressed as,

.. math::

    p_i(\mathbf{x})=\int_0^{\infty}\mathrm{d}\lambda\,\eta_i(\lambda)\int_{pixel\,\mathbf{x}}\mathrm{d}\theta\,I(\lambda,\theta)

Here, :math:`\eta_i(\lambda,t,\mathbf{x})` is the efficiency function of the :math:`i^{th}` channel.
It can be expressed as,

 .. math::\eta=A_{eff}(\lambda,t)G(\lambda)F(\mathbf{x})

The terms in the above equation are as follows,

* effective area :math:`A_{eff}=A_{geo}R_p(\lambda)R_S(\lambda)T_E(\lambda)T_F(\lambda)D(\lambda,t)Q(\lambda)`
* gain of the CCD-camera system, :math:`G(\lambda)=(12398/\lambda/3.65)g`
* flat field function :math:`F(\mathbf{x})`

According to `Boerner et al. (2012) <http://adsabs.harvard.edu/abs/2012SoPh..275...41B>`_,
the instrument response function is :math:`R(\lambda)=A_{eff}(\lambda,t)G(\lambda)` .
This should not be confused with the *wavelength response function* of `Boerner et al. (2014) <http://adsabs.harvard.edu/abs/2014SoPh..289.2377B>`_
:math:`R_i(\lambda)` which is equivalent to :math:`\eta_i` as expressed above.

With all of that out of the way, we want to calculate the *temperature response function*,
for the :math:`i^{th}` channel :math:`K_i(T)` . This can be expressed as,

.. math::K_i(T)=\int_0^{\infty}\mathrm{d}\lambda\,G(\lambda,T)R_i(\lambda)

Thus, we can calculate the AIA temperature response functions by folding the
instrument response function of through the contribution function :math:`G(\lambda,T)`
for the appropriate number of spectral lines.

Questions
#########
Some questions about how this will be implemented:

* How will we query the data related to the AIA instrument? (e.g. CCD gain, instrument decay, mirror efficiency, etc.)
* Where does this functionality belong in SunPy?
* What is the best way to get the atomic data from ChiantiPy?
* What amount of time should be spent making contributions to ChiantiPy?
