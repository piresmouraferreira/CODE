import numpy as np
import csv
import os
import time

# Define CSV file path
current_dir = os.getcwd()

# define dataset filename
fname = r'{}/src/abaqus/dataset.csv'.format(current_dir)

def main():
    """
    Main function to start code execution.
    """

    # start timer
    start_time = time.time()

    # iterate through file
    try:
        with open(fname, mode='r') as file:
            reader = csv.reader(file)
            # for each timestep
            for k, row in enumerate(reader):
                print(f"Starting timestep {k}")

                # initialize arrays
                ux_arr, uy_arr, uz_arr, rfx_arr, rfy_arr, rfz_arr = [], [], [], [], [], []
                s11_arr, s22_arr, s33_arr, s12_arr, s13_arr, s23_arr = [], [], [], [], [], []
                e11_arr, e22_arr, e33_arr, e12_arr, e13_arr, e23_arr = [], [], [], [], [], []

                # get displacement values
                ux_arr.append(row[0])
                uy_arr.append(row[1])
                uz_arr.append(row[2])

                # get force values
                rfx_arr.append(row[3])
                rfy_arr.append(row[4])
                rfz_arr.append(row[5])

                # for each element
                for i in range(6, 6+156*12, 12):
                    # get stress values
                    s11_arr.append(row[i])
                    s22_arr.append(row[i + 1])
                    s33_arr.append(row[i + 2])
                    s12_arr.append(row[i + 3])
                    s13_arr.append(row[i + 4])
                    s23_arr.append(row[i + 5])

                    # get strain values
                    e11_arr.append(row[i + 6])
                    e22_arr.append(row[i + 7])
                    e33_arr.append(row[i + 8])
                    e12_arr.append(row[i + 9])
                    e13_arr.append(row[i + 10])
                    e23_arr.append(row[i + 11])

    except Exception as e:
        print(f"Error iterating input file: {e}")

    # end the timer and calculate elapsed time in minutes and seconds
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_minutes = int(elapsed_time // 60)
    elapsed_seconds = int(elapsed_time % 60)

    # print total elapsed time in "minutes:seconds" format
    print(
        f"Total elapsed time: {elapsed_minutes}:{elapsed_seconds:02d} minutes."
    )

    return 0

if __name__ == "__main__":
    exit(main())