import functions_commands as fc
from config import Tokens as t

#path
path = "env/tokens.json"

t.getTokens(path)

fc.run(t.discord)