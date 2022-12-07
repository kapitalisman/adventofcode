from aocd import data, numbers, submit
lines = data.splitlines()

files = {}
dirs = set()
path = ''

for line in lines:
    if line[0] == '$':
        if line == '$ cd ..':
            path = path.rsplit('/', 1)[0]
            continue
        if '$ cd' in line:
            folder = line.split(' ')[-1]
            if folder != '/':
                path += '/' + folder
                dirs.add(path)
    else:
        if line[:3] == 'dir':
            continue
        else:
            size, name = line.split(' ')
            files[path + '/' + name] = int(size)

dirsizes = {}
for dir in dirs:
    for full_path, file_size in files.items():
        if (dir) in full_path:
            if dir in dirsizes:
                dirsizes[dir] += file_size
            else:
                dirsizes[dir] = file_size

p1 = sum(size for size in dirsizes.values() if size <= 100000)
submit(p1)

used = sum(numbers)
free = 70e6 - used
need = 30e6 - free

p2 = min(size for size in dirsizes.values() if size >= need)
submit(p2)