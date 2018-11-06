from context_tree.context_tree import Trie

# Input keys (use only 'a' through 'z' and lower case)
def test_context_tree():
    keys = ["the", 'the', 'the', 'tha']

    # Trie object
    t = Trie()

    for key in keys:
        t.insert(key)

    assert 3==t.search('the')
    assert 1 == t.search('tha')
    assert 4 == t.search('th')
