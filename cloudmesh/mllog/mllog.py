from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import readfile
import json

class MLLOG:

    def grep(self, filename):
        content = readfile(filename)
        print (filename)
        content = "\n".join(Shell.find_lines_with(content, ":::MLLOG"))
        return content

    def check_file(self, filename):
        print (filename)

    def check_dir(self, dirname):
        print(dirname)


    def content_to_list_of_dicts(self, content):
        entries =[]
        content = content.splitlines()
        count = 0
        for line in content:
            try:
                entry = self.line_to_dict(line)
                entry["line"] = count
                entries.append(entry)
            except Exception as e:
                print (e)
                pass
            count = count + 1
        return entries

    def content_to_string(self, content):
        "\n".join(content)

    def line_to_dict(self, line):
        content = line.replace(":::MLLOG ", "")
        d = json.loads(content)
        return d

    def find_org(self, filename):
        content = self.grep(filename).splitlines()
        keys = {
            "submission_benchmark",
            "submission_org",
            "submission_division",
            "submission_status",
            "submission_platform",
        }
        success = True
        for key in  keys:
            found = Shell.find_lines_with(content, key)
            if (len(found) == 0):
                success = False
                print(f"Error: {key} not found")
            if (len(found) > 1):
                success = False
                print(f"Error: to many {key}'s found: {len(found)}")
        return success

    def find_intervals(self, filename):
        content = self.grep(filename).splitlines()
        keys = {
            "init_start",
            "init_stop",
            "run_start",
            "run_stop",
        }
        success = True
        count = {}
        for key in  keys:
            found = Shell.find_lines_with(content, key)
            if (len(found) == 0):
                success = False
                print(f"Error: {key} not found")
            if (len(found) > 1):
                success = False
                print(f"Error: to many {key}'s found: {len(found)}")
            count[key] = len(found)
        return success and count["init_start"] == count["init_end"] and count["run_start"] == count["run_end"]

    def find(self, content, query):
        result = []
        for line in content:
            print (line)
            for q in query:
                print (q)


