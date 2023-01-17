from collections import namedtuple
import copy


Entry = namedtuple("Entry", ["row1", "col1", "row2", "col2", "value"])


class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, new_value: int
    ) -> None:
        # NOTE: This can potentially end in TLE
        # I think there's a solution to use prefix sums
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = new_value

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


class SubrectangleQueriesOpt:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = copy.deepcopy(rectangle)
        self.history: list[Entry] = []

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, new_value: int
    ) -> None:
        self.history.append(
            Entry(row1=row1, row2=row2, col1=col1, col2=col2, value=new_value)
        )

    def getValue(self, row: int, col: int) -> int:
        for entry in reversed(self.history):
            if entry.row1 <= row <= entry.row2 and entry.col1 <= col <= entry.col2:
                return entry.value

        return self.rectangle[row][col]
