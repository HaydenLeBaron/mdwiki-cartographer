#!/usr/bin/python3
# main.py

import os  # TODO: do i need the os module?
from collections import deque
import re


# NOTE: manually tested get_link_names() to prototype satisfaction
def get_link_names(curr_filename):
    """
    Returns a set of string filenames of the linked-to files in $filename.
    Note that the var $filename should have no extension, though the corresponding
    actual file name must have a .md extension

    Assumes links of the form: [reference text here](reference_filename_here)
    """

    ''' 
    TODO: Consider making this open file line not throw exception when file doesn't exist
    There just might be a link that doesn't yet point to a file.
    '''
    with open ('{}.md'.format(curr_filename), 'r') as currfile:
        lines = currfile.readlines()

    #print('LINES = ', lines)  # DBGPRNT

    ref_filename = []
    for line in lines:
        # Find matches for links of the form: [reference text here](reference_filename_here)
        ref_filename.extend(re.findall('\[.*?\]\(.*?\)', line))

    #print('REF_FILENAME = ', ref_filename)  # DBGPRNT
    
    refs = []
    filenames = []
    for pair in ref_filename:
        templist = re.findall('[^\[\]\(\)]*', pair)  
        #print('TEMPLIST = ', templist)  # DBGPRNT
        
        # Now we have templist == ['', 'key words', '', '', 'file name here', '', '']
        while '' in templist:  # Remove empty strings from list
            templist.remove('')

        # Now we have templist == ['key words', 'file name here']

        refs.append(templist[0])  # We don't really need this, but it may be useful for later functionality
        filenames.append(templist[1])

    return filenames



class VimwikiGraph:
    """
    A directed graph representing a the links in a vim wiki. Assumes the
    actual vim wiki does not have self references. No wiki page should 
    have a link to itself. Also assumes all file names in the wiki are 
    unique, even if they are split among different directories.
    """
    
    def __init__(self, root_dir_name, start_filename_no_ext):
        """
        Init a new VimwikiGraph. Root dirname should be of the form:
        /dirA/dirB/.../dirN/
        """
        
        # Init fields
        # ----------------------------------------
        self.root = root_dir_name

        # Maps a string wimwiki filename to a set of linked filenames
        self.edges = {self.root: set()}

        self._visited = set()  # Nodes in this set have been visited


        # Generate graph in a breadth-first manner
        # ----------------------------------------

        root_file = '{}{}'.format(self.root, start_filename_no_ext)

        q = deque()
        q.append(root_file)
        while q:

            v_curr = q.popleft()

            if v_curr not in self._visited:
                self._visited.add(v_curr)  # Visit curr vtx

                # Generate adjacent neighbors & add to queue
                neighbors = get_link_names(v_curr) 
                self.edges[v_curr] = neighbors
                for v in neighbors:  # TODO: rewrite using list comp.
                    if v not in self._visited:
                        q.append('{}{}'.format(self.root, v))


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

    def _dbg_print(self):
        print('---------VimwikiGraph._dbg_print-------')
        print('edges == ', self.edges)
        print()
        print('visited == ', self._visited)
        print('---------------------------------------')




def main():
    root_dirname = '/home/hlebaron98/exocortex/facio/vimwiki-cartographer/testwiki/'  # (must be without extension)
    #print('GETLINKNAMES() == ', get_link_names(start_filename))  # DBGPRNT
    start_filename_no_ext = 'index'

    graph = VimwikiGraph(root_dirname, start_filename_no_ext)
    graph._dbg_print()




if __name__ == '__main__':
    main()
