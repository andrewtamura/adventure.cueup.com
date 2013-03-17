'''
Challenge #3 from http://adventure.cueup.com/

Andrew Tamura
March 16, 2013

n, e, e, n, e, e, w, n, n, e

'''


def main():
    troll_map = TrollMap()
    troll_map.solve(35)        
        
class Move():
    position = None
    
    def __init__(self, position):
        self.position = position
            
        
class TrollMap():

    map = [ [8, 8, 4, 4, 5], 
            [4, 9, 6, 4, 8], 
            [8, 6, 4, 1, 2], 
            [4, 8, 2, 6, 3], 
            [0, 6, 8, 8, 4] ]
    start_pos = (4, 0)
    end_pos = (0, 4)
    start_tokens = 35
    move_queue = []

    def __init__(self):
        pass
        
    def solve(self, tokens_left):
        for move in self.get_valid_moves():
            self.move_queue.append(move)
            
    def get_valid_moves(self, position, tokens):
        valid_moves = []
        if self.current_pos == self.end_pos:
            return None
        if self.current_pos[0] > 0:
            valid_moves.append(self.north)
        if self.current_pos[0] < 3:
            valid_moves.append(self.south)
        if self.current_pos[1] > 0:
            valid_moves.append(self.east)
        if self.current_pos[1] < 3:
            valid_moves.append(self.west)
        return valid_moves

    def north(self):
        new_pos = self.current_pos[0]-1, self.current_pos[1]
        return Move(new_pos)
        
    def south(self):
        new_pos = self.current_pos[0]+1, self.current_pos[1]
        return Move(new_pos)

    def east(self):
        new_pos = self.current_pos[0], self.current_pos[1]+1
        return Move(new_pos)

    def west(self):
        new_pos = self.current_pos[0], self.current_pos[1] - 1
        return Move(new_pos)

if __name__ == '__main__':
    main()



