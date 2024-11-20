import re

# Load the MySQL SQL file
with open('bincom_test.sql', 'r') as file:
    sql_content = file.read()

# Replace MySQL syntax with PostgreSQL-compatible syntax
sql_content = re.sub(r'`', '"', sql_content)  # Replace backticks with double quotes
sql_content = re.sub(r'int\(\d+\)', 'INTEGER', sql_content)  # Replace int(11) with INTEGER
sql_content = re.sub(r'AUTO_INCREMENT', 'SERIAL', sql_content)  # Replace AUTO_INCREMENT with SERIAL
sql_content = re.sub(r'NOT NULL SERIAL', 'SERIAL', sql_content)  # Remove NOT NULL from SERIAL
sql_content = re.sub(r'DEFAULT CHARSET=\w+', '', sql_content)  # Remove DEFAULT CHARSET
sql_content = re.sub(r'ENGINE=\w+', '', sql_content)  # Remove ENGINE definitions
sql_content = re.sub(r'sql_mode\s*=\s*\'.*?\'', '', sql_content)  # Remove sql_mode references
sql_content = re.sub(r'ON UPDATE CURRENT_TIMESTAMP', '', sql_content)  # Remove ON UPDATE

# Save the corrected SQL file
with open('bincom_test_converted_final.sql', 'w') as file:
    file.write(sql_content)

print("SQL file converted successfully!")
