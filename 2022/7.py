from aocd import data, submit
lines = data.splitlines()

path = ''  # keep track of current path
dirs = set()  # all directories in tree
files = {}  # full path -> size of file

for line in lines:
    if line == '$ cd ..':
        path = path.rsplit('/', 1)[0]
        continue
    if '$ cd' in line:
        folder = line.split(' ')[-1]
        path += '/' + folder
        dirs.add(path)
    elif line[:4] in ['$ ls', 'dir ']:
        continue
    else:
        size, name = line.split(' ')
        files[path + '/' + name] = int(size)

dirsizes = {}  # full path -> size of dir

for dir in dirs:
    for full_path, file_size in files.items():
        if (dir) in full_path:
            if dir in dirsizes:
                dirsizes[dir] += file_size
            else:
                dirsizes[dir] = file_size

p1 = sum(size for size in dirsizes.values() if size <= 100000)
submit(p1)

used = dirsizes['//']  # root
free = 70e6 - used
need = 30e6 - free

p2 = min(size for size in dirsizes.values() if size >= need)
submit(p2)
