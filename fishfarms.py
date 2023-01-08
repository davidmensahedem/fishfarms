
# Python program to read CSV file line by line
# import necessary packages
import csv


# Open file 
with open('fishfarms.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object

    farm_polygons = []
    farm_coordinates = []
    farm_name = "Individual"

    for row in reader_obj:
        farm_name = row[2]
        farm_coordinates.append((row[3],row[4]))
        break
  
    for row in reader_obj:
        if(row[2] == farm_name):
            farm_coordinates.append((row[3],row[4]))
        else:
            farm_polygons.append(farm_coordinates)
            farm_coordinates = []
            farm_name = row[2]
            farm_coordinates.append((row[3],row[4]))
    for farm in farm_polygons:
        print("Farm Coordinates: ")
        for coord in farm:
            print(coord[0],coord[1])
            
            
    #     print("============End=============")
    
    

