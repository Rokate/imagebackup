from pathlib import Path

all_file = []
files = Path('/home/runner/work/imagebackup/imagebackup/aomen').rglob('*.*')
print(Path(__file__))
for file in files:
    if Path.is_file(file):
        all_file.append(file)

print(len(all_file))
