import chardet

# The chardet library is used to detect the encoding of the file.
# This is useful when you encounter encoding issues while reading a file, such as a UnicodeDecodeError.

# Replace 'Example.csv' with the name of your file.
file_name = 'Example.csv'

# Open the file in binary mode ('rb' stands for read binary).
with open(file_name, 'rb') as f:
    # Read the entire content of the file.
    raw_data = f.read()

    # Use chardet to detect the encoding of the file.
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# Print the detected encoding.
print(f'The encoding used in the file is: {encoding}')

