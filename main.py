from world.map import Map
import time


def main():
    game_map = Map(10, 10)

    for turn in range(10):
        print(f"\nTurn {turn + 1}")
        game_map.display()
        game_map.simulate_turn()
        time.sleep(1)


if __name__ == "__main__":
    main()