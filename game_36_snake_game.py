import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def snake_game():
    try:
        import curses
        import random
        import time
    except ImportError:
        print("🐍 Snake Game requires 'curses' module")
        print("On Windows, you might need to install windows-curses:")
        print("pip install windows-curses")
        return

    def main(stdscr):
        curses.curs_set(0)
        sh, sw = stdscr.getmaxyx()
        w = curses.newwin(sh, sw, 0, 0)
        w.keypad(1)
        w.timeout(100)

        # Initial snake position
        snake_x = sw // 4
        snake_y = sh // 2
        snake = [
            [snake_y, snake_x],
            [snake_y, snake_x - 1],
            [snake_y, snake_x - 2]
        ]

        # Food position
        food = [sh // 2, sw // 2]
        w.addch(food[0], food[1], curses.ACS_PI)

        # Initial direction
        key = curses.KEY_RIGHT
        score = 0

        while True:
            next_key = w.getch()
            key = key if next_key == -1 else next_key

            # Check if snake hits wall or itself
            if (snake[0][0] in [0, sh-1] or 
                snake[0][1] in [0, sw-1] or 
                snake[0] in snake[1:]):
                w.addstr(sh//2, sw//2 - 5, "GAME OVER!")
                w.refresh()
                time.sleep(2)
                break

            # Calculate new head position
            new_head = [snake[0][0], snake[0][1]]

            if key == curses.KEY_DOWN:
                new_head[0] += 1
            if key == curses.KEY_UP:
                new_head[0] -= 1
            if key == curses.KEY_LEFT:
                new_head[1] -= 1
            if key == curses.KEY_RIGHT:
                new_head[1] += 1

            snake.insert(0, new_head)

            # Check if snake eats food
            if snake[0] == food:
                score += 10
                food = None
                while food is None:
                    nf = [
                        random.randint(1, sh-2),
                        random.randint(1, sw-2)
                    ]
                    food = nf if nf not in snake else None
                w.addch(food[0], food[1], curses.ACS_PI)
            else:
                tail = snake.pop()
                w.addch(tail[0], tail[1], ' ')

            # Draw snake
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
            
            # Display score
            w.addstr(0, 2, f"Score: {score}")
            w.refresh()

    print("🐍 Snake Game 🐍")
    print("=" * 40)
    print("Use arrow keys to move")
    print("Press Ctrl+C to quit")
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nGame ended by user")

# 37. 🏓 Pong (simplified terminal version)


if __name__ == "__main__":
    snake_game()
