from context_tree.context_tree import Trie, Queue


# Input keys (use only 'a' through 'z' and lower case)
def test_context_tree():

    data='aababca'

    # Trie object
    t = Trie()
    CONTEXT_LEN=3
    q=Queue()

    for char in data:
        if q.size() < CONTEXT_LEN:
            q.enqueue(char)
        else:
            q.dequeue()
            q.enqueue(char)

        if q.size()==CONTEXT_LEN:
            t.insert(q.getQueueData())


    assert 2 == t.search('ab')
    assert 1 == t.search('bab')