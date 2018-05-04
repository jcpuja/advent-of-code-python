class CircularList:
    def __init__(self, list_size):
        self.list = list(range(list_size))

    def get_list(self):
        return self.list

    def reverse(self, position, length):
        list_length = len(self.list)

        if not 0 <= position < list_length:
            raise Exception('Start position for reverse is out of bounds: list_length='
                            + str(list_length) + ', position=' + str(position))

        if not 0 <= length <= list_length:
            raise Exception('Slice length for reverse is out of bounds: list_length='
                            + str(list_length) + ', length=' + str(length))

        if length <= 1:
            # short-circuit return
            return

        end_index = position + length

        if end_index <= list_length:
            slice_to_reverse = self.list[position:end_index]
            slice_to_reverse.reverse()
            self.list[position:end_index] = slice_to_reverse

        else:
            actual_end_index = end_index % list_length

            right_slice = self.list[position:]
            left_slice = self.list[:actual_end_index]

            slice_to_reverse = right_slice + left_slice
            slice_to_reverse.reverse()

            self.list[position:] = slice_to_reverse[:len(right_slice)]
            self.list[:actual_end_index] = slice_to_reverse[-1 * len(left_slice):]
            # times -1 means "len(left_slice) chars from the right of slice_to_reverse"

    def get_actual_position(self, position):
        if position < 0:
            raise Exception('The given position to compute must be positive: position=' + str(position))

        return position % len(self.list)
