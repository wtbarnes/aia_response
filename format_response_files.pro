PRO FORMAT_RESPONSE_FILES
	;SSW home directory
	ssw_home = '/Users/willbarnes/Documents/Rice/Research/ssw'
	;aia response data directory
	aia_response_dir = CONCAT_DIR(ssw_home,'sdo/aia/response/*.genx')
	;search directory
	aia_response_files = FILE_SEARCH(aia_response_dir)
	
	;directory to save new aia response files
	new_aia_response_dir = '/Users/willbarnes/Documents/Projects/gsoc/aia_response/ssw_aia_response_data'
	
	;loop through .genx files
	FOREACH file,aia_response_files DO BEGIN
		;print progress
		PRINT,'Processing file ',file
		;load save file with SSW restgen routine
		RESTGEN,file=file,struct=data
		;get bare .genx filename
		bare_file = FILE_BASENAME(file,'.genx')
		;save genx file as a normal idl save file
		SAVE,data,filename=CONCAT_DIR(new_aia_response_dir,bare_file)
	ENDFOREACH
END