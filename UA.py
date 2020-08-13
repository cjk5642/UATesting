import os
import subprocess

def main():
    path = r'C:\\Users\\Connor\\Python Scripts\\UA Testing'

    os.chdir(path)

    cmd = ['curl','-A',0,'google.com']

    data = {}
    with open('UserAgents.txt', 'r') as F:
        for line in F:
            l = str(line).strip()
            cmd[2] = l
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            response = str(p.stdout.read())
            retcode = p.wait()
            code = response[response.find('<H1>') + 4: response.find('</H1>')]
            data[str(line).strip()] = code
            cmd = ['curl','-A',0,'google.com']

    F.close()

    # create a file
    file = open('UserAgentCodes.txt', "w")
    for dat in list(data.items()):
        file.write(f"{dat[0]}: {dat[1]}\n")

    file.close()

if __name__ == '__main__':
    main()
