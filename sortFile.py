import os
import shutil
import math

temp_dir = 'temp'
os.makedirs(temp_dir, exist_ok=True)
line_count = 0     
with open('sample_input.txt', 'r') as file:
    line_count = sum(1 for line in file)

chunk_size = 500 * 1024 * 1024  
with open('sample_input.txt') as input_file:
    for i, chunk in enumerate(iter(lambda: list(input_file.readline() for _ in range(line_count)), [])):
        chunk[len(chunk)-1]+="\n"
        if i >= math.ceil(line_count/chunk_size):
            break
        chunk_file = os.path.join(temp_dir, f'chunk_{i}.txt')
        with open(chunk_file, 'w') as chunk_out:
            chunk_out.writelines(sorted(chunk))

sorted_file = 'sample_output.txt'
with open(sorted_file, 'w') as output_file:
    chunk_files = [os.path.join(temp_dir, f'chunk_{i}.txt') for i in range(math.ceil(line_count/chunk_size))]

    chunk_handles = [open(chunk_file) for chunk_file in chunk_files]
    lines = [handle.readline().strip() for handle in chunk_handles]

    while any(lines):
        min_line = min(line for line in lines if line)
        output_file.write(min_line + '\n')

        index = lines.index(min_line)
        lines[index] = chunk_handles[index].readline().strip()

    for handle in chunk_handles:
        handle.close()

shutil.rmtree(temp_dir)