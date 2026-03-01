from world.map import Map
import time
import argparse


def main():
    parser = argparse.ArgumentParser(description="Terminal Civilization Engine")
    parser.add_argument("--size", type=int, default=10, help="Map size (NxN)")
    args = parser.parse_args()

    game_map = Map(args.size, args.size)

    turn = 0
    while True:
        turn += 1
        print(f"\nTurn {turn}")
        game_map.display()
        game_map.print_statistics()

        winner = game_map.check_victory()
        if winner:
            print(f"\n🏆 {winner.name} wins the world!")
            break

        game_map.simulate_turn()
        time.sleep(1)


if __name__ == "__main__":
    main()