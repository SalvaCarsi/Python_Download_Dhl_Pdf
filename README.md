Phython_Download_Dhl_Pdf
========================

Contents of python utilies:

1- dhl_pdf_downloader_selenium_v2.py: script to download the order shipment pdf from the dhl file.

2- dhl_pdf_check_documents.py: checks if there were some files not downloaded.

3- rename_files.py: utility to rename the downloaded files and include the .pdf extension.

4- 20141106_SendungsnummernOriginal.csv: shipment numbers to download the pdf.

Instructions of use:

1- Create a folder "/home/dhl" and another "/home/dhl/download".

2- Scripts 1 and 2 need to be placed and runned from "/home/dhl"

3- Script 3 (if needed, is optional) neds to be placed and runned from "/home/dhl/download".

4- In a console execute: python dhl_pdf_downloader_selenium_v2.py

	The selenium script some times fails to execute and action. In that case perform this action manually in the browser and the script will continue. 
	In case it stops go to the download folder, check the last downloaded file and remove this and all the previous files from the file 20141106_SendungsnummernOriginal.csv. And re execute the script again.

5- In a console execute: dhl_pdf_check_documents.py
	
	In case some files are missing download them manually

6- In case the files doesnt have the desired extension you can run: python rename_files.py
