from collections import Counter
import re
import socket

# Function to count words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())  # Split into words, ignoring punctuation
        return words, len(words)

# Function to handle contractions and count frequent words
def handle_contractions(text):
    contractions = re.sub(r"(\w+)'(\w+)", r"\1 \2", text)  # Split contractions
    words = re.findall(r'\b\w+\b', contractions.lower())
    return words, Counter(words).most_common(3)

# Get IP address
def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Count words in both files
words_if, count_if = count_words("/Users/mallikarjuna/Desktop/dockerfile/IF.txt")
words_arutw, count_arutw = count_words("/Users/mallikarjuna/Desktop/dockerfile/AlwaysRememberUsThisWay.txt")

# Total word count
#total_words = count_if + count_arutw

# Most frequent words
# most_frequent_if = Counter(words_if).most_common(3)

# Handle contractions in 'Always Remember Us This Way' and get top words
#with open("/Users/mallikarjuna/Desktop/dockerfile/AlwaysRememberUsThisWay.txt", 'r') as file:
#    text_arutw = file.read()
#most_frequent_arutw = handle_contractions(text_arutw)

# Get the IP address of the machine running the container
ip_address = get_ip_address()

# Write results to output file
with open("/Users/mallikarjuna/Desktop/dockerfile/output/result.txt", 'w') as output_file:
    output_file.write(f"Total words in IF.txt: {count_if}\n")
    output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {count_arutw}\n")
    output_file.write(f"IP address of container: {ip_address}\n")

# Print the result to the console
with open("/Users/mallikarjuna/Desktop/dockerfile/output/result.txt", 'r') as result_file:
    print(result_file.read())
