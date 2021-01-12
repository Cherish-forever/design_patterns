#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from __future__ import annotations
from abc import ABC, abstractmethod

# abstract product A
class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class ConcreateProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class ConcreateProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."

# abstract product B
class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> None:
        pass

    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass

class ConcreateProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"

class ConcreateProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


# abstract factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreateFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreateProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreateProductB1()

class ConcreateFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreateProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreateProductB2()


# client
def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreateFactory1())

    print("\n")
    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreateFactory2())
