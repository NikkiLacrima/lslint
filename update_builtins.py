import os

def generate_builtins_cc(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#ifdef _MSC_VER\n')
        f.write('#pragma execution_character_set("utf-8")\n')
        f.write('#endif\n')
        f.write('const char *builtins_txt[] = {\n')

        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Escape backslashes and double quotes
            escaped_line = line.replace('\\', '\\\\').replace('"', '\\"')
            f.write(f'"{escaped_line}",\n')

        f.write('(char*)0 };\n')

if __name__ == '__main__':
    generate_builtins_cc('builtins.txt', 'builtins_txt.cc')
