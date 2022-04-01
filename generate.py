# Written by Coolsonickirby/Random
# Music of the day: BlazBlue CPEX Opening (https://www.youtube.com/watch?v=-oKoi8JkvCE)

import difflib
import os, subprocess, json, io
import shutil
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

def loadMSBT(path):
    with open("tmp.json", "w+") as x:
        x.write("{}")
        x.close()
    out = "tmp.json"
    subprocess.call(["dotnet", "MSBTEditorCli.dll", path, out])
    data = []
    with open(out, encoding='utf-8') as f:
        data = json.load(f)
    os.remove(out)
    return data

def makeDirs(path):
    try:
        os.makedirs(path, 777, exist_ok=True)
    except:
        pass


def load_og_msbt(msbt_name):
    if msbt_name not in os.listdir("./msbts"):
        return
    else:
        return {msbt_name.rstrip(".msbt"): loadMSBT(msbt_name)}

def modded_msbt_diff(modded_msbt, msbts_og_data):
        name, ext = os.path.splitext(os.path.basename(modded_msbt))
        lbls_xmsbt = {}
        print(loadMSBT(modded_msbt))
        data = loadMSBT(modded_msbt)["strings"]
        for entry in data:
            for str in difflib.Differ().compare(entry, msbts_og_data):
                print(str)
            if entry["label"] not in msbts_og_data[name] or entry["value"] != msbts_og_data[name][entry["label"]]:
                lbls_xmsbt[entry["label"]] = entry["value"]
        xmsbt_root = Element("xmsbt")
        for lbl in lbls_xmsbt:
            xmsbtLBL = SubElement(xmsbt_root, "entry", {"label": "%s" % lbl})
            value = SubElement(xmsbtLBL, "text")
            value.text = lbls_xmsbt[lbl]
        try:
            xmsbt_string = minidom.parseString(tostring(xmsbt_root, encoding='utf-16', method='xml').decode('utf-16')).toprettyxml(indent="   ")
        except:
            xmsbt_string = tostring(xmsbt_root, encoding='utf-16', method='xml').decode('utf-16')
        with open("%s/%s.xmsbt" % (os.path.dirname(modded_msbt), name), "w", encoding='utf-16') as handle:
            handle.write(xmsbt_string)
