pybaccker
1. zipper to zip file 
2. transer to tasnslate file to remote backer


## requirement

```bash
pip install webdavclient3
```

dav(sort by recommendation):

||alist on server|go-webdav on rpi|
|-|-|-|
|webdavclient|yes|yes|
|requestwebdav|yes|yes|
|easywebdav(not recommend)|bad|bad|

to use it, you need to fill the config file:
```yaml
-
  type: singlefile # or folder
  local: localfilebalabala
  # need zip ?
  zip: True # of False
  # zipped file name output without .zip postfix
  # not used if zip is False
  zipoutput: configzipped
  remotedrive: webdav # only webdav now
  dav: 
    server: 'http(s)://host:port/balabala'
    username: 'yourname'
    password: 'password'
  remote: 'path/to/newbeee.file'

```

if your want ot do servel jobs, you can repeat more time:
```yaml
-
  type: singlefile # or folder
  local: localfilebalabala
  # need zip ?
  zip: True # of False
  # zipped file name output without .zip postfix
  # not used if zip is False
  zipoutput: configzipped
  remotedrive: webdav # only webdav now
  dav: 
    server: 'http(s)://host:port/balabala'
    username: 'yourname'
    password: 'password'
  remote: 'path/to/newbeee.file'
-
  type: singlefile # or folder
  local: localfilebalabala
  zip: True # of False
  zipoutput: configzipped
  remotedrive: webdav # only webdav now
  dav: 
    server: 'http(s)://host:port/balabala'
    username: 'yourname'
    password: 'password'
  remote: 'path/to/newbeee.file'
-
  type: singlefile # or folder
  local: localfilebalabala
  zip: True # of False
  zipoutput: configzipped
  remotedrive: webdav # only webdav now
  dav: 
    server: 'http(s)://host:port/balabala'
    username: 'yourname'
    password: 'password'
  remote: 'path/to/newbeee.file'

```
