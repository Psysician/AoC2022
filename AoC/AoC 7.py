from __future__ import annotations
import re

def parse_command(input_string, fs):
    command_pattern_cd_root = r"\$ cd \/$" # check
    command_pattern_cd_dots = r"\$ cd \.\.$" # check
    command_pattern_cd_string = r"\$ cd .*$" # check
    command_pattern_ls = r"\$ ls$" # check
    command_pattern_dir = r"dir .*$" # check
    command_pattern_file = r"(\d+) .*$" # check

    if re.match(command_pattern_cd_root, input_string):
        #print("Back to root")
        fs = fs.go_back()

    elif re.match(command_pattern_cd_dots, input_string):
        #print("Go one back")
        fs = fs.one_back()

    elif re.match(command_pattern_cd_string, input_string):
        #print("move in directory")
        fs = fs.cd(input_string[5:-1])
        print(fs)


    elif re.match(command_pattern_ls, input_string):
        print(fs.content)

    elif re.match(command_pattern_dir, input_string):
       # print("create dir")
        fs.add_directory(Directory(input_string[4:-1]))

    elif re.match(command_pattern_file, input_string):
        x = File(input_string[input_string.index(" "):-1], int(input_string[:input_string.index(" ")]))
        #print("create file\n", x)
        fs.add_file(x)

    return fs

# isinstance(file, File)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self):
        return f"name: {self.name} size: {self.size}"


class Directory:
    def __init__(self, name):
        self.name = name
        self.content:List[Union[Directory, File]] = []

    def add_directory(self, directory:Directory): # directory = Variablenname, Directory = Typ
        self.content.append(directory) # self = /, content = liste von ordnern oder datein in /, append = fts von oben
        directory.parent = self # elternteil von directory.parent/fts = "/"
        #

    def add_file(self, file:File):
        self.content.append(file)

    def calc_size(self):
        size = 0
        for f in self.content:
            if isinstance(f, File):
                size += f.size
            if isinstance(f, Directory):
                size += f.calc_size() #return mir die größe aller inhalte (z.b. 3000)

        return size




    def go_back(self):
        res = self
        while hasattr(res, "parent"):
            res = res.parent
        return res

    def go_back1(self):
        if hasattr(self, "parent"):
            return self.parent.go_back1()
        return self

    def one_back(self):
        if hasattr(self, "parent"):
            return self.parent
        return self

    def cd(self, name):
        for d in self.content:
            if isinstance(d, Directory):
                if d.name == name:
                    return d

        return self


    def __repr__(self):
        if hasattr(self, "parent"):
            return f"{self.parent}{self.name}/"
        return f"{self.name}"



def main():
    with open(r"C:\Users\praktikant_2\Downloads\AoC Six.txt") as f:
        lines = f.readlines()

    fs = Directory("/")

    for line in lines:
        fs = parse_command(line, fs)

    fs = fs.go_back()

    def f(d:Directory, sum):
        for e in d.content:
            if isinstance(e, Directory):
                if e.calc_size() <= 100000:
                    sum += e.calc_size()
                sum = f(e, sum)
        return sum

    print(fs)
    print(fs.calc_size())

    sum = f(fs, 0)

    print(sum)



if __name__ == "__main__":
    main()