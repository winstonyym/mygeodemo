# read version from installed package
from importlib.metadata import version
__version__ = version("mygeodemo")

from .mygeodemo import *