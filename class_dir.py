import sys
class commandline:
    def __init__(self):
        self.command_pipe=[]
        self.dir=[]
        self.command=""
    def command_input(self):
        self.command = input(self.user_position())
        if self.command[:2] == "cd":
            if self.command[-2:] == ".." and self.command_pipe:
                self.command_pipe.pop()
            elif self.command[3:] == "~":
                self.command_pipe = []
            elif self.command[3:] in self.dir:
                self.command_pipe.append(self.command[3:])
            else:
                pass
        elif self.command == "ls":
            if self.command_pipe:
                temp_dir = "cd "
                for dir in self.command_pipe:
                    temp_dir = temp_dir + dir + "/"
                temp_dir = temp_dir + ";ls"
                self.command = temp_dir
        elif self.command == "clear":
            sys("cls");

    def file_read(self):
        temp="cd "
        for i in self.command_pipe:
            temp+=(i+"/")
        temp+=";ls"
        return temp
    def user_position(self):
        temp="~"
        for i in self.command_pipe:
            temp+=("/"+i)
        temp+=" $"
        return temp


