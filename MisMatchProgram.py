'''
Created on Jul 29, 2014

@author: Joey Azofeifa

Algorithm for finding motif with number of mismatches
This does not support insertions or deletions
'''
class node():
    def __init__(self, letter):
        self.nodeID     = letter
        self.transition = {}
        self.FOUND      = False
    def __str__(self):
        if not self.FOUND:
            return "Node ID: " + str(self.transition.keys()[0])
        else:
            return "END NODE"
    def setTransition(self,letter, node):
        self.transition[letter]=node
    def getNext(self, letter):
        if self.transition.has_key(letter):
            return self.transition[letter]
        elif "*" in self.transition:
            return self.transition["*"]
        else:
            return None
    def getNextNodeAnyway(self):
        return self.transition.values()
class RG:
    def __init__(self, userRegex):
        self.rawRegex   = userRegex
        self.FSM        = node("root")
    def buildFSM(self):
        root            = self.FSM
        currNode        = root
        for letter in self.rawRegex:
            
            L   = letter
            if letter == "N":
                L   = "*"
            
            currNode.setTransition(L, node(L))
            currNode    = currNode.getNext(L)
        currNode.FOUND  = True
    def printFSM(self):
        node    = self.FSM
        while not node.FOUND:
            print node.transition.keys(),"=>",
            node=node.transition.values()[0]
            
        
    def search(self, STRING, ERROR_TOL=3):
        root        = self.FSM
        j           = 0
        N           = len(STRING)
        HITS        = list()
        
        for i,l in enumerate(STRING):
            currNode    = self.FSM
            ERROR       = 0
            j       = i
            FOUND   = False
            STOP    = False
            
            while j < N and not currNode.FOUND and not STOP:
                
                if ERROR > ERROR_TOL: 
                    STOP    = True
                elif currNode.getNext(STRING[j]) is None:
                    currNode    = currNode.getNextNodeAnyway()[0]
                    ERROR+=1
                else:
                    currNode    = currNode.getNext(STRING[j])
                    
                j+=1
            if currNode and currNode.FOUND:
                HITS.append((i,j,ERROR, STRING[i:j+1] ))
        return HITS
def runUnitTest():
    regex   = "ATNACNNCNTATANNNTANNNTATANGNNGTNAT"
    
    'atatccacttatcagtaagtatatattgtgtgagt'
    R       = RG(regex)
    R.buildFSM()
    
    
    #ONE MISTMATCH
    TRY1            = "AAAAAAAATAACAACATATAAAATAAAATATAAGAAGTAATAAAAAAAAAA"
    TRY2            = "ATTACTTCTTATATTTTATTTTATATGTTGTTAT"
    TRY3            = "ATCACTGCGTATAGCTTACGGTATACGTTGTCAT" 
    #TWO MISTMATCH
    TRY4            = "GGGGGGGGGGGGATACCAACATATAAAATAAAATATAAGAAGTAATGGGGGGGG"
    TRY5            = "ATTACTTCTTATATTTTATTTTATATCTTGTTAT"
    TRY6            = "ATCACTGCGTATAGCTTACGGTATACGTTCTCAT" 
    #THREE MISTMATCH
    TRY7            = "ATACCAACATATAAAATAAAATATAATAAGTAAT"
    TRY8            = "GGGGGGGGGATTACTTATTATATTTTATTTTATATCTTGTTAT"
    TRY9            = "TTTTTTTTCTCACTGCGTATAGCTTACGGTATACGTTCTCAT" 
    
    
    assert R.search(TRY1)[0] and R.search(TRY1)[1] ==0, "FAIL TRY1"
    assert R.search(TRY2)[0] and R.search(TRY2)[1] ==0, "FAIL TRY2"
    assert R.search(TRY3)[0] and R.search(TRY3)[1] ==0, "FAIL TRY3"
    assert R.search(TRY4)[0] and R.search(TRY4)[1] ==1, "FAIL TRY4"
    assert R.search(TRY5)[0] and R.search(TRY5)[1] ==1, "FAIL TRY5"
    assert R.search(TRY6)[0] and R.search(TRY6)[1] ==1, "FAIL TRY6"
    assert R.search(TRY7)[0] and R.search(TRY7)[1] ==2, "FAIL TRY7"
    assert R.search(TRY8)[0] and R.search(TRY8)[1] ==2, "FAIL TRY8"
    assert R.search(TRY9)[0] and R.search(TRY9)[1] ==2, "FAIL TRY9" 
    
    print "***************All 9 Unit Tests Passed***************"

    


if __name__ == '__main__':
    runUnitTest()
    
    
    
    pass