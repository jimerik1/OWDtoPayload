class BaseParser:
    def __init__(self, data):
        self.data = data
        
    def parse(self):
        """Base parse method, to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")