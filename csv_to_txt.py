import argparse
import csv

def convert_csv_to_space_separated(input_file, output_file):
    try:
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]
        
        with open(output_file, 'w') as space_separated_file:
            for row in data:
                space_separated_file.write(f"{row[0]} {row[1]}\n")
                
        print(f"Conversion successful. Output saved to {output_file}")
    
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a CSV file with two columns to space-separated format.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output space-separated text file")
    args = parser.parse_args()
    
    convert_csv_to_space_separated(args.input_file, args.output_file)