# Autocopy

[ > Setup ](#Setup)  
[_> How to make it an app/executable_](#appmaker)


## Aim
Copying files regularly from A to B using a scheduled windows executable.

## Summary
This small collection allows to create a small .exe which can be scheduled to
regularly copy files from A to B. A Log file will document successfull transactions and
report any errors which have occured.

<a name="Setup"></a>

## Setup:
- Install anaconda python 3.XX  
- Run [autocopy.py][1]

_Note: Please make sure that [autocopy_settings.json][2] file is provided side by side with [autocopy.py][1]. It contains the
necessary source and destination file paths. Please provide the correct paths._

<a name="appmaker"></a>

## How to make the script an app:
Install anaconda python 3.XX
open terminal/Command line and create the virtual environment:
```
conda create --name appmaker matplotlib pandas tk xlrd openpyxl pyinstaller
```
cd to the the directory of the python script and activate the virtual environment:
```
conda activate appmaker
pyinstaller --onefile scriptname.py
conda deactivate
```

The executable will be in the "dist" folder. 
If you would like to remove the virtual environment:
```
conda remove --name appmaker --all
conda info --envs
```




.... How to schedule Tasks on Windows will be written soon ...


[1]: ../master/autocopy/autocopy.py
[2]: ../master/autocopy/autocopy_settings.json
