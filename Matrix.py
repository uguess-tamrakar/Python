class Matrix:
    def bunniesEscape(map):
        # we were at 0,0 > we can go to next space at the right or bottom
        coords = []
        coords.append((0, 0, 0))
        src_dest = Matrix.__marchForward(map, coords)

        # we are at
        coords = []
        coords.append((0, len(map) - 1, len(map[0]) - 1))
        dest_src = Matrix.__marchForward(map, coords)

        res = [
            sum(r) - 1 for i, _ in enumerate(map) for r in zip(src_dest[i], dest_src[i])
        ]
        return min(res)

    def __marchForward(map, coords):
        # hold all the visited spots (spaces/walls); initialized to 0
        memo = [999] * len(map)
        for i in range(len(map)):
            memo[i] = [999] * len(map[i])

        while len(coords) > 0:
            curr_coord = coords.pop(0)
            prev_num_paths, i, j = curr_coord
            # if already visited (indicated by > 0 because every step calculates number of paths taken)
            # and if new calculated number of paths is greater than prev then skip
            if memo[i][j] == 999:
                memo[i][j] = prev_num_paths + 1
                if map[i][j] == 0:
                    if i > 0:
                        coords.append((memo[i][j], i - 1, j))
                    if j > 0:
                        coords.append((memo[i][j], i, j - 1))
                    if i < len(map) - 1:
                        coords.append((memo[i][j], i + 1, j))
                    if j < len(map[0]) - 1:
                        coords.append((memo[i][j], i, j + 1))
        return memo

    def bunnies_escape_test():
        assert (
            Matrix.bunniesEscape(
                [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 1, 0]]
            )
            == 8
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                ]
            )
            == 9
        )

        # assert solution([
        #     [0, 1, 0, 0, 0],
        #     [0, 0, 0, 1, 0],
        #     [0, 0, 1, 1, 1],
        #     [0, 1, 1, 0, 0],
        #     [0, 1, 1, 0, 0]
        # ]) == 11

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                ]
            )
            == 14
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0],
                ]
            )
            == 13
        )

        assert (
            Matrix.bunniesEscape(
                [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
            )
            == 7
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                ]
            )
            == 11
        )

        assert Matrix.bunniesEscape([[0, 0], [0, 0]]) == 3

        assert Matrix.bunniesEscape([[0, 0], [0, 1]]) == 3

        # 0 0 0 0 0 0
        # 0 1 1 1 1 0
        # 0 0 0 0 0 0
        # 0 1 1 1 1 1
        # 0 1 1 1 1 1
        # 0 0 0 0 0 0

        assert (
            Matrix.bunniesEscape(
                [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 1, 1, 0]]
            )
            == 8
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                ]
            )
            == 9
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                ]
            )
            == 11
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 1, 1],
                    [0, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0],
                ]
            )
            == 14
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0],
                ]
            )
            == 13
        )

        assert (
            Matrix.bunniesEscape(
                [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
            )
            == 7
        )

        assert (
            Matrix.bunniesEscape(
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                ]
            )
            == 11
        )

        assert Matrix.bunniesEscape([[0, 0], [0, 0]]) == 3

        assert Matrix.bunniesEscape([[0, 0], [0, 1]]) == 3

    def distance(map):
        # count up distance to each node from start location
        notseen = 999
        d = [
            [1 if i == j == 0 else notseen for j in range(len(row))]
            for i, row in enumerate(map)
        ]

        q = [(0, 0)]
        while q:
            x, y = q.pop(0)
            for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + move[0], y + move[1]
                if 0 <= x2 < len(d) and 0 <= y2 < len(d[0]):
                    if d[x2][y2] == notseen:
                        d[x2][y2] = d[x][y] + 1
                        if not map[x2][y2]:
                            q.append((x2, y2))
        return d

    def flip(map):
        # flip a map to have the "end" at (0,0)
        return [[v for v in reversed(row)] for row in reversed(map)]

    def solution(map):
        # find the distances starting from both entrance and exit
        b = Matrix.distance(map)
        e = Matrix.flip(Matrix.distance(Matrix.flip(map)))
        # add the distances and find the shortest point where they intersect
        res = [sum(v) - 1 for i, _ in enumerate(map) for v in zip(b[i], e[i])]
        return min(res)
