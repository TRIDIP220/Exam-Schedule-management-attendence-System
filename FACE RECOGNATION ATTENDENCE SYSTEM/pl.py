
import subprocess
cmd='python student.py'

p=subprocess.Popen(cmd,shell=True)
out,err=p.communicate()
print(err)

    