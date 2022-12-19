import re
from collections import deque
import copy

from aocd import data, submit, numbers
lines = data.splitlines()

pattern = re.compile(r'\d+')


def get_max_geodes(bp, max_resources, time, robots, materials, states):
    # check for existing state
    key = tuple([time, *robots, *materials])
    if key in states:
        return states[key]

    # if we do nothing for the time remaining
    geodes = materials[-1] + robots[-1] * time

    for idx, (robot, resources) in enumerate(bp.items()):
        # if we already have enough robots
        if robot != 'geode' and robots[idx] >= max_resources[idx]:
            continue

        # otherwise we wait for materials
        minutes = 0
        for idy, resource in enumerate(resources):
            # if we have no robots there is no point in waiting
            if robots[idy] == 0:
                break
            minutes = max(minutes, -((resources[resource] - materials[idy]) // -robots[idy]))
        else:
            # wait for materials
            time_remaining = time - minutes

            # if it takes too long
            if time_remaining <= 1:
                continue

            # update robots
            robots_copy = copy.deepcopy(robots)
            robots_copy[idx] += 1
            time_remaining -= 1

            # update materials
            materials_copy = [stash + bots * minutes for bots, stash in zip(robots, materials)]
            for idy, resource in enumerate(resources):
                materials_copy[idy] -= resources[resource]

            # recursion
            geodes = max(geodes, get_max_geodes(bp, max_resources, time_remaining, robots_copy, materials_copy, states))

    # store geodes in states
    states[key] = geodes
    return geodes


def calculate(p):
    total = 0 if p == 1 else 1
    for line in lines:
        id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = list(
            map(int, pattern.findall(line)))

        if p == 2 and id > 3:
            break

        bp = {}
        bp['ore'] = {'ore': ore_ore}
        bp['clay'] = {'ore': clay_ore}
        bp['obsidian'] = {'ore': obsidian_ore, 'clay': obsidian_clay}
        bp['geode'] = {'ore': geode_ore, 'clay': 0, 'obsidian': geode_obsidian}

        # get max of each resource
        ore = max([v.get('ore', 0) for v in bp.values()])
        clay = max([v.get('clay', 0) for v in bp.values()])
        obsidian = max([v.get('obsidian', 0) for v in bp.values()])
        max_resources = [ore, clay, obsidian, 99]

        # calculate
        time = 24 if p == 1 else 32
        geodes = get_max_geodes(bp, max_resources, time, robots=[1, 0, 0, 0], materials=[0, 0, 0, 0], states={})

        if p == 1:
            total += id * geodes
        else:
            total *= geodes

    return total


print(p1 := calculate(1))
print(p2 := calculate(2))
