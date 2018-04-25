
if __name__ == '__main__':

    file_path = "D:\\workspace_test\\AutoDeploy\\ScriptTools\\dup_data_20180410.txt"

    file = open(file_path, "r")

    for lines in file.readlines():
        id_array = lines.split(",")
        if len(id_array) == 2:
            if int(id_array[0])+1 == int(id_array[1]) or int(id_array[0])-1 == int(id_array[1]):
                print(lines.replace("\n" , ","))

        if len(id_array) > 2:
            for n0 in id_array:
                flag = 0
                for n in id_array:
                    if int(n0) + 1 == int(n) or int(n0) - 1 == int(n):
                        flag = 1
                        break

                if flag == 1:
                    print(lines.replace("\n" , ","))
                    break
