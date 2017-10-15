import csv

# Takes the data in rawData_file_path and clean it. This includes 
# removing excess white spaces, correcting for all edge cases, and correcting any remaining formatting issues. 
# This script should output results to cleanData_file_path
def clean(rawData_file_path , cleanData_file_path): 
    f = open(cleanData_file_path, 'w')
    writer = csv.writer(f, delimiter=',')

    with open(rawData_file_path, "r") as csvDataFile:
        cleanedRow = ''  
        row_set = []  # Check for duplicate entries
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if row not in row_set:
                cleanedRow = [(*map(lambda ele:ele.strip().lower(), row))] # all to lower case and strip any whitespace 
                writer.writerow(cleanedRow)
                row_set.append(row)
    f.close()