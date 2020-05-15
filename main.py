#!/usr/bin/python3
# main.py

import os
from collections import deque
import re


# NOTE: manually tested get_link_names() to prototype satisfaction
def get_link_names(curr_filename):
    """Returns a set of string filenames of the linked-to files in $filename"""
    with open (curr_filename, 'r') as currfile:
        lines = currfile.readlines()

    print('LINES = ', lines)
    ref_filename = []
    for line in lines:
        # Find matches for links of the form: [reference text here](reference_filename_here)
        ref_filename.extend(re.findall('\[.*?\]\(.*?\)', line))

    print('REF_FILENAME = ', ref_filename)
    
    refs = []
    filenames = []
    for pair in ref_filename:
        templist = re.findall('[^\[\]\(\)]*', pair)  
        print('TEMPLIST = ', templist)  # TODO: deleteme
        
        # Now we have templist == ['', 'key words', '', '', 'file name here', '', '']
        while '' in templist:  # Remove empty strings from list
            templist.remove('')

        # Now we have templist == ['key words', 'file name here']

        refs.append(templist[0])  # We don't really need this, but it may be useful for later functionality
        filenames.append(templist[1])

    return filenames



class VimwikiGraph:
    """A directed graph representing a the links in a vim wiki."""
    
    def __init__(self, root_filename):
        """Init a new (empty) VimwikiGraph"""
        
        # Init fields
        # ----------------------------------------
        self.root = root_filename

        # Maps a string wimwiki filename to a set of linked filenames
        self.edges = {self.root: set()}

        self._visited = set()  # Nodes in this set have been visited


        # Generate graph in a breadth-first manner
        # ----------------------------------------

        q = deque()
        q.append(self.root)
        while q:

            v_curr = q.popleft()

            if v_curr not in self._visited:
                self._visited.add(v_curr)  # Visit curr vtx

                # Generate adjacent neighbors & add to queue
                neighbors = get_link_names(v_curr) 
                self.edges[v_curr] = neighbors
                for v in neighbors:  # TODO: rewrite using list comp.
                    if v not in self._visited:
                        q.append(v)


    # TODO: may have to define this before __init__ method
    def _try_add_node(self, parent, child):
        """
        Tries to add $child to the adjacency set of $parent. If a file
        by the same name in the adjacency set doesn't already exist,
        adds string filename $child to the adjacency set and returns True.
        Else, does nothing and returns False.
        """
        pre_add_size = len(self.edges[parent])
        self.edges[parent].add(child)
        return len(self.edges[parent]) > pre_add_size




def main():
    # test on index.md
    filename = './testwiki/index.md'
    print('GETLINKNAMES() == ', get_link_names(filename))


if __name__ == '__main__':
    main()
