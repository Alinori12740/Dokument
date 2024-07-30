class Field:
    def __init__(self, position, color):
        self.position = position
        self.color = color


class Game:
    def __init__(self, width=3, height=3, win=3):
        self.width = width
        self.height = height
        self.win = win
        self.board = [[None for _ in range(width)] for _ in range(height)]
        self.count_fields = 0
        self.game_status = "active"
        self.turn_color = None
        self.won_by = None

    def ascii(self):
        return (
            "\n"
            + "\n".join(
                [
                    "".join([cell.color if cell else "." for cell in row])
                    for row in self.board[::-1]
                ]
            )
            + "\n"
        )

    def drop(self, color, column):
        if self.game_status != "active":
            raise Exception("Game is over")
        if self.turn_color and color != self.turn_color:
            raise Exception(f"It's {self.turn_color}'s turn")
        for row in range(self.height):
            if self.board[row][column] is None:
                field = Field((column, row), color)
                self.board[row][column] = field
                self.count_fields += 1
                self.turn_color = "o" if color == "x" else "x"
                self._check_win(field)
                return field
        raise Exception("Column is full")

    def _check_win(self, field):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for direction in [1, -1]:
                x, y = field.position
                while True:
                    x, y = x + direction * dx, y + direction * dy
                    if (
                        0 <= x < self.width
                        and 0 <= y < self.height
                        and self.board[y][x]
                        and self.board[y][x].color == field.color
                    ):
                        count += 1
                    else:
                        break
            if count >= self.win:
                self.game_status = "over"
                self.won_by = field.color
                return

    def axis_strings(self, x, y):
        vertical = "".join([row[x].color if row[x] else "." for row in self.board])
        horizontal = "".join([cell.color if cell else "." for cell in self.board[y]])
        diagonal1 = self.board[y][x].color if self.board[y][x] else "."
        diagonal2 = "".join(
            [
                self.board[y - i][x + i].color
                if 0 <= y - i < self.height
                and 0 <= x + i < self.width
                and self.board[y - i][x + i]
                else "."
                for i in range(min(self.height, self.width))
            ]
        )
        return [vertical, diagonal1, diagonal2, horizontal]

    @staticmethod
    def load(ascii_game):
        lines = ascii_game.strip().split("\n")
        height = len(lines)
        width = len(lines[0])
        game = Game(width, height)
        for y, line in enumerate(lines[::-1]):
            for x, char in enumerate(line):
                if char != ".":
                    game.board[y][x] = Field((x, y), char)
        return game