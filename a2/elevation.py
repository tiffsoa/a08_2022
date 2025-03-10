"""Assignment 2 functions."""

from copy import deepcopy

THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]

EPSILON = 0.005


def compare_elevations_within_row(elevation_map: list[list[int]], map_row: int,
                                  level: int) -> list[int]:
    """Return a new list containing the three counts: the number of
    elevations from row number map_row of elevation map elevation_map
    that are less than, equal to, and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]

    """
    sublist = []
    smaller = 0
    equal = 0
    bigger = 0
    sublist.extend(elevation_map[map_row])
    for item in sublist:
        if item < level:
            smaller += 1
        elif item > level:
            bigger += 1
        else:
            equal += 1
    return [smaller, equal, bigger]


def update_elevation(elevation_map: list[list[int]], start: list[int],
                     stop: list[int], delta: int) -> None:

    """
    >>> THREE_BY_THREE_COPY = deepcopy(THREE_BY_THREE)
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = deepcopy(FOUR_BY_FOUR)
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    """
    for item in range(start[0], stop[0] + 1):
        for num in range(start[1], stop[1] + 1):
            elevation_map[item][num] += delta


def get_average_elevation(elevation_map: list[list[int]]) -> float:
    """Return the average elevation across the cells in the given
    elevation map.

    Precondition: the given elevation map is valid map.

    >>> abs(get_average_elevation(UNIQUE_3X3) - 5.0) < EPSILON
    True
    >>> abs(get_average_elevation(FOUR_BY_FOUR) - 3.8125) < EPSILON
    True
    """
    new_list = []
    count = 0
    for item in elevation_map:
        for num in item:
            new_list.append(num)
    for num in new_list:
        count += 1
    return sum(new_list) / count


def find_peak(elevation_map: list[list[int]]) -> list[int]:
    """Return the cell which contains the highest elevation point in the given
    map.

    Precondition: the given elevation map is valid and all values in the map
    are unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    """
    all_values = []
    i = 0
    j = 0
    for item in elevation_map:
        for cell in item:
            all_values.append(cell)
    for item in elevation_map:
        for cell in item:
            if cell == max(all_values):
                i += item.index(max(all_values))
                j += elevation_map.index(item)
    return [j, i]


def is_sink(elevation_map: list[list[int]], cell: list[int]) -> bool:
    """Return True iff the given cell is a sink in the given elevation_map.
    A cell is a sink if it has lower values than its adjacent cells.

    >>> is_sink(UNIQUE_3X3, [2, 0])
    True
    >>> is_sink(UNIQUE_3X3, [0, 0])
    True
    >>> is_sink(UNIQUE_3X3, [1, 1])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(UNIQUE_4X4, [3, 3])
    False
    """
    for item in get_adjacent_cells(cell, len(elevation_map)):
        if not is_cell_lower(elevation_map, cell, item):
            return False
    return True


def find_local_sink(elevation_map: list[list[int]],
                    cell: list[int]) -> list[int]:
    """Return the local sink for the given cell in elevation_map. The local
    sink is the cell to which the water from the given cell will flow.

    Precondition: elevation_map is a valid map, cell exists in
    elevation_map and all values of the given map are unique.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [1, 2])
    [0, 1]
    >>> find_local_sink(FOUR_BY_FOUR, [1, 1])
    [0, 0]
    >>> find_local_sink(THREE_BY_THREE, [2, 2])
    [1, 2]
    >>> find_local_sink(THREE_BY_THREE, [1, 2])
    [0, 2]
    """
    adjacent_cells = get_adjacent_cells(cell, len(elevation_map))
    low = adjacent_cells[0]
    for item in adjacent_cells:
        if elevation_map[low[0]][low[1]] > elevation_map[item[0]][item[1]]:
            low = item
    return low


def can_hike_to(elevation_map: list[list[int]], start: list[int],
                dest: list[int], supplies: int) -> bool:
    """Return True if hiker can reach final destination dest. Note that
    hiker can get there only if supplies are enough. The change in movement
    will be deducted from the initial number of supplies as hiker moves to the
    north or the west.

    Precondition: elevation_map is a valid map, start and dest exist in
    elevation_map and supplies in a positive integer.

    >>> can_hike_to(THREE_BY_THREE, [2, 2], [1, 1], 13)
    True
    >>> can_hike_to(FOUR_BY_FOUR, [3, 2], [0, 0], 5)
    False
    >>> can_hike_to(UNIQUE_3X3, [1, 2], [1, 0], 3)
    True
    >>> can_hike_to(UNIQUE_4X4, [1, 3], [0, 2], 6)
    False
    >>> can_hike_to(UNIQUE_3X3, [0, 1], [0, 0], 18)
    True
    >>> can_hike_to(FOUR_BY_FOUR, [3, 3], [0, 0], 14)
    True
    """
    d_n = abs(elevation_map[start[0]][start[1]] -
              elevation_map[start[0] - 1][start[1]])
    d_w = abs(elevation_map[start[0]][start[1]] -
              elevation_map[start[0]][start[1] - 1])

    while [start[0], start[1]] != [dest[0], dest[1]]:
        if abs(dest[1]-start[1]) == 0:
            supplies -= d_n
            start[0] -= 1
        elif abs(dest[0]-start[0]) == 0:
            supplies -= d_w
            start[1] -= 1
        elif d_n <= d_w:
            supplies -= d_n
            start[0] -= 1
        else:
            supplies -= d_w
            start[1] -= 1
        d_n = abs(elevation_map[start[0]][start[1]] -
                  elevation_map[start[0] - 1][start[1]])
        d_w = abs(elevation_map[start[0]][start[1]] -
                  elevation_map[start[0]][start[1] - 1])
        abs(dest[0]-start[0])
        abs(dest[1]-start[1])
    return 0 <= supplies


def get_lower_resolution(elevation_map: list[list[int]]) -> list[list[int]]:
    """Return a new 2X2 elevation_map that contains the average elevation of
    each 2X2 section of the given elevation_map.

    Precondition: elevation_map is a valid map.

    >>> get_lower_resolution(FOUR_BY_FOUR)
    [[3, 4], [4, 3]]
    >>> get_lower_resolution(THREE_BY_THREE)
    [[3, 3], [7, 9]]
    >>> get_lower_resolution(UNIQUE_3X3)
    [[5, 5], [4, 6]]
    >>> get_lower_resolution(UNIQUE_4X4)
    [[7, 12], [9, 12]]
    >>> get_lower_resolution(FOUR_BY_FOUR)
    [[3, 4], [4, 3]]
    """
    low = []
    for i in range(0, len(elevation_map), 2):
        two_two = []
        for j in range(0, len(elevation_map), 2):
            avg = []
            if is_valid_cell([i, j], len(elevation_map)):
                avg.append(elevation_map[i][j])
            if is_valid_cell([i, j+1], len(elevation_map)):
                avg.append(elevation_map[i][j+1])
            if is_valid_cell([i+1, j], len(elevation_map)):
                avg.append(elevation_map[i+1][j])
            if is_valid_cell([i+1, j+1], len(elevation_map)):
                avg.append(elevation_map[i+1][j+1])
            two_two.append(sum(avg) // len(avg))
        low.append(two_two)
    return low


def is_valid_cell(cell: list[int], dimension: int) -> bool:
    """Return True if and only if cell is a valid cell in an elevation map
    of dimensions dimension x dimension.

    Precondition: cell is a list of length 2.

    >>> is_valid_cell([1, 1], 2)
    True
    >>> is_valid_cell([0, 2], 2)
    False

    """
    return (0 <= cell[0] <= dimension - 1) and (0 <= cell[1] <= dimension - 1)


def is_cell_lower(elevation_map: list[list[int]], cell_1: list[int],
                  cell_2: list[int]) -> bool:
    """Return True iff cell_1 has a lower elevation than cell_2.

    Precondition: elevation_map is a valid elevation map
                  cell_1 and cell_2 are valid cells in elevation_map

    >>> map = [[0, 1], [2, 3]]
    >>> is_cell_lower(map, [0, 0], [1, 1])
    True
    >>> is_cell_lower(map, [1, 1], [0, 0])
    False

    """
    i = cell_1[0]
    j = cell_1[1]
    i_2 = cell_2[0]
    j_2 = cell_2[1]
    return elevation_map[i][j] < elevation_map[i_2][j_2]


def get_adjacent_cells(cell: list[int], dimension: int) -> list[list[int]]:
    """Return a list of cells adjacent to cell in an elevation map with
    dimensions dimension x dimension.

    Precondition: cell is a valid cell for an elevation map with
                  dimensions dimension x dimension.

    >>> adjacent_cells = get_adjacent_cells([1, 1], 3)
    >>> adjacent_cells.sort()
    >>> adjacent_cells
    [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
    >>> adjacent_cells = get_adjacent_cells([1, 0], 3)
    >>> adjacent_cells.sort()
    >>> adjacent_cells
    [[0, 0], [0, 1], [1, 1], [2, 0], [2, 1]]

    """
    adjacent_cells = []
    i = cell[0]
    j = cell[1]
    possible_cells = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j+1],
                      [i+1, j-1], [i+1, j], [i+1, j+1]]
    for item in possible_cells:
        if is_valid_cell(item, dimension):
            adjacent_cells.append(item)
    return adjacent_cells


if __name__ == '__main__':
    import doctest
    doctest.testmod()
