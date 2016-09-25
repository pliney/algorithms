""" Author: Michael Chambliss
    Algorithms Assignment #2
    Word Tree

Created on python 2.7

Can be run with a command line argument to specify a file of words to load
Ex: python word_tree.py wordfile.txt

The file should be in the current directory or an absolute path should be specified"""

import Tkinter as tk
import sys
import os.path

"""A tree data structure that contains several functions for adding words to the tree and searching
for words contained in the tree"""
class word_tree:
    def __init__(self):
        self.root = node()

    """Adds a text file of words to the tree, each line represents one word

    Args:
        filename: name of file to be added, must be relative to current directory or an absolute path"""
    def add_file_to_tree(self, filename):
        file = open(filename, mode='rt')
        word_list = file.readlines()
        for word in word_list:
            word = word.lower()
            self.add_word(word.strip())
        file.close()

    """A function for counting the # of words in the tree
    Returns: the number of words in tree"""

    def count_tree(self):
        return self.root.count_tree()

    """Prints the entire tree in alphabetical order"""
    def print_tree(self):
        self.root.print_tree()

    """Adds a word to the tree

    Args:
        word: a string to be added to the tree"""
    def add_word(self, word):
        self.root.add_word(word, word)

    """Searches for words in the tree that begin with given string

    Args:
        word_fragment: the beggining of a word to serach for
        num_words: the number of words to return

    Returns: a list of words"""
    def word_search(self, word_fragment, num_words):
        word_list = []
        self.root.word_search(word_fragment, num_words, word_list)
        return word_list

"""A node object for a tree data structure. Each node contains a dictionary of children, there is no
specified number of children for each node. New children are added to the dictionary as needed. Each
node also contains a word variable, if it is not equal to None then the path through the tree spells out
the string in the word variable."""
class node:

    def __init__(self):
        self.children = {}
        self.word = None

    """Recursive function for adding words to the tree
    Args:
        word: the word being added to tree
        word_part: the part of the word after all previous node's letters have been removed from it"""
    def add_word(self, word, word_part):

        if word_part == '':
            self.word = word
        else:
            #if there is not a child for the first letter in remaining string, create a new child
            if word_part[:1] not in self.children:
                self.children[word_part[:1]] = node()
            self.children[word_part[:1]].add_word(word, word_part[1:])

    """Print tree out in alphabetical order"""
    def print_tree(self):
        keys = self.children.keys()
        keys.sort()
        if self.word != None:
            print(self.word)
        for key in keys:
            self.children[key].print_tree()

    """Recursive function for counting the words in the tree
        Returns: # of words in the tree below and including this node if it contains a word"""
    def count_tree(self):
        count = 0

        for key in self.children:
            count += self.children[key].count_tree()

        if self.word != None:
            count += 1
        return count

    """Recursive function for searching for words in the tree
    Args:
        word_fragment: the remaining part of search string, at each node the first char is
                       removed from string
        num_words: the number of words to find before halting search
        word_list: a list of words found by the search, one list object is shared between
                   all recursive calls"""
    def word_search(self, word_fragment, num_words, word_list):
        #if enough words have already been found then return
        if len(word_list) >= num_words:
            return

        #if the search string is empty then all words below or at this node start with the original search string
        if word_fragment == '':

            #add the nodes word if one exists
            if self.word != None:
                word_list.append(self.word)

            #continue searching down the tree
            for key in self.children:
                self.children[key].word_search('', num_words, word_list)
        #continue down the tree until the search string is empty
        else:
            if word_fragment[:1] in self.children:
                self.children[word_fragment[:1]].word_search(word_fragment[1:], num_words, word_list)
            else:
                word_list.append("No words found")
                word_list.extend(['']*10)


"""Initializes a Tkinter gui for using the word search

    Args: word_tree: a word tree, must have words in it before running
        this function or no results will be given"""
def gui_init(word_tree):
    root = tk.Tk()
    root.title("Word finder")
    #text entry variable
    textvar = tk.StringVar()
    L1 = tk.Label(root, textvariable = 'Begin typing a word:')
    entry = tk.Entry(root, bd=5, textvariable = textvar)
    word_list_box = tk.Listbox(root, height=10, width=40)
    L1.grid(column=0,row=0)
    entry.grid(column=0,row=1)
    word_list_box.grid(column=0,row=2)

    #continuiously updates the search results and changes the display
    def update_search():
        num_words = 10
        word_list = word_tree.word_search(textvar.get(), num_words)
        for i in range(0, len(word_list)):
            word_list_box.insert(i, word_list[i])
        root.after(250, update_search)

    #calls update search after opening gui
    root.after(250, update_search)

    root.mainloop()

def main(filename='words.txt'):
    print('Loading dictionary please wait...')
    tree = word_tree()
    if os.path.isfile(filename):
        tree.add_file_to_tree(filename)
        gui_init(tree)
    else:
        print(filename + ' was not found in current directory, please rerun program with a command line\n'
                         'argument specifying a text file of words.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()





