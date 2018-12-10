from context_tree.context_tree import Trie, TrieNode
import pickle
import sys
import os
class AdviceSize:
    """
    This class  computes number of node in the context tree and their size.
    """

    def __init__(self, file_name):
        self.file_name=file_name
        self.context_tree=None

    def load_context_tree(self):
        with open(os.path.abspath(os.path.join(os.curdir,'advices',self.file_name)), 'rb') as f:
            self.context_tree = pickle.load(f)

    def bredth_first_search(self):
        pass

    def number_of_node(self):
        total_node_count=0
        number_of_bytes_number = 0
        number_of_bytes_key=0

        for child_lvl1 in self.context_tree.root.children:
            total_node_count+=1
            number_of_bytes_number += sys.getsizeof(child_lvl1.count)
            number_of_bytes_key += sys.getsizeof(child_lvl1.data)
            for child_lvl2 in child_lvl1.children:
                number_of_bytes_number += sys.getsizeof(child_lvl2.count)
                number_of_bytes_key += sys.getsizeof(child_lvl2.data)
                total_node_count+=1
                for child_lvl3 in child_lvl2.children:
                    number_of_bytes_number += sys.getsizeof(child_lvl3.count)
                    number_of_bytes_number += sys.getsizeof(child_lvl3.data)
                    total_node_count += 1

        print("{} - total node {} bytes count {} bytes data {} total {}".format( self.file_name, total_node_count, number_of_bytes_number, number_of_bytes_key, number_of_bytes_number+number_of_bytes_key))


if __name__ == '__main__':
    for file_name in ['book1.cb.advice','news.cb.advice','progc.cb.advice', 'trans.cb.advice']:
        obj=AdviceSize(file_name)
        obj.load_context_tree()
        obj.number_of_node()


