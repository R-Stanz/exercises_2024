class Node:
    
    left = None
    right = None

    def __init__(self, value, height=1):
        self.value = value
        self.height = height

    def __repr__(self):
        return "\n\tNode Value: {}, Node Height: {}".format(self.value, self.height)
