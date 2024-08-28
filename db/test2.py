def replace_characters(file_path):
    # Read the file content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace dots and pluses with commas
    content = content.replace('•', ',')
    content = content.replace('+', ',')

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    file_path = "./db/extracted_recipes.txt"
    replace_characters(file_path)
    print("Replacements done successfully.")
