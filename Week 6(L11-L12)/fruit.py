def main():
    try:
    # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"Original: {fruit_list}")

    #Reverse the fruit_list and print
        fruit_list.reverse()
        print(f"Reversed: {fruit_list}")
    #Append orange into the list
        fruit_list.append("orange")
        print(f"Appended: {fruit_list}")
    # Find where "apple" is located in the fruit_list and insert
    # "cherry" before "apple" in the list and print the list.
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"Insert cherry: {fruit_list}")
    #Remove banana from the list
        fruit_list.remove("banana")
        print(f"Removed: {fruit_list}")
    #Pop the last item on the list
        last = fruit_list.pop()
        print(f"Popped: {last}: {fruit_list}")
    #Sort the list
        fruit_list.sort()
        print(f"Sorted: {fruit_list}")
    #Clear the list
        fruit_list.clear()
        print(f"Cleared: {fruit_list}")


    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

if __name__ == "__main__":
    main()