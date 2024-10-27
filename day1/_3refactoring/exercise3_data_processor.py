"""
Refactor the given procedural code into an object-oriented design,
organizing the code into classes and methods.
"""

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        data = []
        with open(self.input_file, 'r') as f:
            for line in f:
                fields = line.strip().split(',')
                data.append(fields)
        return data

    def print_output(self, data):
        print(data)

    def process_data(self, data):
        processed_data = []
        for item in data:
            # Some complex processing
            processed_item = [field.upper() for field in item]
            processed_data.append(processed_item)
        return processed_data

    def write_data(self, data):
        with open(self.output_file, 'w') as f:
            for item in data:
                line = ','.join(item)
                f.write(line + '\n')

    def process_and_save(self):
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
        self.print_output(processed_data)


# Example usage
if __name__ == '__main__':
    print("Code Refactoring[3] Data Processor")

    input_file = 'data/input.csv'
    output_file = 'data/output.csv'

    processor = DataProcessor(input_file, output_file)
    processor.process_and_save()

    print("Data Processing Completed! Text should be in uppercase.")
