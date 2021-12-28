# mdwiki-cartographer

These instructions are up to date at least as of commit 5c97b26a0dd3a8739881c285c4ca18c0caa48cd4 (May 16, 2020)

## About

Creates an image of a directed graph representing the structure of a markdown wiki. The program makes certain assumptions about the markdown wiki, including:

* All files in the wiki are in one directory
* All files are .md files
* All links are in the markdown style, e.g. `[File description here](file_name_here)`

## Quick demo

Make sure you have the graphviz package installed first.

To see the program at work without creating your own wiki, just `cd` into the root of the repository and run `./cartographer ./testwiki/ index map.dot`. This will generate an svg graph of `testwiki`. Now open `map.dot.svg` in a web browser.


## How to run

1. Make sure you have the 'graphviz' package installed and that you can successfully run `dot -V` from the command line.
2. Clone the repository and cd into the directory
3. Make `cartographer` executable by running `chmod +x cartographer`
4. Run

```sh
./cartographer "root_dirname" "start_filename" "output_filename"
```
, where

* *root_dirname* is the file path to the root directory of the vimwiki of the form "/.../wikiname/"
* *start_filename* is the name of the file (WITHOUT a file extension) you want the program to start exploring from. You might want this to be 'index' if that is your vimwiki home file.
* *output_filename* is the name of the .dot and .svg files to be outputted

5. Finally, open up the resulting .svg file in the browser of your choice.



