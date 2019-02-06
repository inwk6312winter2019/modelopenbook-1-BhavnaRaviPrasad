"""import configparser
config=configparser.configparser()
config.read('running-config.cfg')
print(configsections())
parser.read_dict({})"""


fin = open('running-config.cfg','r')
for line in fin:
    line = line.strip()
    line = line.split()
    print(line)

"""creating dictionary"""
d=dict()

