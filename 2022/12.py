import copy
import math
import re

from aocd import data, numbers, submit
lines = list(map(str, data.splitlines()))

grid = [[ord(x) for x in line] for line in lines]
steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
