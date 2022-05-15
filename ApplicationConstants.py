import os
from inspect import getsourcefile
from os.path import abspath

BASE_PATH = os.path.split(abspath(getsourcefile(lambda: None)))[0].replace('\\', '/') + "/"
DATA_PATH = BASE_PATH + "data/"
