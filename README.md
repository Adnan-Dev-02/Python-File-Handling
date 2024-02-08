# Python-File-Handling
This script reads content from a text file, performs basic analysis, allows word/phrase replacement, and writes the modified content back.

Features:
Counts words, lines, and characters
Replaces specific words or phrases
Error handling for file operations
Requirements:
Python 3.x
How to Use:
Save the script: Download or copy the script content and save it as a .py file (e.g., text_analysis.py).
Place your text file: Put the text file you want to analyze in the same directory as the script.
Run the script: Open a terminal or command prompt, navigate to the directory containing the script and text file, and run the following command:
python text_analysis.py <filename> <old_word> <new_word>
Replace <filename> with the actual name of your text file, <old_word> with the word or phrase you want to replace, and <new_word> with the replacement word or phrase.

Example:
python text_analysis.py my_text.txt example replacement
This will analyze my_text.txt, replace all occurrences of "example" with "replacement", and write the modified content back to the file.

Notes:
Make sure Python is installed and accessible in your command prompt/terminal.
The script overwrites the original file content with the modified version.
For more complex modifications, you might need to adapt the script further.
