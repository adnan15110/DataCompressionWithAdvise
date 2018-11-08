
class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [] # can be improved by having  a dict
        self.data = 0
        self.count=0
        # isEndOfWord is True if node represent the end of the word
        self.isEnd = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def insert(self, key):
        pCrawl = self.root
        length = len(key)

        for ind, char in enumerate(key):
            # check if the char already exist in that level or not
            child_found=False
            for child in pCrawl.children:
                if child.data == char:
                    child_found=True
                    pCrawl=child
                    pCrawl.count+=1
                    break

            if not child_found:
                new_node = self.getNode()
                new_node.data=char
                new_node.count=1
                pCrawl.children.append(new_node)
                pCrawl=pCrawl.children[-1]


        pCrawl.isEnd = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)

        found=False
        for ind, char in enumerate(key):
            for child in pCrawl.children:
                if child.data==char:
                    found=True
                    pCrawl=child
                    break

            if not found:
                break

        return pCrawl.count


class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self,data):
        self.queue.append(data)
        return True

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        return ("Queue Empty!")

    def size(self):
        return len(self.queue)

    def getQueueData(self):
        return ''.join(d for d in self.queue)