import requests
from requests.auth import HTTPBasicAuth
import easywebdav
easywebdav.basestring = str
easywebdav.client.basestring = str

from webdav3.client import Client
def easewebdav(config,localfile,remotefile):

    # Start off by creating a client object. Username and
    # password may be omitted if no authentication is needed.
    webdav = easywebdav.connect(config['server'], username=config['username'], password=config['password'])
    # Do some stuff:
    # webdav.upload(localfile,remotefile)
    webdav.mkdir('job')
    webdav.upload(localfile,remotefile)

def webdavclient(config,localfile,remotefile):
    options = {
    'webdav_hostname': config['server'],
    'webdav_login':    config['username'],
    'webdav_password': config['password'],
    'disable_check': True,
    }
    client = Client(options)
    client.verify = False # To not check SSL certificates (Default = True)
    # free_size = client.free()
    client.upload_sync(remote_path=remotefile, local_path=localfile)

def requestswebdav(config,localfile,remotefile):
    files = open(localfile,'rb')
    url = config['server']
    r = requests.put(url+remotefile, files={"archive": files},auth = HTTPBasicAuth(config['username'], config['password']))
    print(r.text)

webdav=webdavclient

if __name__ == '__main__':
    server={'server':'http://192.168.3.13:5244/dav/','username':'admin','password':'iamadmin'}
    webdavclient(server, 'config.yml', 'hdd/backups/hi.zip')
