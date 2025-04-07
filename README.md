# Getting started with MetaChecklist

1. Download the above files as a zip file (' <> Code' button, upper right - > download ZIP)
2. Make a folder in your documents folder called 'Meta analysis data' (or similar). Copy the downloaded zip file into this folder and unzip it.

   Your folder should have the structure: `User\Documents\Meta analysis data\meta-characterisation-main`

   with the `meta-characterisation-main` folder containing various `.py` files

3. Launch Jupyter Notebook, and navigate to your folder `User\Documents\Meta analysis data`. Make a new Jupyter notebook in this folder.
4. Enter the following and run the cell:

  ```%matplotlib nbagg
import sys
import pandas as pd

sys.path.append("meta-characterisation-main")
from MetaChecklist import MetaChecklistTab

meta = MetaChecklistTab(test=False)
meta.tab

```



# Further information

Apologies for the current absence of comments, instructions, or docstrings within the code - I'll try to add these in the near future!

For further information and help, feel free to contact: liam.bird@eng.ox.ac.uk
