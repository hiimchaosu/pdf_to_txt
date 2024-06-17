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
            keyword_line = lines[i - 1].strip()
            keyword_line2 = lines[i].strip()
            with open(output_file, 'a', encoding='utf-8') as out_file:
                if "SKADEN" in keyword_line:
                    keyword_line = lines[i - 4].strip()
                    out_file.write(keyword_line + "\n" + str(keyword_amount) + "." + keyword_line2 + "\n")
                elif len(lines) > 0:
                    out_file.write(keyword_line + "\n" + str(keyword_amount) + "." + keyword_line2 + "\n")
                else:
                    print("No data to write.")
    with open(output_file, 'a', encoding='utf-8') as out_file:
        out_file.write(lines[-4])
    print(f"Data has been written to {output_file}")