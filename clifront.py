#!/usr/bin/python3
"""
This file contains a simple command line parser for d
"""

import argparse
import backend

__author__ = "Hayden"
__version__ = "0.1.0"
__license__ = "MIT"

def runcmd(args):
    root_dirname = vars(args)['root_dirname']
    start_filename = vars(args)['start_filename']
    output_filename = vars(args)['output_filename']
    vw_graph = backend.VimwikiGraph(root_dirname, start_filename)
    backend.translate_vwgraph_to_dotlang(vw_graph, output_filename)
    backend.dotlang_to_outfile(output_filename)


def main():
    parser = argparse.ArgumentParser(description='A utility for creating a directed graph of a vimwiki.')
    parser.add_argument('root_dirname', help='')
    parser.add_argument('start_filename', help="The name of the file to start exploring from (usually 'index'), given without an extension.")
    parser.add_argument('output_filename', help='The name of the svg file to output.')
    parser.set_defaults(func=runcmd)
    args = parser.parse_args()
    args.func(args)




if __name__ ==  '__main__':
    main()
