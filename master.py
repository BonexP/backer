import yaml,time
from worker import transer, zipper

t=time
with open("config.yml", "r") as f:
    jobs = yaml.load(f, yaml.Loader)
    print(jobs)
    for item in jobs:
        print(item)
        # need zip?
        if item["zip"]:
            if item["type"] == "singlefile":
                outname=item["zipoutput"]
                item["local"] = zipper.singlefile(item["local"], eval(f"f'{outname}'"))
                item["remote"]+=".zip"
            elif item["type"] == "folder":
                item["local"] = zipper.folder(item["local"], eval(f"f'{outname}'"))
                item["remote"]+=".zip"
        # trasfer
        if item["remotedrive"]=="webdav":
            transer.webdav(item["dav"], item["local"], item["remote"])