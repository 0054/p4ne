import glob
import re


PATH = '/home/jet/seafile/Seafile/p4ne_training/config_files/*'

gen_path = glob.iglob(PATH)




if __name__ == "__main__":
    l = set()
    for file_name in gen_path:
        with open(file_name) as f:
            for line in f:
                if 'ip address' in line:
                    splt = line.split()
                    if len(splt) == 4:
                        l.add('/'.join(splt[2:]))
    for ip in l:
        print(ip)
