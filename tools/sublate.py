#!/usr/bin/env python3
import datetime
import glob
import json
import os
import shutil
import subprocess
import types

import jinja2
import yaml


data = {}
root = os.getcwd()


_data = data


def run(pathname):
    for path in glob.glob(pathname):
        if path.endswith(".py"):
            with open(path) as f:
                code = f.read()
                module_dict = {}
                exec(code, module_dict)
                module = types.ModuleType('module')
                module.__dict__.update(module_dict)

                cwd = os.getcwd()
                os.chdir(os.path.dirname(path))
                os.chdir(cwd)
        else:
            subprocess.run([path])


def cp(source, target):
    if os.path.isdir(source):
        shutil.copytree(source, target)
    else:
        shutil.copyfile(source, target)  # corrected typo


def mkdir(path):
    os.makedirs(path, exist_ok=True)


def rm(pattern):
    for path in glob.glob(pattern, recursive=True):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        elif os.path.isfile(path):
            os.remove(path)


def render(path, template=None, local_data={}):
    env = jinja2.Environment(loader=jinja2.ChoiceLoader([
        jinja2.FileSystemLoader(searchpath="."),
        jinja2.FileSystemLoader(searchpath=root)
    ]))

    _template = env.get_template(template if template else path)

    output = _template.render(**(_data | local_data)).strip()  # changed variable name
    with open(path, 'w+') as f:
        f.write(output)


def read(pathname):
    global _data  # make it clear that we are using the global variable
    for path in glob.glob(pathname):
        with open(path) as f:  # Explicitly set encoding to utf-8
            if path.endswith(".json"):
                _data[path] = json.loads(f.read())

            if path.endswith(".yaml"):
                _data[path] = yaml.load(f.read(), Loader=yaml.FullLoader)

    return _data


def date_iso():
    return datetime.datetime.now().isoformat()
