'''
Challenge #3 from http://adventure.cueup.com/

Andrew Tamura
March 16, 2013

n, e, e, n, e, e, w, n, n, e

'''


def main():
    troll_map = TrollMap()
    troll_map.solve(35, (4,0), [(4,0)])     
        
class Move():
    position = None
    
    def __init__(self, position):
        self.position = position
            
        
class TrollMap():

    maze = [ [8, 8, 4, 4, 5], 
            [4, 9, 6, 4, 8], 
            [8, 6, 4, 1, 2], 
            [4, 8, 2, 6, 3], 
            [0, 6, 8, 8, 4] ]
    height = len(maze)
    width = len(maze[0])
    start_pos = (4, 0)
    end_pos = (0, 4)
    start_tokens = 35
    move_queue = []
    
    def __init__(self):
        pass
    
    def get_value(self, position):
        row, column = position
        return self.maze[row][column]
        
    def solve(self, tokens, position, move_history=None):
        if not move_history:
            move_history = []
        for move in self.get_valid_moves(position):
            new_token_count = tokens - self.get_value(move)
            new_path = list(move_history)
            new_path.append(move)
            if new_token_count > 0:
                self.solve(new_token_count, move, new_path)
            elif new_token_count == 0 and move == self.end_pos:
                print new_path
                        
    def get_valid_moves(self, position):
        valid_moves = []
        if self.getNorth(position):
            valid_moves.append(self.getNorth(position))
        if self.getSouth(position):
            valid_moves.append(self.getSouth(position))
        if self.getEast(position):
            valid_moves.append(self.getEast(position))
        if self.getWest(position)  :
            valid_moves.append(self.getWest(position))
        return valid_moves

    def getNorth(self, position):
        if position[0]-1 >= 0:
            new_pos = position[0]-1, position[1]
            return new_pos
        else:
            return None
                
    def getSouth(self, position):
        if position[0]+1 < self.height:
            new_pos = position[0]+1, position[1]
            return new_pos
        else:
            return None

    def getEast(self, position):
        if position[1]+1 < self.width:
            new_pos = position[0], position[1]+1
            return new_pos
        else:
            return None

    def getWest (self, position):
        if position[1]-1 >=0 :
            new_pos = position[0], position[1]-1
            return new_pos
        else:
            return None

if __name__ == '__main__':
    main()



