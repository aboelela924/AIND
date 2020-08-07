from utils import *
import numpy as np
from collections import Counter
import copy

# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)

grid = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."

def grid_values(grid):
    if len(grid) != 81:
        print("Grid must be 81 length")
    else:
        return dict(zip(boxes, grid))





def eliminate(grid_dict):
    for item in boxes:
        if grid_dict[item] == ".":
            available_numbers = ""
            used =""
            for peer in peers[item]:
                if len(grid_dict[peer]) == 1 and not grid_dict[peer] == ".":
                    used = used + str(grid_dict[peer])

            for i in range(1,10):
                if str(i) not in used:
                    available_numbers = available_numbers + str(i)

            grid_dict[item] = available_numbers
    return grid_dict

def only_choice(values):

    for unit in square_units:

        list_unit_sets = []
        super_list = []
        occuared_once = []

        for square in unit:
            number_in_square = values[square]
            number_list = list(number_in_square)
            if len(number_list) > 1:
                list_unit_sets.append(set(number_list))
            else:
                for i in range(10):
                    list_unit_sets.append(set(number_list))

        for nums in list_unit_sets:
            super_list.extend(nums)


        for key, value in Counter(super_list).items():
            if value == 1:
                occuared_once.append(key)

        for unique_num in occuared_once:
            for square in unit:
                number_in_square = values[square]
                if unique_num in number_in_square:
                    values[square] = unique_num


    # for unit in unitlist:
    #     for digit in "123456789":
    #         places_of_occurance = [box for box in unit if digit in values[box]]
    #         if len(places_of_occurance) == 1:
    #             values[places_of_occurance[0]] = digit


    return values

def recreate_grid(values):
    grid = ""
    for key in values:
        value = values[key]
        if len(value) > 1:
            grid +="."
        else:
            grid += value
    return grid

def isSolved(values):
    for key in values:
        value = values[key]
        if not len(value) == 1:
            return False
    return True

def search(grid):
    if len(grid) < 81:
        return False

    filled = grid_values(grid)
    values = eliminate(filled)
    only_choice_result = only_choice(values)
    grid = recreate_grid(only_choice_result)
    if not isSolved(only_choice_result):

        sudoku_board = {k: v for k, v in sorted(only_choice_result.items(), key=lambda item: len(item[1])) if len(v) > 1}

        for key in sudoku_board:
            value = sudoku_board[key]
            probabale_values = list(value)
            for probabale_value in probabale_values:
                sudoku_board_copy = copy.deepcopy(only_choice_result)
                sudoku_board_copy[key] = probabale_value
                grid = recreate_grid(sudoku_board_copy)
                result = search(grid)
                if result:
                    return result
    else:
        return only_choice_result



display(search(grid))
