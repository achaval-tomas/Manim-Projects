## CSV to LINE GRAPH image visualization

Import a 2-column CSV file* by dragging it to the data folder (````mv oldpath/oldname.csv data/newname.csv````), then change **config.py's 'file'** value to **'newname.csv'**, you should also set each axis' label to match the new file's meaning and, optionally, play around with the remaining tweakable parameters in config.py. <br><br>
Run with ````manim main.py```` and an image of the line graph will be saved as ````media/images/main/CSVToLineGraph_*.png````
<br><br>
\* The file's rows should represent pairs of "x, y" values to be interpreted as (x, y) points on the plane. If you have a 2-row file (with many columns) of x-values and y-values, consider using [**this util to convert it**](https://github.com/achaval-tomas/Manim-Projects/blob/main/utils/turnRowsToCSVColumns.py).

### Graph generated for 'example2.csv':
![image](https://github.com/achaval-tomas/Manim-Projects/assets/134091945/4244ef21-8e27-4c7b-b065-3f008239d1e7)
