import math
import numpy as np


class SpiralMemory:
    # The matrix holding the spiral structure
    matrix: np.ndarray
    mapped_matrix: np.ndarray
    edge_size: int
    edge_center_index: int
    max_index_overflow = 0

    # Map to quickly retrieve coordinates by index
    coordinates_by_index = {}

    @staticmethod
    def calculate_edge_size(max_index):
        edge_size = math.ceil(math.sqrt(max_index))
        if edge_size % 2 == 0:
            edge_size += 1
        return edge_size

    def __init__(self, max_index: int):
        # The matrix will be of size ceil(sqrt(i)) (if odd, +1 if even) for a given index i
        self.edge_size = int(self.calculate_edge_size(max_index))

        # Init zero-matrix to the calculated size
        self.matrix = np.zeros((self.edge_size, self.edge_size))
        self.mapped_matrix = np.zeros((self.edge_size, self.edge_size))

        # Calculate matrix center and initialize cursor to it
        # size divided by 2, next integer, -1 because 0-indexed array
        self.edge_center_index: int = math.floor(self.edge_size / 2)
        fill_cursor = (self.edge_center_index, self.edge_center_index)

        directions = ['right', 'up', 'left', 'down']

        # Current length of an edge. Will grow by n^2
        edge_length = 1

        # Number of items filled in the current edge. Max = edge_length.
        # When we have filled the whole edge, we switch directions
        items_in_edge_filled = 0

        # Number of edges filled, up to 4. When we have filled the 4th edge, we increment edge size
        # Initialized to 3 because we want to increment edge size right after filling 1
        number_of_edges_filled = 3

        # Index of the current direction in the directions array. We're starting towards the right
        current_direction = 0

        def cursor_up(cursor: tuple):
            return cursor[0] - 1, cursor[1]

        def cursor_down(cursor: tuple):
            return cursor[0] + 1, cursor[1]

        def cursor_left(cursor: tuple):
            return cursor[0], cursor[1] - 1

        def cursor_right(cursor: tuple):
            return cursor[0], cursor[1] + 1

        moves = {
            'up': cursor_up,
            'down': cursor_down,
            'left': cursor_left,
            'right': cursor_right,
        }

        def count_neighbors(cursor: tuple) -> int:
            def count_row(row_index, ref_y) -> int:
                row_sum = 0
                if ref_y > 0:
                    row_sum += self.mapped_matrix[row_index, ref_y - 1]

                row_sum += self.mapped_matrix[row_index, ref_y]

                if ref_y < self.edge_size - 1:
                    row_sum += self.mapped_matrix[row_index, ref_y + 1]

                return row_sum

            (x, y) = cursor
            neighbors_sum = 0
            if x > 0:
                neighbors_sum += count_row(x - 1, y)

            neighbors_sum += count_row(x, y)

            if x < self.edge_size - 1:
                neighbors_sum += count_row(x + 1, y)

            return neighbors_sum

        for i in range(1, max_index + 1):
            self.matrix[fill_cursor[0], fill_cursor[1]] = i
            neighbors_sum = 1 if i == 1 else count_neighbors(fill_cursor)
            self.mapped_matrix[fill_cursor[0], fill_cursor[1]] = neighbors_sum
            if self.max_index_overflow == 0 and neighbors_sum > max_index:
                self.max_index_overflow = neighbors_sum

            self.coordinates_by_index[i] = fill_cursor

            items_in_edge_filled += 1

            if items_in_edge_filled >= edge_length:
                # Edge is filled => switch directions
                number_of_edges_filled += 1

                # Switch directions after filling an edge.
                # If we're in the special case of filling the 4th edge, we want to go one more step in the same
                # direction, and THEN change direction.
                if number_of_edges_filled < 4 or number_of_edges_filled == 5:
                    current_direction = (current_direction + 1) % 4
                    items_in_edge_filled = 1

                    if number_of_edges_filled == 5:
                        # We've filled the 4th edge and the extra step, so we increase the edge size
                        number_of_edges_filled = 0
                        edge_length = self.calculate_edge_size(i)
                        # Pretend we already filled 2 (the one we just filled, + the one 'below'
                        # which will be filled gon the 4th edge
                        items_in_edge_filled = 2

            fill_cursor = moves[directions[current_direction]](fill_cursor)

    def get_matrix_shape(self):
        return self.matrix.shape

    def debug(self):
        print(self.matrix)

    def get_origin_coordinates(self) -> tuple:
        """Get coordinates for the origin, ie. the 1 index (the 'center' of the spiral)
        :returns a Tuple containing the 0-based, x, y coordinates relative to the top left most element of the matrix"""
        return self.edge_center_index, self.edge_center_index

    def get_coordinates(self, index) -> tuple:
        """Get coordinates for the given index
        :returns a Tuple containing the 0-based, x, y coordinates relative to the top left most element of the matrix"""
        return self.coordinates_by_index[index]


def get_spiral_memory_steps(index: int):
    # Init matrix
    m = SpiralMemory(index)

    coordinates_index = m.get_coordinates(index)
    coordinates_origin = m.get_origin_coordinates()

    return math.fabs(coordinates_index[0] - coordinates_origin[0]) \
        + math.fabs(coordinates_index[1] - coordinates_origin[1])


def get_max_index_overflow(index: int):
    m = SpiralMemory(index)

    return m.max_index_overflow


# print(get_spiral_memory_steps(368078))
# print(get_max_index_overflow(368078))
