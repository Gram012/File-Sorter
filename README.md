# File-Sorter
File Sorter for the Wang Group at the University of Minnesota Twin Cities.
All uploads should be approved by a current lab member.

Some things to note:
* To use locally, you must first change the path name to that of the folder you are organizing. 
* This script works by identifying 'M_n' in the file name, where n is an integer between 199 and 512 indicating the measurement number. 
for example, and files corresponding to the 214th measurement should have 'M_214...' in the title.
* It creates an individual folder for each measurement, copies any files with 'M_n' in the name into the 'M_n' folder and then deletes them from the main path. 
