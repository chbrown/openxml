#!/usr/bin/env python
from setuptools import setup
import os
# here = os.path.abspath(os.path.dirname(__file__))


def recurse(root, folders):
    cwd = os.getcwd()
    os.chdir(root)
    exclude = set(['.DS_Store'])
    for folder in folders:
        for dirpath, _, filenames in os.walk(folder):
            if len(set(filenames) - exclude) > 0:
                yield os.path.join(dirpath, '*')
    os.chdir(cwd)

package_data_folders = list(recurse('openxml', ['docx_template', 'pptx_template']))

setup(name='openxml',
    version='0.1.1',
    description='Create .pptx and .docx files from Python',
    author='Tom Scrace, Christopher Brown',
    author_email='tom.scrace@timetric.com, audiere@gmail.com',
    license='MIT',
    url='http://github.com/chbrown/openxml',
    packages=['openxml'],
    install_requires=['lxml'],
    include_package_data=True,
    zip_safe=False
    # package_data={'openxml': package_data_folders}
)
