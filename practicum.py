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

def alphabet_sort(key)
    pass


def main():
    print(euclidian_stuff([4], [1]))


if __name__ == "__main__":
    main()