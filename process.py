import subprocess

def run(file, *args):
    return subprocess.run(
        [file], 
        stdout=subprocess.PIPE, 
        input="\n".join(map(str,args)).encode()).stdout.decode()