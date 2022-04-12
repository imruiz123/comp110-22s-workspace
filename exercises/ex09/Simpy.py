"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730335383"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Wtf am I doing."""
        self.values = values 

    def __str__(self) -> str:
        """I kinda get it now."""
        return f"({self.values})"

    def fill(self, value_one: float, two: int) -> None:
        """I think this wrong lmfao."""
        result: list[float] = []
        i: int = 0 
        while i < two:
            result.append(value_one)
            i += 1 
        self.values = result 

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This shit not working."""
        result: list[float] = []
        i: float = start 
        assert step != 0.0 
        while i < stop:
            result.append(i)
            i += step 
        if i < 0:
            while i > stop: 
                result.append(i)
                i += step 
            
        self.values = result 

    def sum(self) -> float:
        """kinda get it."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """lmfao lets see."""
        result: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] + rhs)
                i += 1
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values) 
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1 
                
        return Simpy(result) 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """lmfao lets see."""
        result: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] ** rhs)
                i += 1
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values) 
            while i < len(self.values):
                result.append(self.values[i] ** rhs.values[i])
                i += 1 
                
        return Simpy(result) 
