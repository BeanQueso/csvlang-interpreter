import pandas as pd
import numpy as np
import csv

def main():
    data = []

    with open('main.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            data.append(i)
    var_dict = {}
    for i in data:
        command = i[0]
        args = i[1:]
        if command == "let":
            temp_var = {args[0]:args[1]}
            var_dict.update(temp_var)

        if command == "print":
            for arg in args:
                variable_exists = 0
                for key,value in var_dict.items():
                    if "{"+key+"}" in arg:
                        var_val = value
                        var_name = "{"+key+"}"
                        if "+" in arg:
                            conc_list = arg.split("+")
                            new_arg = ""
                            for x in conc_list:
                                if x == var_name:
                                    el_index = conc_list.index(x)
                                    conc_list[el_index] = var_val
                                    temp_var = ""
                                    for y in conc_list:
                                        temp_var = temp_var+y
                                    print(temp_var)
                            
                        else:
                            print(var_val)
                    elif "{"+key+"}" not in arg:
                        var_count_relative = len(var_dict.items())*-1
                        _arg = arg.replace("{",'')
                        _arg = _arg.replace("}",'')
                        #print(key)
                        if _arg == key:
                            variable_exists+=1
                        else:
                            variable_exists-=1
                        if variable_exists==var_count_relative:
                            df = pd.DataFrame(data)
                            row_num = data.index(i)+1
                            col = str(df[1][row_num-1])
                            col_conc = col.split("+")
                            
                            for u in col_conc:
                                if "{" in u and "}" in u:
                                    col = u
                            col_val = col.replace("{","")
                            col_val = col_val.replace("}","")
                            #print("'{}'".format(col_val))
                            return print("error: mentioned variable"+" '{}' ".format(col_val)+"has not been defined yet. [line",str(row_num)+"]")

                if "\{/" in arg or "\}/" in arg:
                    arg = arg.replace("\{/","{")
                    arg = arg.replace("\}/","}")
                    conc_list = arg.split("+")
                    new_arg = ""
                    for concated_var in conc_list:
                        new_arg = new_arg+concated_var
                    print(new_arg)

                if "{" not in arg and "}" not in arg:
                    conc_list = arg.split("+")
                    new_arg = ""
                    for concated_var in conc_list:
                        new_arg = new_arg+concated_var
                    print(new_arg)

main()
