import re

pattern = re.compile(r"([a-zA-Z])")
string = 'search this inside of this text please! Nur'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.group(1))