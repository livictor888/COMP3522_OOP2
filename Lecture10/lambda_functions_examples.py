def send_some_data(data, response_callback):
    # fancy code to send data here
    response_callback(f"{data} sent successfull")


def main():
    print("\n---------Lambda Function---------")
    # This is what a lambda function looks like
    lambda x: x * 2

    # Passing lambda functions as callbacks
    address_data = {
        "name": "Meghan",
        "adddress": ("123 street name", "City", "Zipcode", "Province"),
        "phone": "+1-888-777-6666"
    }
    send_some_data(address_data, lambda x: print(f"{x} sent successfully"))

    # Generally not a good idea to assign a lambda expression to a
    # variable, but for demonstration's sake:
    square_root = lambda x: x ** 0.5
    numbers = [square_root(i) for i in [1,2,3,4,5,6]]
    print(f"Result (lambda expressions in comprehensions): {numbers}")

    print("\n---------Filter Function---------")
    # filter() method example
    vowels = ['a', 'e', 'i', 'o', 'u']
    my_string = "Hello World"
    consonants = filter(lambda x: x not in vowels, my_string)
    print(f"The result of filter when converted to a string: "
          f"{list(consonants)}")

    # filter returns an object of type filter, a special iterator. Since
    # we have already printed it as a list once, we have exhausted the
    # iterator. It will not print again.
    print(f"Filter returns an object of type {type(consonants)}")
    print(f"Attempting to print the result of the filter() function: "
          f"{list(consonants)}")

    print("\n---------Map Function---------")
    # map() method example
    full_names = ["Ross Geller", "Rachel Green", "Phoebe Buffay",
                  "Chandler Bing", "Monica Geller", "Joey Tribbiani"]
    first_name_map = map(lambda x: x.split()[0], full_names)
    print(f"Result of map function to pull out the first names from a list of "
          f"names: {list(first_name_map)}")

    # map returns an object of type map, a special iterator. Since
    # we have already printed it as a list once, we have exhausted the
    # iterator. It will not print again.
    print(f"Map returns an object of type {type(first_name_map)}")
    print(f"Attempting to print the result of the map() function: "
          f"{list(first_name_map)}")

    # map() example with multiple arguments
    first_names = ["Ross", "Rachel", "Pheobe", "Chandler", "Monica", "Joey"]
    last_names = ["Geller", "Green", "Buffay", "Bing", "Geller", "Tribbiani"]
    full_names_map = map(lambda x, y: f"{x} {y}", first_names, last_names)
    print(f"Result of using maps with multiple arguments: "
          f"{tuple(full_names_map)}")


if __name__ == '__main__':
    main()