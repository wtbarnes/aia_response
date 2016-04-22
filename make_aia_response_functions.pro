PRO PLOT_AIA_TEMPERATURE_RESPONSE
  ;Calculate response functions
  raw_tresp = aia_get_response(/temp,/dn,/evenorm)
  ;Calculate response functions with chianti fix (see Boerner et al, 2014)
  fix_tresp = aia_get_response(/temp,/dn,/chiantifix,/evenorm)

  ;Reshape to matrix
  ;raw
  raw_tresp_mat = make_array(n_elements(raw_tresp.logte),6+1)
  ;put response functions and temperature in matrix
  raw_tresp_mat[*,0] = raw_tresp.logte
  raw_tresp_mat[*,1] = raw_tresp.a94.tresp
  raw_tresp_mat[*,2] = raw_tresp.a131.tresp
  raw_tresp_mat[*,3] = raw_tresp.a171.tresp
  raw_tresp_mat[*,4] = raw_tresp.a193.tresp
  raw_tresp_mat[*,5] = raw_tresp.a211.tresp
  raw_tresp_mat[*,6] = raw_tresp.a335.tresp
  ;chianti correction
  fix_tresp_mat = make_array(n_elements(fix_tresp.logte),6+1)
  ;put response functions and temperature in matrix
  fix_tresp_mat[*,0] = fix_tresp.logte
  fix_tresp_mat[*,1] = fix_tresp.a94.tresp
  fix_tresp_mat[*,2] = fix_tresp.a131.tresp
  fix_tresp_mat[*,3] = fix_tresp.a171.tresp
  fix_tresp_mat[*,4] = fix_tresp.a193.tresp
  fix_tresp_mat[*,5] = fix_tresp.a211.tresp
  fix_tresp_mat[*,6] = fix_tresp.a335.tresp

  ;Save data to file
  OpenW,lun,'aia_tresponse_raw.dat',/get_lun,width=1000
  printf,lun,transpose(raw_tresp_mat)
  free_lun,lun
  OpenW,lun,'aia_tresponse_fix.dat',/get_lun,width=1000
  printf,lun,transpose(fix_tresp_mat)
  free_lun,lun

  ;Plot parameters
  ;yrange0=1e-28
  ;;yrange1=1e-23

  ;Set up the display
  ;cgDisplay, 800, 700, Title='AIA Response Functions'
  ;;Plot the response functions--94,131,171,193,211,335 angstrom
  ;94 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a94.tresp,Color='Light Sea Green',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],$
  ;XTitle='log(T) (K)',YTitle='Temperature Response ['+raw_tresp.a94.units+']'
  ;131 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a131.tresp,Color='Sky Blue',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;171 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a171.tresp,Color='Goldenrod',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;193 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a193.tresp,Color='Orange',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;211 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a211.tresp,Color='Magenta',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;335 angstrom
  ;cgPlot,raw_tresp.logte,raw_tresp.a335.tresp,Color='Blue',Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;chianti correction from Boerner et al. (2014)
  ;94 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a94.tresp,Color='Light Sea Green',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;131 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a131.tresp,Color='Sky Blue',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;171 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a171.tresp,Color='Goldenrod',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;193 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a193.tresp,Color='Orange',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;211 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a211.tresp,Color='Magenta',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot
  ;335 angstrom
  ;cgPlot,fix_tresp.logte,fix_tresp.a335.tresp,Color='Blue',LineStyle=2,Thick=2,/YLog,XRange=[5,8],YRange=[yrange0,yrange1],/Overplot

END
