filename = "twl3.txt"
file_ = open(filename)
lines = []
for line in file_.readlines():
  lines.append(line.strip())
print(lines)

# From this point,you can do anything since the file is already read