
from collections import defaultdict

def main() -> None:

    left = []
    right = []
    with open("input.txt", 'r') as file:
        for line in file:
            pair = line.split()
            left.append(int(pair[0]))
            right.append(int(pair[1]))

    left.sort()
    right.sort()

    answer: int = sum(abs(l - r) for l, r in zip(left, right))
    print(f"1st part: {answer}")

    count_dict = defaultdict(int)
    for num in left:
        count_dict[num] += right.count(num)
    
    answer_2 = sum(num * count for num, count in count_dict.items())
    print(f"2nd part: {answer_2}")
    


if __name__ == "__main__":
    main()