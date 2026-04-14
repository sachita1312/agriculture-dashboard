import os
import pandas as pd

data = []

dataset_path = r"D:\6th sem\data handling & visualization lab\Project\archive\PlantVillage"  # change if folder name is different

for folder in os.listdir(dataset_path):
    if "___" in folder:
        crop, disease = folder.split("___")
        folder_path = os.path.join(dataset_path, folder)
        
        for img in os.listdir(folder_path):
            data.append([crop, disease])

df = pd.DataFrame(data, columns=["crop", "disease"])

df.to_csv("plant_disease.csv", index=False)

print(" CSV created successfully!")


#in terminal 
#python convert.py