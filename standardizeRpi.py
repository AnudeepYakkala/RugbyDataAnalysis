import csv
from math import sqrt

with open('/Users/anudeepyakkala/Downloads/data/gps.csv', mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    impulse = []
    load = []
    accel_mag = []

    for i in range(1, 18):
        print i
        csv_file.seek(0)
        line_count = 0
        num_apperances = 0.0

        impulse_total = 0.0
        load_total = 0.0
        accel_x = 0.0
        accel_y = 0.0
        accel_z = 0.0
        mag_accel = 0.0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
                id = int(row["PlayerID"])
                if id == i:
                    num_apperances += 1
                    impulse_total += float(row["AccelImpulse"])
                    load_total += float(row["AccelLoad"])
                    accel_x = float(row["AccelX"])
                    accel_y = float(row["AccelY"])
                    accel_z = float(row["AccelZ"])
                    mag_accel += sqrt((accel_x * accel_x) + (accel_y * accel_y) + (accel_z * accel_z))


        impulse.append(round(impulse_total/num_apperances, 4))
        load.append(round(load_total/num_apperances, 4))
        accel_mag.append(round(mag_accel/num_apperances, 4))

        total_data = []
        data = {}

    for i in range(0, 17):
        data['PlayerID'] = i + 1
        data['AccelImpuse'] = impulse[i]
        data['AccelLoad'] = load[i]
        data['accel_mag'] = accel_mag[i]
        total_data.append(data)
        data = {}

    with open('/Users/anudeepyakkala/Downloads/averageGameData.csv', mode = 'w') as outFile:
        fields = ['PlayerID', 'AccelImpuse', 'AccelLoad', 'accel_mag']
        writer = csv.DictWriter(outFile, fieldnames=fields)
        writer.writeheader()
        for info in total_data:
            writer.writerow(info)
    outFile.close()
