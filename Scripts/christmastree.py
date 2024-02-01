import pytest

def main():
    levels = input("How many levels should the tree have?:")
    tree = tree_build(levels)
    tree_draw(tree)

def tree_build(levels):
    tree = []
    try:
        levs = int(levels)
        if levs > 0:
            for lev in range(levs):
                # print(level)
                if lev<(levs-1):
                    tree.append((levs-lev)*' ' + (lev*2+1)*'X')
                else: tree.append((levs)*' '+'X')
        else: tree.append('no tree')
    except:
        tree.append('no tree')
    return tree

def tree_draw(tree):
    for level in tree:
        print(level)

#tests
def test_notree():
    assert tree_build('asd') == ['no tree']

def test_1tree():
    assert tree_build(1) == [' X']

def test_2tree():
    assert tree_build(2) == ['  X', '  X']

def test_3tree():
    assert tree_build(3) == ['   X', '  XXX', '   X']

def test_4tree():
    assert tree_build(4) == ['    X', '   XXX', '  XXXXX', '    X']

def test_5tree():
    assert tree_build(5) == ['     X', '    XXX', '   XXXXX', '  XXXXXXX', '     X']




if __name__ == "__main__":
    main()
