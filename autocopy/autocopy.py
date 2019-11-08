
import json
from shutil import copyfile
import time
from pathlib import Path
import datetime


#data = {
#    "Job": {
#        "sourcepath": "C:/Users/etienne.schmelzer/Desktop/Test1/A/test.xlsx",
#        "destpath": "C:/Users/etienne.schmelzer/Desktop/Test1/B/test.xlsx",
#    },
#}
#
#
#with open ("autocopy_settings.json", "w") as write_file:
#    json.dump(data, write_file, indent=4)



# settings file must be provided in the same Folder
sets = Path("autocopy_settings.json")

def get_filepaths(sets):
    """
    Extracts the file paths from the provided .json file and returns, the content of
    the .json file as a dictionary as well as a potential error message.
    """

    # Reading in the json file with the settings
    try:
        with open(sets, "r") as read_file:
            paths = json.load(read_file)
            error = ""
    except:
        paths = None
        error = "Error: autocopy_settings.json has not been provided or typo in json\n"
        print(error)
        #time.sleep(60)

    return paths, error

def copy_file(src, dst):
    """
    Copies the file from the sourcepath (src) to the destinationpath (dst).
    returns a message for the Log file.
    """
    try:
        copyfile(src, dst)
        message = "Successfully copied: {}\n".format(src)
        print(message)

    except:
        message = "Error: File could not be copied - maybe filepath incorrect?\n->{}\n->{}\n".format(src, dst)
        print(message)
        #time.sleep(60)

    return message


# Creating a timestamp for the Log file
datetime_object = datetime.datetime.now()
Log = "{} The Script started\n".format(datetime_object.strftime('%Y-%b-%d-%H:%M'))

# Getting the file paths and potential error message
paths, error = get_filepaths(sets)
# Appending potential error message to the Log file
Log = Log + error
# If the previous function returns paths == None - no paths can be extracted and the script finishes immediately
if paths != None:

    for key in paths:
        message = ""
        try:
            value = paths[key]
            src = value["sourcepath"]
            dst = value["destpath"]
            message = copy_file(src, dst)
            Log = Log + message

        except:
            message = "Error probably typo in settings.json concerning: {}".format(key)
            print(message)
            # Appending the Log with the exception message
            Log = Log + message


# Appending the date stamp to the Log file when the script finished
datetime_object = datetime.datetime.now()
Log = "{}The Script finished {}\n".format(Log, datetime_object.strftime('%Y-%b-%d-%H:%M'))
# Writing the Log to Log.txt in the same folder
with open('Log.txt', 'a') as the_file:
    the_file.write(Log)

# Print output for the console
print("\nThe Script has run successfully - Awesome\n")

print("""
                    Exterminate!
                   /
      _n__n__
     /       \===V==<D
    /_________\\
     |   |   |
    ------------               This script was
    |  || || || \+++----<(     written for Francois
    =============              by Etienne Schmelzer
    | O | O | O |
   (| O | O | O |\)
    | O | O | O | \\
   (| O | O | O | O\)
 ======================
""")

time.sleep(60)
exit()
