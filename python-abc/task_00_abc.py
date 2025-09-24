#!/usr/bin/python3
"""
Creating an abstract class
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        return "Bark"
    
class Cat(Animal):

    def sound(self):
        return "Meow"
