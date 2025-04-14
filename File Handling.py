# Define input and output file names
input_file = 'original.txt'
output_file = 'Happy coding.txt'

try:
    # Read from the original file
    with open(input_file, 'r') as infile:
        content = infile.read()

    # Modify the content
    modified_content = content.upper()

    # Write to a new file
    with open(output_file, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Modified content written to '{output_file}' successfully!")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Define the read_file function
def read_file():
    filename = input("Happy coding: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n File Content:\n")
            print(content)

    except FileNotFoundError:
        print(f"\n Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"\n Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")

# Run the function
read_file()
