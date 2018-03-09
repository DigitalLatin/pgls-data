from subprocess import call
from glob import iglob
from os.path import exists

"""
This script requires the TEIC Stylesheet package from: https://github.com/TEIC/Stylesheets
The teitohtml file used by this script is located in the bin/ directory of the above package
and will need to be pointed to in tei_bin_path.

Requirements of the TEIC Stylesheet package will need to be installed.

The converted files will be placed in the directory pointed to in output_dir.
"""

# TODO: Update the following paths
tei_bin_path = "/Users/sjhuskey/Development/TEIC/Stylesheets/bin/"
glob_path = "/Users/sjhuskey/Development/TEIC/pgls-texts/**/*lat?.xml"
output_dir = "/Users/sjhuskey/Development/TEIC/pgls-texts/rendered-html/"

if not exists(output_dir):
    print("Output directory needs to be created first!")
    exit(1)

teitohtml = tei_bin_path + "teitohtml"

if not exists(teitohtml):
    print("Could not find teitohtml script - check configuration")

files = iglob(glob_path, recursive=True)
for file in files:
    outfile = output_dir + file.split("/")[-1].replace(".xml", ".html")
    if not exists(outfile):
        print("Converting: {0}".format(file))
        call([teitohtml, file, outfile])
    else:
        print("Skipping: {0}".format(file))
