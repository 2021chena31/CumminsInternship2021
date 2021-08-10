This files contains instructions for mainScript.py only.
v.1.1, last updated 8/10/2021

=== Author ===
These following programs are written by Angie Chen, in July-August 2021.
  - mainScript.py
  - script2.py
  - generateNames.py
  - mainScript2.py



=== Compatibility ===
This Python file currently is known to be compatible with version 2.6.6, but any version 2.x is likely to work. It is unknown if this code is compatible with Python version 3.x. However, it should probably work if you replace all 'raw_input()' with 'input()' 



=== Instructions ===
The file you will want to use is mainScript.py. It is the combined version of both script2.py and generateNames.py, but with additional comments and detailed error messages.

Start by downloading mainScript.py. Open up the python shell. Select File, Open, and find mainScript.py. A window named mainScript.py should pop up. Ensure all your necessary files are in the same folder as the program (csv files, mainScript.py, names.txt).

Please note-- temp.csv is the default name for the combined. If you don't delete temp.csv after it is created, the program will ask you to input a new name. Any name you input will overwrite any previous files, if they are present in the folder. 

Either click F5 or select Run, then Run Module. The program should prompt you for information as necessary and give you progress updates.



=== Known Bugs ===
  - If two columns have the same data up to a certain point, but one is shorter before the point (ex. 1,2,3,4 and 1,2,3), then then one that comes later will not be added no matter the length.



== Background Information ==
(This is just a rundown of how the program works)

This program works by converting all necessary tables into .csv files, then reading the .csv files, adding all the data into a dictionary, then writing all the dictionary data into a new .csv file.

All tables to be combined need to be exported as a csv file and share the same formating of data. My program works under the assumption that the file name for each csv file is the same, save for the ending of the file which should follow the format of: (file source initial).csv. For example, varWarrantyGensetPricesPSO.csv (varWarrantyGensetPrices in the PowerSouth database). Suffixes can be changed, as long as the code is edited to reflect that-- check sList in main. 

Due to the nature of .csv files, all headings are unfortunately lost. 

A dictionary was chosen because it uses a hashtable, and therefore should be faster than using a list to store and check for duplicates. The key for each row is chosen to be column 0, with the entry being the rest of the column. As the entire sheet may share a single key, the entry will be stored as a nested list, the first list being the duplicate keys and the second being a list of all the columns in the row.

In the function call for addDict() in main, you are able to edit the keyIndex (defaulted to 0). Please note that I have not tested to see if it works, and the data is probably small enough that even if all the file share the same key, it won't take more than half a minute.

This file is a combination of two programs, both ran seperately during testing, which is why names.txt is needed. If you want, you could change the code so that names.txt is not required for use. 


=== Final Notes ===
The code is honestly a mess, but I added as much detail as I could so it should hopefully be comprehensible. Feel free to made any edits/share the code, but be sure to make a backup of the current version just in case.

In all honestly, I would recommend creating a new program in Python version 3 that makes use of the pyodbc module. 


== Changelog ==
v.1.0: 8/9/2021 - uploaded program
v.1.1: 8/10/2021 - changed some comments (should not impact program)