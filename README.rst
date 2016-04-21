********************************************************************************************************
aia_response: Calculate the *SDO/AIA* temperature response functions with SunPy and ChiantiPy
********************************************************************************************************
Here are some preliminary notes on implementing the AIA response functions with ChiantiPy and SunPy.
Currently, the only way to calculate these is with the routines provided in SSW. There is little
supporting documentation for these routines. **GOAL:** Implement AIA temperature response functions using the tools
provided by SunPy and ChiantiPy, providing adequate documentation and benchmarking.

We'll rely primarily on two papers for looking at the AIA response functions:

* `Boerner et al. (2012) <http://adsabs.harvard.edu/abs/2012SoPh..275...41B>`_
* `Boerner et al. (2014) <http://adsabs.harvard.edu/abs/2014SoPh..289.2377B>`_

Formalism
##########

For a given position in the image plane :math:`\mathbf{x}` and wavelength channel
:math:`i`, the pixel values can be expressed as,

.. math::
    p_i(\mathbf{x}) = \int^{\infty}_0\mathrm{d}\lambda\,\eta_i(\lambda)\int_{pixel\,\mathbf{x}}\mathrm{d}\theta\,I(\lambda,\theta)

Here, :math:`\eta_i(\lambda,t,\mathbf{x})` is the efficiency function of the :math:`i^{th}` channel.
It can be expressed as,

 .. math::
    \eta = A_{eff}(\lambda,t)G(\lambda)F(\mathbf{x})

* effective area :math:`A_{eff}=A_{geo}R_p(\lambda)R_S(\lambda)T_E(\lambda)T_F(\lambda)D(\lambda,t)Q(\lambda)`
* gain of the CCD-camera system, :math:`G(\lambda)=(12398/\lambda/3.65)g`
* flat field function :math:`F(\mathbf{x})`

According to `Boerner et al. (2012) <http://adsabs.harvard.edu/abs/2012SoPh..275...41B>`_,
the instrument response function is :math:`R(\lambda)=A_{eff}(\lambda,t)G(\lambda)`.
This should not be confused with the *wavelength response function* of `Boerner et al. (2014) <http://adsabs.harvard.edu/abs/2014SoPh..289.2377B>`_
:math:`R_i(\lambda)` which is equivalent to :math:`\eta_i` as expressed above.
