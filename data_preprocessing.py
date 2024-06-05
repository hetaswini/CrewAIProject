# -*- coding: utf-8 -*-
"""create python code to read multiple xml files usi...

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z0Qngo5u7zFy-fR6CSCjyP-vHhjau2Pb

I'd be glad to create the best possible response to the prompt, combining the strengths of Response A and Response B, addressing their shortcomings, and incorporating insights from the ratings:
"""

from bs4 import BeautifulSoup
import glob  # For efficient file path handling

def concat_child_tag_values(xml_filepath, parent_tag_name):
  """
  Reads an XML file, finds child tag values under the specified parent tag,
  and concatenates them into a single string.

  Args:
      xml_filepath (str): Path to the XML file.
      parent_tag_name (str): Name of the parent tag to search for.

  Returns:
      str: Concatenated string of child tag values, or an empty string if
          no parent tag is found.
  """

  with open(xml_filepath, 'r') as f:
    xml_data = f.read()

  soup = BeautifulSoup(xml_data, 'lxml')  # Parse XML with BeautifulSoup

  parent_tag = soup.find(parent_tag_name)
  if not parent_tag:
    print(f"Parent tag '{parent_tag_name}' not found in '{xml_filepath}'.")
    return ''

  child_tag_values = []
  for child_tag in parent_tag.find_all(True):  # Find all child tags recursively
    if child_tag.name != parent_tag_name:  # Exclude the parent tag itself
      child_tag_values.append(child_tag.text.strip())

  return ' '.join(child_tag_values)  # Concatenate with newline characters


# Specify the directory containing your XML files (replace with your directory)
xml_dir = 'C:\DataScience\CrewAI-Projects\crewgooglegemini\data'
parent_tag_name = 'catchphrases'  # Replace with the actual parent tag name in your XML
print(glob.glob(f'{xml_dir}/*.xml'))
all_concatenated_values = []
for xml_file in glob.glob(f'{xml_dir}/*.xml'):  # Use glob for efficient pattern matching
  print(f"Reading XML file: {xml_file}")
  # Call the function to concatenate child tag values
  concatenated_value = concat_child_tag_values(xml_file, parent_tag_name)
  if concatenated_value:
    all_concatenated_values.append(f"File: {xml_file},{concatenated_value}")

if all_concatenated_values:
  print("Concatenated values from all XML files:\n")
  print('\n'.join(all_concatenated_values))
else:
  print("No child tags found under the specified parent tag in any XML files.")
