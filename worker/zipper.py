import zipfile
import shutil

def singlefile(filename,outputfile):
    with zipfile.ZipFile(outputfile+'.zip', mode="w") as archive: 
        archive.write(filename)

def folder(folder,outputfile):
    shutil.make_archive(outputfile,'zip',folder)
