

def main() -> None:
    
    count: int = 0
    with open("input.txt", 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            differences = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

            if all(1 <= abs(diff) <= 3 for diff in differences):
                if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
                    count += 1

                
    print(f"1st: {count}")


if __name__ == '__main__':
    main()