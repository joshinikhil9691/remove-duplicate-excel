import pandas as pd

data = pd.read_excel('demo.xlsx')
data = data.drop_duplicates(subset=["Student", "Course", "Branch", "Semester"],
                            keep="first")
data.to_excel("remove-duplicate.xlsx", index=False)
