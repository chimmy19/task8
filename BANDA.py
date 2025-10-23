

import pandas as pd

students_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 19, 22, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 67, 88]
})

print(students_data.head(3))
print(students_data['Name'], students_data['Marks'])
print(students_data[students_data['Grade'] == 'A'])
