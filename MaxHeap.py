from seeds import getGames  # Import the getGames function to retrieve games list
from ADT import Game  # Import Game to confirm we are working with Game objects

class MaxHeap:
    def __init__(self, priority_field="price"):
        self.heap = []
        self.priority_field = priority_field

    def parent(self, index):
        return (index - 1) // 2

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.parent(index) >= 0

    def hasLeftChild(self, index):
        return self.leftChild(index) < len(self.heap)

    def hasRightChild(self, index):
        return self.rightChild(index) < len(self.heap)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, game):
        self.heap.append(game)
        self.heapifyUp(len(self.heap) - 1)

    def heapifyUp(self, index):
        while (self.hasParent(index) and 
               self.getPriorityValue(self.parent(index)) < self.getPriorityValue(index)):  # Changed to '<' for MaxHeap
            self.swap(self.parent(index), index)
            index = self.parent(index)

    def heapifyDown(self, index):
        while self.hasLeftChild(index):
            larger_child_index = self.leftChild(index)  # Renamed to larger_child_index
            if (self.hasRightChild(index) and 
                self.getPriorityValue(self.rightChild(index)) > self.getPriorityValue(larger_child_index)):  # Changed to '>' for MaxHeap
                larger_child_index = self.rightChild(index)

            if self.getPriorityValue(index) >= self.getPriorityValue(larger_child_index):  # Changed to '>=' for MaxHeap
                break  # Heap property is satisfied
            else:
                self.swap(index, larger_child_index)

            index = larger_child_index

    def extractMax(self):  # Renamed to extractMax for consistency
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.heapifyDown(0)  # Maintain the heap property
        return root

    def getPriorityValue(self, index):
        return getattr(self.heap[index], self.priority_field)

    def importGames(self):
        games = getGames()  # Get the list of games from the seeds module
        for game in games:
            self.insert(game)

    def extractSortedGames(self):
        sorted_games = []
        while self.heap and len(sorted_games) < 10:  # Only extract up to 10 games
            game = self.extractMax()
            sorted_games.append(game)
        return sorted_games  # Return list of Game objects directly 
