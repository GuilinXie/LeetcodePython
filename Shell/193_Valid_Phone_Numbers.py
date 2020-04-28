# Read from the file file.txt and output all valid phone numbers to stdout.
cat file.txt | awk -F '\t' '{print $1}' | awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/'