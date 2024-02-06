import csv
from googletrans import Translator
from httpcore import ConnectError, ReadTimeout

def translate_to_amharic(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest='am').text
        return translated_text
    except (ConnectError, ReadTimeout) as e:
        print(f"Error during translation: {e}")
        return None  # Return None to indicate translation failure

# Read the English CSV file
with open('eng.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row
    data = list(reader)

# Limit the number of rows to process (adjust as needed)
num_rows_to_process = 50
limited_data = data[:num_rows_to_process]

# Translate the second column to Amharic
translated_data = []

for i, row in enumerate(limited_data):
    label = row[0]
    text = row[1]
    translated_text = translate_to_amharic(text)

    # Check if translation was successful
    if translated_text is not None:
        translated_row = [label, translated_text]
        translated_data.append(translated_row)
    else:
        print(f"Skipping row {i+1} due to translation error.")

    # Print progress
    print(f"Processing row {i+1}/{num_rows_to_process}")

# Append the translated data to the existing CSV file
with open('amh2.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    if csvfile.tell() == 0:  # Check if the file is empty (write header only once)
        writer.writerow(header)  # Write the header row
    writer.writerows(translated_data)

print(f"Translation completed for the first {num_rows_to_process} rows. Translated data appended to 'amh.csv'.")
