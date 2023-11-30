import os
import readchar
import random

class Game:
    def __init__(self, filename):
        self.WALL = "#"
        self.PATH = "."
        self.PLAYER = "P"
        self.px = 0
        self.py = 0
        self.maze, self.width, self.height, self.px, self.py = self.cargar_mapa(filename)
        self.GOAL = (self.width , self.height)
        
    def cargar_mapa(self, filename):
        with open(filename, "r") as f:
            px, py, width, height = map(int, f.readline().strip().split())
            maze = [list(line.strip()) for line in f.readlines()]
            
            print(f"Ancho: {width}, Alto: {height}")
            
        return maze, width, height, px, py



    def mostrar_mapa(self):
        for row in self.maze:
            print(" ". join(row))
    
    def obtener_posicion(self):
        return self.GOAL
    
    def datos_mapa(self):
        map_data = ""
        for row in self.maze:
            map_data += "".join(row) + "\n"

        return map_data.strip()
    
    def obtener_dimensiones(self):
        return self.width, self.height
                  
    def pos_jugador(self, x, y, dx, dy):
        maze_width = self.width + 1
        maze_height = self.height + 1
        
        if x + dx < 0 or x + dx >= maze_width or y + dy < 0 or y + dy >= maze_height:
            return
        
        if (x + dx, y + dy) == self.obtener_posicion():
            print("Felicidades, has completado el juego")
            exit()
        
        if self.maze[y + dy][x + dx] == self.PATH:
            self.maze[y][x] = self.PATH
            self.maze[y + dy][x + dx] = self.PLAYER
            self.px = x + dx
            self.py = y + dy
        
    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.mostrar_mapa()
            
            key = readchar.readkey()

            if key == "q":
                break
            elif key.lower() == "a" or key == readchar.key.LEFT:
                self.pos_jugador(self.px, self.py, -1, 0)
            elif key.lower() == "s" or key == readchar.key.DOWN:
                self.pos_jugador(self.px, self.py, 0, 1)
            elif key.lower() == "d" or key == readchar.key.RIGHT:
                self.pos_jugador(self.px, self.py, 1, 0)
            elif key.lower() == "w" or key == readchar.key.UP:
                self.pos_jugador(self.px, self.py, 0, -1)

class GameFiles(Game):
    def __init__(self, filenames):
        selected_filename = random.choice(filenames)        
        super().__init__(selected_filename)
        
def main():
    game = GameFiles(["mapa1.txt", "mapa2.txt"])
    game.run()

if __name__ == "__main__":
    main()
