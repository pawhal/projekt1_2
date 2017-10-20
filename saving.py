from main import base

with open(file, "w") as f:
    for key, val in sorted(base.items()):
        f.write(str(key) + " " + val + "\n")
print("saved")