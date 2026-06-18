import openpyxl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


wb = openpyxl.Workbook()
ws= wb.active
ws.title="student"

ws.append(["Name","Math","Science","English","Computer"])
ws.append(["Rahul",86,98,56,67])
ws.append(["Priya",77,89,66,74])
ws.append(["Abhishek",80,87,90,68])
ws.append(["Rohan",70,54,68,88])
ws.append(["Sneha",58,57,64,45])
ws.append(["Amit",82,93,55,95])
ws.append(["Pooja",98,78,77,84])
ws.append(["Vikash",87,92,79,68])


wb.save("students.xlsx")

print("Excel file created successfully!")

df = pd.read_excel("students.xlsx")
print ("Data Loaded")
print(df)


df["Average"] = df[["Math","Science","English","Computer"]].mean(axis=1)
print(df[["Name","Average"]])

df["Result"]= df["Average"].apply(lambda x:"pass" if x>=60 else "fail")
print(df[["Name","Average","Result"]])


lowest= df.loc[df["Average"].idxmin()]
print(f"Lowest: {lowest['Name']} - {lowest['Average']}")

print(f"Class Average : {df['Average'].mean():.2f}")

#bar chart

plt.figure(figsize=(10,6))
plt.bar(df["Name"],df["Average"],color="skyblue")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.axhline(y=60, color="red" , linestyle="--",label="pass")
plt.legend()
plt.show()