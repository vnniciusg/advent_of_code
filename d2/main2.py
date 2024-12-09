

def main() -> None:
    
    count: int = 0
    with open("input.txt", 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            differences = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

            if all(1 <= abs(diff) <= 3 for diff in differences) and \
            (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)):
                count += 1
                continue

            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i + 1:]
                differences = [modified_levels[j] - modified_levels[j - 1] for j in range(1, len(modified_levels))]
                
                if all(1 <= abs(diff) <= 3 for diff in differences) and \
                (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)):
                    count += 1
                    break
                
    print(f"2nd: {count}")


if __name__ == '__main__':
    main()