import random

def main():

    numbers = [16.2, 75.1, 52.3]
    
    print(f"numbers {numbers}")

    append_random_numbers(numbers)

    print(f"numbers {numbers}")

    append_random_numbers(numbers , 3)

    print(f"numbers {numbers}")

    words = []
    
    append_random_words(words)

    append_random_words(words, 8)

    print(f"words {words}")



def append_random_numbers(numbers_list, quantity=1):

     for _ in range(quantity):
        random_number = round(random.uniform(0, 1000000), 1)
        numbers_list.append(random_number)


def append_random_words(words_list, quantity=1):

    for _ in range(quantity):
    
        words = ["I", "Am", "Inevitable", "Iron", "Man", 
             "Spider", "Senses", "Mir4", "Mobile", "Legends", 
             "Daddy"]
    
        ranwords = random.choice(words)
        words_list.append(ranwords)





    
    


if __name__ == "__main__":
    main()