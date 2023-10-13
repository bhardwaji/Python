import csv


class FileHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_csv_and_calculate_average_age(self):
        try:
            with open(self.input_file, "r") as csv_file:
                reader = csv.DictReader(csv_file)
                total_age = 0
                num_records = 0

                for row in reader:
                    age = int(row["Age"])
                    total_age += age
                    num_records += 1

                average_age = total_age / num_records

                return average_age
        except FileNotFoundError:
            return None

    def write_result_to_file(self, average_age):
        if average_age is not None:
            with open(self.output_file, "w") as output_file:
                output_file.write(f"Average Age: {average_age:.2f}")


if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.txt"

    file_handler = FileHandler(input_file, output_file)
    average_age = file_handler.read_csv_and_calculate_average_age()

    if average_age is not None:
        file_handler.write_result_to_file(average_age)
        print(f"Average age calculated and saved to {output_file}.")
    else:
        print(f"Input file '{input_file}' not found.")
