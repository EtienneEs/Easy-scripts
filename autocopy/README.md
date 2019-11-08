# Autocopy

[ > Setup ](#Setup)  
[_> How to make it an app/executable_](#Appmaker)
[ > How to Schedule Tasks on Windows ](#Schedule_Tasks)


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

## Autocopy_settings.json
The autocopy_settings.json contains the file paths necessary for the transactions.  
It allows you to create as many "Jobs" as you wish. The "Job" key is not necessary for the script but allows better 
trouble shooting. Please feel free to modify the autocopy_settings.json file.

````json
{
    "Job": {
        "sourcepath": "C:/Users/YourUsername/Desktop/Test1/A/test.xlsx",
        "destpath": "C:/Users/YourUsername/Desktop/Test1/B/test.xlsx"
    },
    "Job2": {
        "sourcepath": "C:/Users/YourUsername/Desktop/Test1/A/test.xlsx",
        "destpath": "C:/Users/YourUsername/Desktop/Test1/B/test.xlsx"
    }
}
````
## Log.txt
The Log file contains a Date and time stamp when the Script started and finished. All successfull transactions
as well as Errors are documented.

<a name="Appmaker"></a>

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

<a name="Schedule_Tasks"></a>

## How to Schedule Tasks on Windows
- Press Windows key and search for "Task Scheduler"
- Select Task Scheduler Library
- On the right side: "Create Task"
- Name your task
- Create a Trigger ( when your program will be run)
- Create an Action:
  - Action: "Start a program"
  - Browse to your script (make sure that autocopy_settings.json is in the folder as well)
  - recomended: put in your directory path to your .exe file in the "Start in (optional)" field.

Done - Make sure that it works by manually run it with right click on the schedule and __Run__.


.... How to schedule Tasks on Windows will be written soon ...


[1]: ../autocopy/autocopy.py
[2]: ../autocopy/autocopy_settings.json
