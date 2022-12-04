import os
from solutions import one,two
if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    one.execute(script_dir)
    two.execute(script_dir)
