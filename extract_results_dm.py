"""
Tool to extract data from odb file.
"""

from abaqus import *
from abaqusConstants import *

import os
import csv
import time

# Define path for data
current_dir = os.getcwd()
overwrite=True

# Start the timer
start_time = time.time()

odb_Path = 'Job-Joao.odb'
ODB = session.openOdb(name=odb_Path)

# Define CSV file path
csv_filename = r'{}\dataset.csv'.format(current_dir)

# Open the CSV file in binary mode ('wb')
with open(csv_filename, 'wb') as file:
    writer = csv.writer(file)

    # Create a list to store all rows of data
    all_data = []

    # number of frames
    frames = len(ODB.steps['Step-Tracao'].frames)

    # Loop for Frames
    for frame in range(1, frames):
        print("Starting frame "+ str(frame))
        data = []

        # get displacement values
        ux = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['U'].values[0].data[0]
        uy = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['U'].values[0].data[1]
        uz = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['U'].values[0].data[2]

        # get force values
        rfx = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['RF'].values[0].data[0]
        rfy = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['RF'].values[0].data[1]
        rfz = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['RF'].values[0].data[2]

        # extend values to buffer
        data.extend([ux, uy, uz, rfx, rfy, rfz])

        for cent in range(len(ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values)):
            # get stress values
            s11 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[0]
            s22 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[1]
            s33 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[2]
            s12 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[3]
            s13 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[4]
            s23 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['S'].values[cent].data[5]

            # get strain values
            e11 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[0]
            e22 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[1]
            e33 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[2]
            e12 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[3]
            e13 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[4]
            e23 = ODB.steps['Step-Tracao'].frames[frame].fieldOutputs['E'].values[cent].data[5]

            # extend values to buffer
            data.extend([s11, s22, s33, s12, s13, s23, e11, e22, e33, e12, e13, e23])
    
        # Append the row data to all_data
        all_data.append(data)

    # Use writerows() to write all_data to the CSV file in bulk
    print("Writting buffer to csv file")
    writer.writerows(all_data)

# Close the ODB file
ODB.close()

# End the timer and calculate elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

# Convert elapsed time to minutes and seconds
elapsed_minutes = int(elapsed_time // 60)
elapsed_seconds = int(elapsed_time % 60)

# Print total elapsed time in "minutes:seconds" format
print("Finished in {}:{:02d} minutes.".format(elapsed_minutes, elapsed_seconds))