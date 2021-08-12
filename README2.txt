This files contains instructions for mainScript2.py. Please refer to README.txt for more detail. I highly recommend using mainScript.py if you only need to combine 1 batch of files. 

v.1.1, last updated 8/12/2021

=== Author ===
These following programs are written by Angie Chen (angie.chen@cummins.com), in July-August 2021.
  - mainScript.py
  - script2.py
  - generateNames.py
  - mainScript2.py



=== Compatibility ===
See README.txt



=== Instructions ===
The file you will want to use is mainScript2.py. It is a modified version of mainScript.py and should be more automated and less specific progress updates.

Start by downloading mainScript2.py. Open up the python shell. Select File, Open, and find mainScript.py. A window named mainScript2.py should pop up. Ensure all your necessary files are in the same folder as the program (csv files, mainScript2.py, names.txt, files.txt).

Files.txt should be filled with the general name (ex. Users) in each line, with no other characters. Ensure there is no extra whitespace aside from the newlines.

Please note: files will be written in the format zNew-[files.txt line].csv. Files will be automatically overwritten if there is any with the same name. You can change the prefix (zNew-) in main by editing the variable PREFIX. Ensure the new name is in a string (enclosed in ' or ").

Either click F5 or select Run, then Run Module. The program will let you know once each file is created. Unlike mainScript.py, there will be no other status updates.



=== Known Bugs ===
See README.txt



== Background Information ==
This program takes the list of files written in files.txt and uses them to go through all the programs automatically. 

This is essentially the same as mainScript.py, except with less status updates and automates a bit more.

See README.txt for more details



=== Final Notes ===
You are free to reuse any portion of this program for any purpose WITHIN Cummins.



== Changelog ==
v.1.0: 8/10/2021 - uploaded program
v.1.1: 8/12/2021 - fixed and added details to exceptions