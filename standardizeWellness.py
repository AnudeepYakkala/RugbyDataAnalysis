import csv
from math import sqrt

with open('/Users/anudeepyakkala/Downloads/combinedDataFloats.csv', mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    monitoring_score = []
    training_readiness = []
    RPE =[]
    duration = []
    pain = []
    illness = []
    menstration = []
    sleep = []

    total_data = []
    data = {}

    sd_monitoring_score = []
    sd_training_readiness = []
    sd_RPE =[]
    sd_duration = []
    sd_pain = []
    sd_illness = []
    sd_menstration = []
    sd_sleep = []

    for i in range(1, 18):
        csv_file.seek(0)
        line_count = 0

        monitoring_total = 0
        monitoring_count = 0.0
        readiness_total = 0
        readiness_count = 0.0
        pain_total = 0
        pain_count = 0.0
        illness_total = 0
        illness_count = 0.0
        menstration_total = 0
        menstration_count = 0.0
        sleep_total = 0
        sleep_count = 0.0
        duration_total = 0
        duration_count = 0.0
        RPE_total = 0
        RPE_count = 0.0

        for row in csv_reader:
            if line_count < 1:
                line_count = line_count + 1
            else:
                if int(row["PlayerID"]) == i:
                    if (float(row["AverageRPE"]) != 0.0):
                        RPE_count += 1
                        RPE_total += 10 - float(row["AverageRPE"])
                    if (int(row["TotalDuration"]) != 0):
                        duration_count += 1
                        duration_total += int(row["TotalDuration"])
                    monitoring_total += int(row["MonitoringScore"])
                    monitoring_count += 1
                    if (float(row["TrainingReadiness"]) != 0):
                        readiness_count += 1
                        readiness_total += float(row["TrainingReadiness"])
                    pain_count += 1
                    pain_total += int(row["Pain"])
                    illness_count += 1
                    illness_total += int(row["Illness"])
                    menstration_count += 1
                    menstration_total += int(row["Menstruation"])
                    sleep_total += float(row["SleepHours"])
                    sleep_count += 1
        monitoring_score.append(monitoring_total/monitoring_count)
        training_readiness.append(readiness_total/readiness_count)
        RPE.append(RPE_total/RPE_count)
        duration.append(duration_total/duration_count)
        pain.append(pain_total/pain_count)
        illness.append(illness_total/illness_count)
        menstration.append(menstration_total/menstration_count)
        sleep.append(sleep_total/sleep_count)

        sd_monitoring_total = 0.0
        sd_readiness_total = 0.0
        sd_pain_total = 0.0
        sd_illness_total = 0.0
        sd_menstration_total = 0.0
        sd_sleep_total = 0.0
        sd_duration_total = 0.0
        sd_RPE_total = 0.0
        num_apperances = 0

        csv_file.seek(0)
        line_count = 0
        for row in csv_reader:
            if line_count < 1:
                line_count += 1
            else:
                if int(row["PlayerID"]) == i:
                    num_apperances += 1
                    if (float(row["AverageRPE"]) != 0.0):
                        sd_RPE_total += (10 - float(row["AverageRPE"]) - RPE[i - 1]) ** 2
                    if (int(row["TotalDuration"]) != 0):
                        sd_duration_total += (int(row["TotalDuration"]) - duration[i - 1]) ** 2
                    sd_monitoring_total += (int(row["MonitoringScore"]) - monitoring_score[i - 1]) ** 2
                    sd_readiness_total += (float(row["TrainingReadiness"]) - training_readiness[i - 1]) ** 2
                    sd_pain_total += (int(row["Pain"]) - pain[i - 1]) ** 2
                    sd_illness_total += (int(row["Illness"]) - illness[i - 1]) ** 2
                    sd_menstration_total += (int(row["Menstruation"]) - menstration[i - 1]) ** 2
                    sd_sleep_total += (float(row["SleepHours"]) - sleep[i - 1]) ** 2

        sd_monitoring_score.append(sqrt(sd_monitoring_total/num_apperances))
        sd_training_readiness.append(sqrt(sd_readiness_total/num_apperances))
        sd_pain.append(sqrt(sd_pain_total/num_apperances))
        sd_illness.append(sqrt(sd_illness_total/num_apperances))
        sd_menstration.append(sqrt(sd_monitoring_total/num_apperances))
        sd_sleep.append(sqrt(sd_sleep_total/num_apperances))
        sd_RPE.append(sqrt(sd_RPE_total/num_apperances))
        sd_duration.append(sqrt(sd_duration_total/num_apperances))


        csv_file.seek(0)
        line_count = 0
        for row in csv_reader:
            if line_count < 1:
                line_count += 1
            else:
                if int(row["PlayerID"]) == i:
                    data['Date'] = row["Date"]
                    data['ID'] = row["PlayerID"]
                    data['AverageRPE'] = (10 - float(row["AverageRPE"]) - RPE[i - 1])/sd_RPE[i - 1]
                    data['MonitoringScore'] = (int(row["MonitoringScore"]) - monitoring_score[i - 1])/sd_monitoring_score[i - 1]
                    data['TotalDuration'] = (int(row["TotalDuration"]) - duration[i - 1])/sd_duration[i - 1]
                    data['TrainingReadiness'] = (float(row["TrainingReadiness"]) - training_readiness[i - 1])/sd_training_readiness[i - 1]
                    if (int(row["Pain"]) == 1):
                        if sd_pain[i - 1] == 0:
                            data['Pain'] = 0
                        else:
                            data['Pain'] = (1 - pain[i - 1])/sd_pain[i - 1]
                    else:
                        if sd_pain[i - 1] == 0:
                            data['Pain'] = 0
                        else:
                            data['Pain'] = (0 - pain[i - 1])/sd_pain[i - 1]
                    if (int(row["Illness"]) == 2):
                        if sd_illness[i - 1] == 0:
                            data['Illness'] = 0
                        else:
                            data['Illness'] = (2 - illness[i - 1])/sd_illness[i - 1]
                    elif (int(row['Illness']) == 1):
                        if sd_illness[i - 1] == 0:
                            data['Illness'] = 0
                        else:
                            data['Illness'] = (1 - illness[i - 1])/sd_illness[i - 1]
                    else:
                        if sd_illness[i - 1] == 0:
                            data['Illness'] = 0
                        else:
                            data['Illness'] = (0 - illness[i - 1])/sd_illness[i - 1]
                    if (int(row["Menstruation"]) == 1):
                        data['Menstruation'] = (1 - menstration[i - 1])/sd_menstration[i - 1]
                    else:
                        data['Menstruation'] = (0 - menstration[i - 1])/sd_menstration[i - 1]
                    if (sd_sleep[i - 1] == 0):
                        data['Sleep'] = 0
                    else:
                        data['Sleep'] = (float(row["SleepHours"]) - sleep[i - 1])/sd_sleep[i - 1]
                    total_data.append(data)
                    data = {}
    with open('/Users/anudeepyakkala/Downloads/zscores.csv', mode = 'w') as outFile:
        fields = ['Date', 'ID', 'MonitoringScore', 'TrainingReadiness', 'Pain', 'Illness', 'Menstruation', 'Sleep', 'AverageRPE', 'TotalDuration']
        writer = csv.DictWriter(outFile, fieldnames=fields)
        writer.writeheader()
        for info in total_data:
            writer.writerow(info)
    outFile.close()
