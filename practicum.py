"""
Implement your solution to the practicum in this file.

@author Oscar Capraro
"""

PHONETIC_ALPHABET = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot",
    "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", 
    "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", 
    "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]

def euclidean_distance(coords_1, coords_2):
    if len(coords_1) != len(coords_2):
        return None
    tot = 0
    for i in range(len(coords_1)):
        tot += (coords_1[i] - coords_2[i])**2
    return tot ** 0.5

def alphabet_sort(num):
    numbers = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ord(numbers[int(str(num)[0])][0])

def digit_sort(num):
    return int(str(num)[0])

def data_sorter(lst):
    return sorted(lst, key=alphabet_sort), sorted(lst, key=digit_sort)


def main():
    print(euclidean_distance([4], [1]))
    a = [2, 5, 4, 7, 9, 100, 35, 22]
    print(sorted(a, key=alphabet_sort))
    print(sorted(a, key=digit_sort))


if __name__ == "__main__":
    main()