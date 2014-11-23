======
pyepw
======

Python EnergyPlus Weather File (EPW) Generator


**This is a work in progress, do NOT expect it to actually work!**

The aim of this project is to create Python data structures to read, modify and generate EPW files. The necessary data structures are generated by parsing a modified EPW idd file from the document Auxiliary EnergyPlus Programs - Extra programs for EnergyPlus, Date: November 22, 2013. 

Usage:
-----------

Reading data from an EPW file:
```python
    epw = EPW()
    epw.read(r"USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw")
```

Print the dry bulb temperature for every weather record:
```python
    for wd in epw.weatherdata:
        print wd.year, wd.month, wd.day, wd.hour, wd.minute, wd.dry_bulb_temperature
```
        
Modifying the dry bulb temperature for every weather record:
```python
    for wd in epw.weatherdata:
        wd.dry_bulb_temperature += 1.0
```

Creating an EPW File
```python
    epw.save(r"new_file.epw")
```

Notes:
-----------

The script to parse the IDD definitions and generate epw.py is located in the generator package. To read, modify and generate EPW files only epw.py need to be used. epw.py is generated by executing generator.main.py. It requires jinja2, autopep8 and docformatter.
