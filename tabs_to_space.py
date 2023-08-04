import argparse

def convert_csv_to_space_separated(input_file, output_file):
    try:
        with open(input_file, 'r') as tab_file:
            data = [line.strip().split() for line in tab_file]
        
        with open(output_file, 'w') as space_separated_file:
            for row in data:
                space_separated_file.write(f"{row[0]} {row[1]}\n")
                
        print(f"Conversion successful. Output saved to {output_file}")
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a whitespace (ex. tab) separated edge list to single space-separated format.")
    parser.add_argument("input_file", help="Path to the input TXT file")
    parser.add_argument("output_file", help="Path to the output TXT file")
    args = parser.parse_args()
    
    convert_csv_to_space_separated(args.input_file, args.output_file)