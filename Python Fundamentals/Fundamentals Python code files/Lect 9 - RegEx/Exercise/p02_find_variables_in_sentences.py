import re

pattern = r"\b_{1}[A-Za-z]+\b"
text = input()
print(",".join(x[1:] for x in re.findall(pattern, text)))
