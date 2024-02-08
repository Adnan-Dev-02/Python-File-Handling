def analyze_and_modify_text(filename, old_word, new_word):
  
  try:
    # Read the content of the file
    with open(filename, "r") as file:
      content = file.read()

    # Perform analysis
    num_words = len(content.split())
    num_lines = len(content.splitlines())
    num_chars = len(content)

    print(f"File analysis:")
    print(f"- Number of words: {num_words}")
    print(f"- Number of lines: {num_lines}")
    print(f"- Number of characters: {num_chars}")

    # Modify the content
    modified_content = content.replace(old_word, new_word)

    # Write the modified content back to the file
    with open(filename, "w") as file:
      file.write(modified_content)

    print(f"Successfully replaced '{old_word}' with '{new_word}' in the file.")

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

  except Exception as e:
    print(f"An error occurred: {e}")

# Example usage
filename = "myfile.txt"  # Replace with your actual filename
old_word = "example"
new_word = "replacement"

analyze_and_modify_text(filename, old_word, new_word)