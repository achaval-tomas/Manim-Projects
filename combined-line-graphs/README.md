## CSVs to COMBINED LINE GRAPH image visualization

Import as many 2-column CSV files* as you want by dragging them to the data folder (````mv oldpath/oldname.csv data/newname.csv````), then change **config.py's 'filenames'** array to include **'newname.csv'** for every file you wish to add, then select a color and scale factor for each function. You can also play around with other parameters to accomodate the graph to your style. <br><br>
Run with ````manim main.py```` and an image of the combined line graphs will be saved as ````media/images/main/CombinedGraphs_*.png````
<br><br>
\* Each file's rows should represent pairs of "x, y" values to be interpreted as (x, y) points on the plane. If you have a 2-row file (with many columns) of x-values and y-values, consider using [**this util to convert it**](https://github.com/achaval-tomas/Manim-Projects/blob/main/utils/turnRowsToCSVColumns.py).

### Graph generated for examples 1, 2 and 3, scaled and combined
![image](https://github.com/achaval-tomas/Manim-Projects/assets/134091945/c60146f8-5187-49f4-8059-44686dab083d)
