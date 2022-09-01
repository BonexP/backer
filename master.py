import yaml,time
from worker import transer, zipper
import logging

logging.basicConfig(level=logging.INFO,filename='worker.log')

t=time
with open("config.yml", "r") as f:
    jobs = yaml.load(f, yaml.Loader)
    print(jobs)
    for item in jobs:
        print(item)
        logging.info(f"item type : {item['type']}, localfile : {item['local']}, zipoutput : {item['zipoutput']}, upload : {item['remote']}")
        # need zip?
        if item["zip"]:
            if item["type"] == "singlefile":
                outname=item["zipoutput"]
                item["zipoutput"]=eval(f"f'{outname}'")
                item["local"] = zipper.singlefile(item["local"],item["zipoutput"])
                remotename=item["remote"]
                item["remote"]=eval(f"f'{remotename}'")
                item["remote"]+=".zip"
            elif item["type"] == "folder":
                outname=item["zipoutput"]
                item["zipoutput"]=eval(f"f'{outname}'")
                item["local"] = zipper.folder(item["local"], item["zipoutput"])
                remotename=item["remote"]
                item["remote"]=eval(f"f'{remotename}'")
                item["remote"]+=".zip"
        # trasfer
        print(item)
        logging.info(f"item type : {item['type']}, localfile : {item['local']}, zipoutput : {item['zipoutput']}, upload : {item['remote']}")

        if item["remotedrive"]=="webdav":
            transer.webdav(item["dav"], item["local"], item["remote"])
