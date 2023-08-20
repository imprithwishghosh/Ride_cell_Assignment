import xml.etree.ElementTree as ET
import csv
import os

def parse_xml_files(folder_path):
  """Parses all XML files in the specified folder and returns a list of data records."""
  data_records = []
  for file_name in os.listdir(folder_path):
    if file_name.endswith(".xml"):
      with open(os.path.join(folder_path, file_name)) as xml_file:
        xml_tree = ET.parse(xml_file)
        root = xml_tree.getroot()
        for record in root:
          data_records.append({
            "classname": record.find("classname").text,
            "time": record.find("time").text,
            "groupNo": record.find("groupNo").text
          })
  return data_records

def print_data_in_csv_format(data_records, output_file_path):
  """Prints the specified data records in CSV format to the specified output file."""
  with open(output_file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["classname", "time", "groupNo"])
    for data_record in data_records:
      data_record_list = [
          data_record["classname"],
          data_record["time"],
          data_record["groupNo"]
      ]
      csv_writer.writerow(data_record_list)

if __name__ == "__main__":
  folder_path = "/Users/prithishghosh/Downloads/devops-assignment-main/programming/assignment-1/data"
  output_file_path = "output.csv"
  data_records = parse_xml_files(folder_path)
  print_data_in_csv_format(data_records, output_file_path)
