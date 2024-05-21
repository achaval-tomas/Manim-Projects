## CSVs to COMBINED LINE GRAPH image visualization

Import as many 2-column CSV files* as you want by dragging them to the data folder (````mv oldpath/oldname.csv data/newname.csv````), then change **config.py's 'filenames'** array to include **'newname.csv'** for every file you wish to add, then select a color and scale factor for each function. You can also play around with other parameters to accomodate the graph and animation to your style.

Run with ````manim main.py```` and an image or animated video of the combined line graphs will be saved as ````media/<images or videos>/main/CombinedGraphs*````

\* Each file's rows should represent pairs of "x, y" values to be interpreted as (x, y) points on the plane. If you have a 2-row file (with many columns) of x-values and y-values, consider using [**this util to convert it**](https://github.com/achaval-tomas/Manim-Projects/blob/main/utils/turnRowsToCSVColumns.py).

Suggestion: Clone the repo and run the project with different configs to check how everything works before bringing in your own files.

### Graph animation generated for examples 1, 2 and 3, scaled and combined

https://github.com/achaval-tomas/Manim-Projects/assets/134091945/81fa9ad6-6be4-4410-a91d-1d85502517ae

The animation avobe is what should be generated if you execute ````manim main.py```` without modifying the cloned repository. Check ````config.py```` for options to create a static image as shown below.

### Graph image generated for examples 1, 2 and 3, scaled and combined
![image](https://github.com/achaval-tomas/Manim-Projects/assets/134091945/c60146f8-5187-49f4-8059-44686dab083d)
