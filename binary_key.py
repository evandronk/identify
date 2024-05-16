from dataclasses import dataclass
texto = []
texto.clear()

texto.insert(0, ["0,0",
                 "0,1"])

texto.insert(1, ["1,0",
                 "1,1",
                 "1,2",
                 "1,3"])

texto.insert(2, ["2,0",
                 "2,1",
                 "2,2",
                 "2,3",
                 "2,4",
                 "2,5",
                 "2,6",
                 "2,7",])

texto.insert(3, ["3,0",
                 "3,1",
                 "3,2",
                 "3,3",
                 "3,4",
                 "3,5",
                 "3,6",
                 "3,7",
                 "3,8",
                 "3,9",
                 "3,10",
                 "3,11",
                 "3,12",
                 "3,13",
                 "3,14",
                 "3,15",
                 ])

texto.insert(4, ["4,0",
                 "4,1",
                 "4,2",
                 "4,3",
                 "4,4",
                 "4,5",
                 "4,6",
                 "4,7",
                 "4,8",
                 "4,9",
                 "4,10",
                 "4,11",
                 "4,12",
                 "4,13",
                 "4,14",
                 "4,15",
                 "4,16",
                 "4,17",
                 "4,18",
                 "4,19",
                 "4,20",
                 "4,21",
                 "4,22",
                 "4,23",
                 "4,24",
                 "4,25",
                 "4,26",
                 "4,27",
                 "4,28",
                 "4,29",
                 "4,30",
                 "4,31",
                 ])

@dataclass
class Key:
    index_i: int
    index_j: int
    index_j2: int
    prev_i: int
    prev_j: int
    texts: []
    identified: bool

    def __init__(self):
        self.index_i = 0
        self.index_j = 0
        self.index_j2 = 1
        self.prev_i = 0
        self.prev_j = 0
        self.texts = texto
        self.identified = False


def __get_text__(i, j):
    return texto[i][j]
