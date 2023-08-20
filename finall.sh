#!/bin/bash

xml_folder="/Users/prithishghosh/Downloads/devops-assignment-main/programming/assignment-1/data"

output_csv="output.csv"

echo "classname,time,groupNo" > "$output_csv"


temp_aggregated_csv=$(mktemp)


for xml_file in "$xml_folder"/*.xml; do
    classname=$(basename "$xml_file" .xml)
    time=$(xmlstarlet sel -t -v "sum(//testcase/@time)" "$xml_file")

    echo "$classname,$time" >> "$temp_aggregated_csv"
done

sort -t',' -k2,2nr -o "$temp_aggregated_csv" "$temp_aggregated_csv"

total_lines=$(wc -l < "$temp_aggregated_csv")
group_size=$(( (total_lines + 4) / 5 )) 


current_group=1
current_time=0


while IFS=',' read -r classname time; do
    if ((current_time >= group_size)); then
        current_group=$((current_group + 1))
        current_time=0
    fi
    echo "$classname,$time,$current_group" >> "$output_csv"
    current_time=$((current_time + 1))
done < "$temp_aggregated_csv"

rm "$temp_aggregated_csv"

echo "CSV output generated in: $output_csv"

