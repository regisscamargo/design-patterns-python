from abc import ABC, abstractclassmethod

class DatabaseInterface(ABC):
    
    @abstractclassmethod
    def select_one(self):
        pass