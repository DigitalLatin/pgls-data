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
output_dir = "/Users/sjhuskey/Development/TEIC/pgls-texts/rendered-txt/"

if not exists(output_dir):
    print("Output directory needs to be created first!")
    exit(1)

teitotxt = tei_bin_path + "teitotxt"

if not exists(teitotxt):
    print("Could not find teitotxt script - check configuration")

files = iglob(glob_path, recursive=True)
for file in files:
    outfile = output_dir + file.split("/")[-1].replace(".xml", ".txt")
    if not exists(outfile):
        print("Converting: {0}".format(file))
        call([teitotxt, file, outfile])
    else:
        print("Skipping: {0}".format(file))
