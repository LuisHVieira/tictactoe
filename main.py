from config import Config as c
from botComands import *

#path
path = "env/tokens.json"

c.getTokens(path)

c.runBot()