"""
Parse and save all valid files. Compares input and output files.
"""

import sys
import os
import tempfile
import shutil
import filecmp

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

validdir = os.path.join(os.path.dirname(__file__), "valids")
validfiles = [os.path.join(validdir, f)
        for f in os.listdir(validdir)]
tmpdir = None

try:
    tmpdir = tempfile.mkdtemp(prefix="liblyrics-test")

    for path in validfiles:
        filename = os.path.basename(path)
        # Parse file
        try:
            lyrics = Lyrics.from_file(path)
        except ParseException as ex:
            print("Unable to parse file {}: {}.".format(path, ex),
                    file=sys.stderr)
            sys.exit(1)

        # Save file
        tmpfile = os.path.join(tmpdir, filename)
        lyrics.save_into(tmpfile)

        # Compare input and output
        if not filecmp.cmp(path, tmpfile, shallow=False):
            print("Error: {}: input and output does not match".format(filename),
                    file=sys.stderr)
            sys.exit(1)
        print("{}: Test succeed".format(filename))

    # All tests are valid
    sys.exit(0)

finally:
    if tmpdir is not None:
        shutil.rmtree(tmpdir)
