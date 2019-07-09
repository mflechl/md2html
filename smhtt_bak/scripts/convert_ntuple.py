#!/usr/bin/env python
import os

if not 'CMSSW_BASE' in os.environ:
    from varmap import VarMap
else:
    from HTT.sync.varmap import VarMap

import ROOT

# forbids root to hijack command line 
ROOT.PyConfig.IgnoreCommandLineOptions = True

def convert(options, args):
    rootfname, direction = args
    varmap = VarMap(options.map)
    ifile = ROOT.TFile(rootfname)
    intuple = ifile.Get(options.tree_name)
    print 'converting ntuple with nevents = ', intuple.GetEntries()
    ofile = ROOT.TFile(options.output_file,'recreate')
    ontuple = intuple.CloneTree()
    the_map = varmap.toa if direction is 'a' else varmap.tob
    for iv, ov in sorted(the_map.iteritems()):
        print iv, '->', ov
        ontuple.SetAlias(ov, iv)
    ofile.Write()
    ofile.Close()
    ifile.Close()
    
def get_options():
    import os
    import sys
    from optparse import OptionParser
    usage = """usage: %prog <input ntuple root file> <a or b>
    
    Creates a new ntuple from the one in the input file. 
    The new ntuples has aliases for the new naming scheme, a or b.
    Please see sync/python/varmap.py for more information about naming schemes.
    """
    parser = OptionParser(usage=usage)
    parser.add_option("-t", "--tree-name", dest="tree_name",
                      default='events',
                      help='Key of the tree in the root file. Default is "events".')
    default_map = os.path.expandvars('$CMSSW_BASE/src/HTT/sync/material/ntuple_format.txt')
    parser.add_option("-m", "--map", dest="map",
                      default=default_map,
                      help="Map file. Default is {}. If you're not working in CMSSW, you need to provide this option" )
    parser.add_option("-o", "--output", dest="output_file",
                      default=None,
                      help='Output file. Name automatically built from input file name if not provided.')
    
    (options,args) = parser.parse_args()
    if len(args)!=2:
        print parser.usage
        sys.exit(1)
    if not os.path.isfile(options.map):
        print 'map file', options.map, 'does not exist. specify it with the -m option'
        sys.exit(2)
    if args[1] not in ['a','b']:
        print 'conversion target should be either "a" or "b"'
        sys.exit(3)
    if options.output_file is None:
        options.output_file = '_'.join([args[1], os.path.basename(args[0])])
    return options, args


if __name__ == '__main__':
    options, args = get_options()
    convert(options, args)
