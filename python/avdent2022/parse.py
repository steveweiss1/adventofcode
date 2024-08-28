def parse_file(filename):
    parsed_data = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            line = line.strip()
            if line:
                # Split the line by spaces
                parts = line.split()

                # Assuming the first part is a string, the second is an integer, and the third is a long integer
                string_part = parts[0]
                integer_part = int(parts[1])
                long_part = int(parts[2])

                # Append the parsed tuple to the list
                parsed_data.append((string_part, integer_part, long_part))

    return parsed_data


# Example usage
filename = "input.txt"
parsed_list = parse_file(filename)
print(parsed_list)
