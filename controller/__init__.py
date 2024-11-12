import os
import glob

# to prevent manually adding filenames to tell app.py to execute 

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py" )]