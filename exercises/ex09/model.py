"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730573834"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        change_in_x: float = self.x - other.x
        change_in_y: float = self.y - other.y
        dist_val: float = sqrt(change_in_x**2 + change_in_y**2)
        return dist_val



class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def contract_disease(self) -> None:
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        if (self.sickness == 0):
            return True
        else:
            return False

    def is_infected(self) -> bool:
        if (self.sickness == 1):
            return True
        else:
            return False

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None:
        self.location = self.location.add(self.direction)

        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if (self.is_vulnerable() == True):
            return "gray"
        if (self.is_infected() == True):
            return "red"
        return "black"

    def contact_with(self, other: Cell) -> None:
        if (self.is_infected() == True and other.is_vulnerable() == True):
            other.contract_disease()
        elif (self.is_vulnerable() == True and other.is_infected() == True):
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if (infected_cells >= cells):
            raise ValueError("Number of infected cells should be some proportion of all cells, but not equal to all cells.")
        if (infected_cells <= 0):
            raise ValueError("Some number of infected cells must exist.")
        
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(infected_cells):
            self.population[i].contract_disease()
            # how to make more of them red/infected balls

    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if (cell.location.x > constants.MAX_X):
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if (cell.location.x < constants.MIN_X):
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if (cell.location.y > constants.MAX_Y):
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if (cell.location.y < constants.MIN_Y):
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        for i in range(0, len(self.population)):
            for j in range(i + 1, len(self.population)):
                if (self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS):
                    self.population[i].contact_with(self.population[j])
                    

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False