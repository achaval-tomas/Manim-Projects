## CSV to LINE GRAPH image visualization

Import a 2-column CSV file* by dragging it to the data folder (````mv oldpath/oldname.csv data/newname.csv````), then change **config.py's 'file'** value to **'newname.csv'**, you should also set each axis' label to match the new file's meaning and, optionally, play around with the remaining tweakable parameters in config.py. <br><br>
Run with ````manim main.py```` and an image of the line graph will be saved as ````media/images/main/CSVToLineGraph_*.png````
<br><br>
\* The file's columns should represent pairs of "x, y" values to be interpreted as (x, y) points on the plane.

### Graph generated for 'example2.csv':
![image](https://github.com/achaval-tomas/Manim-Projects/assets/134091945/4244ef21-8e27-4c7b-b065-3f008239d1e7)
