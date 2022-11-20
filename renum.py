import sys
import os

if len(sys.argv) < 2:
    print "python renum.py pdb"
else:
    fname = sys.argv[1]
    base, ext = os.path.splitext(fname)
    out_fname = base + ".renum" + ext
    with open(out_fname, "w") as out_f:
        for line in open(fname):
            if len(line) > 67:
                line = line[:6] + line[7:]
            out_f.write(line)

    
