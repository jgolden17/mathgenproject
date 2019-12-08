"""
Defines the models for the scraped items

See documentation in https://docs.scrapy.org/en/latest/topics/items.html
"""
from scrapy import Item, Field

class MathGenProjectItem(Item):
    """
    Represents a MathGenProjectItem
    """
    href = Field()

class Mathematician(MathGenProjectItem):
    """
    Respresents a mathematician
    """
    id = Field()
    name = Field()
    university = Field()
    dissertation = Field()
    advisors = Field()
    students = Field()

class Advisor(Mathematician):
    """
    Represents a mathematician's advisor
    """

class Student(Mathematician):
    """
    Represents a mathematician's student
    """
