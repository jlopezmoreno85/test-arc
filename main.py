import os


def list_files_and_directories(path, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(path):
            for f in files:
                file_path = os.path.join(root, f)
                file.write(f"File: {file_path}\n")

def remove_word_from_file(input_file, output_file, word):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            modified_line = line.replace(word, "")
            output_f.write(modified_line)

if __name__ == "__main__":
    # list_files_and_directories(os.getcwd(), "All_Files_Received.txt")
    remove_word_from_file("All_Files_Received.txt", "All_Files_Received_mod.txt", "C:\\Users\\lopezmoj6359\\ARCADIS\\Transactional Services - 103011798-ProMon_FAST EV Charging Stations\\01-Received docs\\01A-Data Room\\")

    print("done")