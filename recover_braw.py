MIT License

Copyright (c) [2023] [DRC Recovery]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

import os

# Prompt user for file path
file_path = input("Enter the path of the image file to recover: ")

# Define the signature for the start of the file
start_sig = b'\x00\x00\x00\x08\x77\x69\x64\x65'

# Define possible signatures for the end of the file
end_sigs = [
    b'\x6B\x69\x70\x00\x00\x00\x00',  # skip
    b'\x73\x6B\x69\x70\x00\x00\x00\x00\x62\x72\x61\x77',
    b'\x73\x6B\x69\x70\x00\x00\x00\x00\x00\x18\x73\x74\x74\x73',
    b'\x73\x6B\x69\x70'
]

# Define the buffer size for reading the file
BUFFER_SIZE = 1024 * 1024 * 1024 # 1GB buffer size

# Open the file for reading in binary mode
with open(file_path, 'rb') as f:

    # Initialize variables
    offset = 0
    end_offset = 0

    # Read in a buffer at a time
    while True:
        buffer = f.read(BUFFER_SIZE)

        # Check if buffer is empty, end of file reached
        if not buffer:
            break

        # Look for the start signature in the buffer
        start_offset = buffer.find(start_sig)

        # If start signature is found
        if start_offset != -1:
            # Calculate the offset from the beginning of the file
            offset += start_offset

            # Loop through possible end signatures and find the one that appears last in the file
            for end_sig in end_sigs:
                end_offset = buffer.rfind(end_sig)

                # If the end signature is found in the buffer
                if end_offset != -1:
                    # Calculate the offset from the beginning of the file
                    end_offset += offset
                    break

            # Break out of the loop if an end signature was found
            if end_offset != 0:
                break

        # Increment the offset by the buffer size
        offset += BUFFER_SIZE

# Print the start and end offsets of the recovered file
print(f'Start offset: {offset}')
print(f'End offset: {end_offset}')
