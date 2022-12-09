#!/usr/bin/python3

with open("input.txt", "r") as f:
    puzzle_input = f.read()

io = puzzle_input.split("\n")


class File:
    def __init__(self, size):
        self.size = size


class Folder:
    def __init__(self, name, parent):
        self.files = []
        self.folders = []
        self.size = None
        self.parent = parent
        self.name = name

    def get_size(self):
        if self.size:
            return self.size
        self.size = 0
        for file in self.files:
            self.size += file.size
        for fold in self.folders:
            self.size += fold.get_size()
        return self.size

    def get_sub_folder_names(self):
        return [fold.name for fold in self.folders]

    def add_folder(self, fold):
        self.folders.append(fold)

    def add_file(self, fold):
        self.files.append(fold)


folders = []
cur_folder = Folder(None, None)

# Part 1
for row in io:
    _input = row.split(" ")
    if _input[0] == "$":
        if _input[1] == "ls":
            pass
        elif _input[1] == "cd":
            if _input[2] != "..":
                if len(folders) == 0:
                    cur_folder = Folder(_input[2], None)
                    folders.append(cur_folder)
                elif _input[2] in cur_folder.get_sub_folder_names():
                    for folder in cur_folder.folders:
                        if folder.name == _input[2]:
                            cur_folder = folder
            else:
                cur_folder = cur_folder.parent
    else:
        if _input[0] == "dir":
            if not _input[1] in cur_folder.get_sub_folder_names():
                tmp_folder = Folder(_input[1], cur_folder)
                tmp_folder.parent.add_folder(tmp_folder)
                folders.append(tmp_folder)
        else:
            file_size = int(_input[0])
            cur_folder.add_file(File(file_size))

total_1 = 0
for folder in folders:
    folder_size = folder.get_size()
    if folder_size <= 100000:
        total_1 += folder_size

print("Result Part 1:", total_1)

# Part 2
total_size = 70000000
target_unused = 30000000
used_space = folders[0].get_size()
space_to_free = target_unused - total_size + used_space

folder_sizes = []
for folder in folders:
    if space_to_free <= 0:
        break
    folder_size = folder.get_size()
    if folder_size >= space_to_free:
        folder_sizes.append(folder_size)

print("Result Part 2:", min(folder_sizes or [0]))
