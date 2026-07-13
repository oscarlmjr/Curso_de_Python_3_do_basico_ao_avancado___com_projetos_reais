import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''


# Positive lookahead
pprint(re.findall(r'.+', texto))
print()
pprint(re.findall(r'(?=.*inactive).+', texto))
print()
pprint(re.findall(r'(?=.*active).+', texto))
print()
pprint(re.findall(r'(?=.*[^in]active).+', texto))

# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
# # Positive lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
# # Negative lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# print(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
