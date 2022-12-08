"""This module defines enumeration states for each Holiday"""
import enum


class HolidayEnum(enum.Enum):
    """An enumeration of states that each represent a Holiday."""
    EASTER = 0,
    CHRISTMAS = 1,
    HALLOWEEN = 2,
