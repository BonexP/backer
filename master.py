import yaml
from worker import transer, zipper

with open("config.yml", "r") as f:
    y = yaml.load(f, yaml.Loader)
    print(y)
    for item in y:
        print(item)
        # need zip?
        if item["zip"]:
            if item["type"] == "singlefile":
                item["local"] = zipper.singlefile(item["local"], item["zipoutput"])
                item["remote"]+=".zip"
            elif item["type"] == "folder":
                item["local"] = zipper.folder(item["local"], item["zipoutput"])
                item["remote"]+=".zip"
        # trasfer
        if item["remotedrive"]=="webdav":
            transer.webdav(item["dav"], item["local"], item["remote"])