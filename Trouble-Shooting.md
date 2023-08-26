**Here is a collection of problems that might occur and how to potentially solve them. Please add new insights ;-)**

* On one of my maps the study experimentor overlay is not shown:
> Maybe the map overwrites the gamemode, open the ``World Settings`` on that map an check:<br>
    ![image](uploads/ccd972b6457aa6c348f9fc1df856be1a/image.png)<br>
     This should be ``None``

* There are weird characters in my csv Phase log files, e.g.:<br>
![image](uploads/9bfe9b5e7837180dec2719a41571cc88/image.png)
<blockquote>
Unreal produces byte order marks (BOM) for some reaseon (for possible solutions see #93), you can place and execute the following python code in the folder (``StudyFramework/StudyLogs``) where the phase csv files are:


```python
import os

def ConvertCoding(full_filename):
    #remove all the byte order marks that Unreal puts in there
    with open(full_filename, mode='r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        modified_lines = [line.lstrip('\ufeff') for line in lines]
    with open(full_filename, mode='w', encoding='utf-8') as file:
        file.writelines(modified_lines)

for filename in os.listdir("./"):
    if filename.endswith(".csv"): 
        print("Convert " + filename)
        ConvertCoding(filename)

```
</blockquote>