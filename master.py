import yaml
from worker import transer
with open('config.yml', 'r') as f:
    y=yaml.load(f,yaml.Loader)
    print(y)
    for item in y:
        print(item['local'],item['remote'])
        transer.webdav(item['dav'],item['local'],item['remote'])

