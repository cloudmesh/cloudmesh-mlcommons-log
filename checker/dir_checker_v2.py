'''
Checking folder structure as described in section 13 of policy document
(https://github.com/mlcommons/science/blob/main/policy.adoc)
'''

import os, sys
from pathlib import Path

def list_files(startpath):
    benchmarks = ['cloudmask', 'uno', 'earthquake', 'stemdl']
    resultFiles = ['config.yaml', 'README.md', 'result.txt']
	
    level = 1
    for root, dirs, files in os.walk(startpath):
        #print(level, dirs,files)
        level = level + 1
        if(level==3):
            appName = str(dirs[0])
            if (appName in benchmarks):
                print("Benchmark found in the list")
            else:
                print(dirs[0]+": application not found in the list of benchmarks")
                return	
				
        if(level==5):
            if(str(files[0]) == 'system_description.yaml'):
                print("System description found")
            else:
                print(dir + "Missing system_description.yaml")
                return
				
        if(level==7):
            if(str(files[0]) in resultFiles and str(files[1]) in resultFiles and str(files[2]) in resultFiles):
                print("Result files all found")

# Checking folder structure
# python dir_checker_v2.py "path_to_directory"

pathName = Path(str(sys.argv[1]))
print("pathName >>: ", pathName)
list_files(pathName)