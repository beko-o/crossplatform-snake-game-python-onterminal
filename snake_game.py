import random
import sys
import os
import time

# Cross-platform keyboard input handling
try:
    import msvcrt  # Windows
    WINDOWS = True
except ImportError:
    import termios, tty, select  # Unix/Linux/Mac
    WINDOWS = False

class SnakeGame:
    def __init__(self, width=40, height=20):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2)]
        self.direction = (1, 0)  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        
        # Terminal setup for Unix systems
        if not WINDOWS:
            self.old_settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin.fileno())
    
    def generate_food(self):
        while True:
            food = (random.randint(1, self.width-2), random.randint(1, self.height-2))
            if food not in self.snake:
                return food
    
    def get_key(self):
        """Cross-platform non-blocking key input"""
        if WINDOWS:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                # Handle arrow keys on Windows
                if key == '\xe0':  # Special key prefix on Windows
                    key = msvcrt.getch().decode('utf-8')
                    if key == 'H':  # Up
                        return 'UP'
                    elif key == 'P':  # Down
                        return 'DOWN'
                    elif key == 'M':  # Right
                        return 'RIGHT'
                    elif key == 'K':  # Left
                        return 'LEFT'
                return key
            return None
        else:
            # Unix/Linux/Mac
            if select.select([sys.stdin], [], [], 0.1) == ([sys.stdin], [], []):
                key = sys.stdin.read(1)
                if key == '\x1b':  # ESC sequence
                    key += sys.stdin.read(2)
                    if key == '\x1b[A':
                        return 'UP'
                    elif key == '\x1b[B':
                        return 'DOWN'
                    elif key == '\x1b[C':
                        return 'RIGHT'
                    elif key == '\x1b[D':
                        return 'LEFT'
                return key
            return None
    
    def update_direction(self, key):
        # Handle both arrow keys and WASD
        if key in ['UP', 'w', 'W']:
            if self.direction != (0, 1):  # Can't go opposite direction
                self.direction = (0, -1)
        elif key in ['DOWN', 's', 'S']:
            if self.direction != (0, -1):
                self.direction = (0, 1)
        elif key in ['RIGHT', 'd', 'D']:
            if self.direction != (-1, 0):
                self.direction = (1, 0)
        elif key in ['LEFT', 'a', 'A']:
            if self.direction != (1, 0):
                self.direction = (-1, 0)
        elif key in ['q', 'Q']:
            self.cleanup()
            sys.exit(0)
    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.width-1 or 
            new_head[1] <= 0 or new_head[1] >= self.height-1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        # Check food collision
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
    
    def clear_screen(self):
        """Fast screen clearing using ANSI escape codes"""
        print('\033[2J\033[H', end='', flush=True)
    
    def draw(self):
        # Fast screen clear
        self.clear_screen()
        
        # Build entire screen as one string for faster output
        screen = []
        
        # Create game board
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Border
                if x == 0 or x == self.width-1 or y == 0 or y == self.height-1:
                    row.append('#')
                # Snake head
                elif (x, y) == self.snake[0]:
                    row.append('O')
                # Snake body
                elif (x, y) in self.snake:
                    row.append('o')
                # Food
                elif (x, y) == self.food:
                    row.append('*')
                # Empty space
                else:
                    row.append(' ')
            screen.append(''.join(row))
        
        # Print entire screen at once
        print('\n'.join(screen))
        
        # Print score and instructions
        print(f"\nScore: {self.score}")
        print("Use arrow keys or WASD to move, 'q' to quit")
        
        if self.game_over:
            print("\n*** GAME OVER ***")
            print("Press any key to exit...")
        
        # Force output immediately
        sys.stdout.flush()
    
    def cleanup(self):
        """Restore terminal settings (Unix only)"""
        if not WINDOWS:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
    
    def run(self):
        try:
            while not self.game_over:
                self.draw()
                
                # Get input
                key = self.get_key()
                if key:
                    self.update_direction(key)
                
                # Move snake
                self.move_snake()
                
                # Game speed (reduced for smoother gameplay)
                time.sleep(0.1)
            
            # Game over screen
            self.draw()
            
            # Wait for any key to exit
            if WINDOWS:
                msvcrt.getch()
            else:
                self.get_key()
            
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()

def main():
    print("Welcome to Terminal Snake!")
    print("Controls:")
    print("- Arrow keys OR WASD to move")
    print("- 'q' to quit")
    print("- Eat the food (*) to grow and score points")
    print("- Don't hit walls or yourself!")
    print(f"\nRunning on: {'Windows' if WINDOWS else 'Unix/Linux/Mac'}")
    print("\nPress Enter to start...")
    input()
    
    game = SnakeGame()
    game.run()

if __name__ == "__main__":
    main()