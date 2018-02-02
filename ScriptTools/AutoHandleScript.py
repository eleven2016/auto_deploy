'''
Create
@author: ywl48338
'''
import os.path


class AutoHandleScript:
    def __init__(self, file_paths, target_path):
        self.filePaths = file_paths
        self.target_path = target_path

    def run_script(self):
        for temp_path in self.filePaths:
            file = open(temp_path)
            file_name = os.path.basename(temp_path)
            cur_path = temp_path.replace(file_name, "")
            new_file_name = file_name.split(".")[0] + "_temp.xml"
            print(file_name)
            content = []
            file_lines = file.readlines()
            for line in file_lines:
                if line.count("<<<<<<<") > 0 or (line.count("=======") > 0 and line.count("============") < 0) or line.count(">>>>>>>") > 0:
                    continue
                if line == '\n' or content.count(line) == 0:
                    content.append(line)

            if len(content) > 0:
                new_file = open(self.target_path + new_file_name, "w")
                for line in content:
                    print(line)
                    new_file.write(line)
