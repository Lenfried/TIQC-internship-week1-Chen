import csv
import os


def main() -> None:
    print("GPA Average Calculator")
    print("----------------------")
    print("Put your CSV file in the same directory as this program.")
    filename = input("Enter the CSV file name (e.g. gpa.csv): ").strip()

    if not filename:
        print("No file name provided. Exiting.")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, filename)

    if not os.path.isfile(csv_path):
        print(f"File '{filename}' not found in the program directory.")
        return

    total_gpa = 0.0
    valid_row_count = 0

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for index, row in enumerate(reader):
            # Skip empty rows
            if not row:
                continue

            # Ensure we have at least two columns
            if len(row) < 2:
                continue

            name = row[0].strip()
            gpa_str = row[1].strip()

            # Skip header row if first cell is "Student Name"
            if index == 0 and name == "Student Name" or name == "Name":
                continue

            # Ignore rows with blank values
            if not name or not gpa_str:
                continue

            # Ignore rows where GPA is not a valid number
            try:
                gpa = float(gpa_str)
            except ValueError:
                continue

            total_gpa += gpa
            valid_row_count += 1

    if valid_row_count == 0:
        print("No valid student rows found. Ensure the CSV file format is Student Name,GPA.")
        return

    average_gpa = total_gpa / valid_row_count

    print(f"Rows processed (valid students): {valid_row_count}")
    print(f"Average GPA: {average_gpa:.2f}")


if __name__ == "__main__":
    main()

