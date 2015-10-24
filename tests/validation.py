"""
Test the liblyrics package, using samples from the directories `valids`,
which contains examples of valid lyrics files and `invalids`, which contains
examples of invalids files.

To launch this test, please add the parent directory of `liblyrics`
directory into your PYTHONPATH
"""

from glob import glob
import sys
import os

try:
    from pyparsing import ParseException
except ImportError:
    print("Unable to find pyparsing. Ensure it is installed and is into "
            "your PYTHONPATH.", file=sys.stderr)
    sys.exit(2)

try:
    from liblyrics import Lyrics
except ImportError:
    print("Unable to find liblyrics. Please ensure that the directory "
            "`liblyrics/..` is into your PYTHONPATH.", file=sys.stderr)
    sys.exit(2)


validfiles = glob(os.path.join("valids", "*"))
invalidfiles = glob(os.path.join("invalids", "*"))

files = [(invalidfile, False) for invalidfile in invalidfiles] \
        + [(validfile, True) for validfile in validfiles]

for path, valid in files:
    # Parse file
    exception = None
    try:
        Lyrics.from_file(path)
    except ParseException as ex:
        exception = ex

    # Check result
    if (exception is None) != valid:
        print("Error: {}: {}valid, expected to be {}valid"
                .format(path, "" if exception is None else "in",
                    "" if valid else "in"), file=sys.stderr)
        if exception is not None:
            print("Parser output: {}".format(exception))
        sys.exit(1)

    print("{}: {}valid as expected".format(path, "" if valid else "in"))

# All tests are corrects
sys.exit(0)
