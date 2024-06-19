# Data extraction that is currently used in my specific .pdf files, if You want, feel free to modify however You may see fit

def extract_data(source_file, output_file, keyword, keyword_amount = 0):
    with open(source_file, 'r', encoding='utf-8') as src_file:
        lines = src_file.readlines()
    lines_to_write = []

    # head empty, how do I clean the file with appending to it afterwards
    with open(output_file, "w", encoding='utf-8') as out_file:
        out_file.write("")

    # Iterate through the lines and add amount above the line when the keyword is found
    for i in range(1, len(lines)):
        if keyword in lines[i]:
            # Just small iteration for index
            keyword_amount = keyword_amount + 1
            # Extract the amount from the line above the keyword line
            keyword_line = lines[i].strip()
            keyword_line2 = lines[i + 43].strip()
            with open(output_file, 'a', encoding='utf-8') as out_file:
                if "-,---" in keyword_line2:
                    keyword_line2 = lines[i + 46].strip()
                    out_file.write(keyword_line + "\n" + str(keyword_amount) + ". " + keyword_line2 + "\n")
                elif len(lines) > 0:
                    out_file.write(keyword_line + "\n" + str(keyword_amount) + ". " + keyword_line2 + "\n")
                else:
                    print("No data to write.")
    print(f"Data has been written to {output_file}")