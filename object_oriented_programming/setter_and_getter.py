from __future__ import annotations
from typing import Union
import logging

class Product:

    def __init__(self, name:str, price:Union[float,int]) -> Product:
        self._name = name
        self._price = price 

    def __add__(self, other):
        return self.price + other.price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value:Union[int, float]):
        try:
            float(value)
        except ValueError:
            logging.error(f"Cannot set attribute name as '{value}'. Value must be numerical")
          
    @property
    def name(self):
        return self._name
    
        
if __name__ == '__main__':
    apple = Product("Apple", 1.5)
    apple.price = 'j'
    print(apple + apple)
    