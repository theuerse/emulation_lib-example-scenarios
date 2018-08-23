import os
import sys
import time
from datetime import timedelta
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import scipy as sp
import scipy.stats

DIR = ""
ONLY_LAST_N_MINUTES = 0
FILE_EXT = ".timing"
START_TIME = 0
INTERVAL_SIZE = timedelta(seconds = 30)  # i.e. 30 seconds a one measure per second -> statistical window of 30 entries
data = {}


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0* np.array(data)
    n = len(a)
    m, se = np.mean(a), sp.stats.sem(a)
    h = se * sp.stats.t._ppf((1 + confidence) / 2., n - 1)
    return m, m - h, m + h


def get_files(dir):
    files = []
    for file in os.listdir(dir):
        if file.endswith(FILE_EXT):
            files.append(file)
    return files


def garther_offset_data(filename):
    global data
    time_points = []
    time_offsets = []

    with open(os.path.join(DIR, filename), "r") as file:
        lines = list(filter(None, (line.rstrip() for line in file)))  # only consider non-empty lines

        for line in lines:
            parts = line.split()
            # 2017-09-22 11:47:25.339173 0.000038287
            # adding some fault-tolerance needed e.g. if logging started before ptpd-services on server-nodes
            # "glossing over errors is ok in this "view of the running system", but will not be tolerated in statistics
            try:
                time_point = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S.%f")
                time_offset = parts[2]
            except Exception as e:
                continue

            # skip until start time reached, additionally exclude (unlikely correct) entries with time_offset 0.0
            if time_point < START_TIME or float(time_offset) == 0.0:
                continue

            time_points.append(time_point)
            time_offsets.append(time_offset)

    data.update({filename.replace(".timing",""):(time_points, time_offsets)})


def set_global_start_time(filename):
    global START_TIME
    # fast forward to common begin
    with open(os.path.join(DIR, filename), "r") as file:
        lines = list(filter(None, (line.rstrip() for line in file)))  # only consider non-empty lines

        if ONLY_LAST_N_MINUTES == None:
            for line in lines:  # try and step over e.g. error messages
                parts = line.split()
                try:
                    time_point = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S.%f")
                except Exception as e:
                    continue
                else:
                    break
            else:
                raise Exception("no valid-starting date/time found in file:" , filename)

            START_TIME = time_point
        else:
            parts = lines[-1].split()
            START_TIME = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S.%f") - ONLY_LAST_N_MINUTES

        print("found starting-time:", START_TIME)

def garther_statistics_data(filename):
    global data
    time_points = []
    time_offsets = []
    time_offset_mean = []
    time_offset_dev = []

    interval_end = START_TIME + INTERVAL_SIZE

    # fast forward to common begin
    with open(os.path.join(DIR, filename), "r") as file:
        lines = list(filter(None, (line.rstrip() for line in file)))  # only consider non-empty lines

        for line in lines:
            parts = line.split()
            # 2017-09-22 11:47:25.339173 0.000038287
            try:
                time_point = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S.%f")
                time_offset = float(parts[2])
            except Exception as e:
                continue

            # skip until start time reached, additionally exclude (unlikely correct) entries with time_offset 0.0
            if time_point < START_TIME or time_offset == 0.0:
                continue

            if time_point > interval_end:
                stats = mean_confidence_interval(time_offsets, 0.95)
                time_points.append(time_point)
                time_offset_mean.append(stats[0])
                time_offset_dev.append(abs(stats[0] - stats[1]))

                interval_end += INTERVAL_SIZE  # set end of new interval
                time_offsets = []

            # time-points "in the zone"
            time_offsets.append(time_offset)

    data.update({filename.replace(".timing", ""): (time_points, time_offset_mean, time_offset_dev)})


def plot_offset_information(update_interval):
    lines = {}
    files = get_files(DIR)
    set_global_start_time(files[0])

    for file in files:
        garther_offset_data(file)

    if update_interval > 0:
        plt.ion()

    fig = plt.figure()
    plt.title('Time-offset from master-clock')
    plt.xlabel('Day/Time')
    plt.ylabel('Offset in milliseconds')
    ax = fig.add_subplot(111)

    scale_y = 1e-3
    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y))
    ax.yaxis.set_major_formatter(ticks_y)

    ax.axhline(color="k")

    sorted_keys = sorted(list(data.keys()))
    for key in sorted_keys:
        lines[key], = ax.plot(data[key][0], data[key][1])

    if update_interval <= 0:
        plt.legend(["Master-clock"] + sorted_keys)
        ax.relim()
        ax.autoscale()
        plt.show()

    while update_interval > 0:
        start_time = time.time()
        files = get_files(DIR)
        set_global_start_time(files[0])

        for file in files:
            garther_offset_data(file)

        sorted_keys = sorted(list(data.keys()))
        for key in sorted_keys:
            lines[key].set_xdata(data[key][0])
            lines[key].set_ydata(data[key][1])

        plt.legend(["Master-clock"] + sorted_keys)
        ax.relim()
        ax.autoscale()
        plt.show()
        print("updated plot in ", time.time() - start_time, "seconds")

        try:
            plt.pause(update_interval)
        except Exception:
            break

def plot_offset_statistics():
    lines = {}

    files = get_files(DIR)
    set_global_start_time(files[0])

    for file in files:
        garther_statistics_data(file)

    fig = plt.figure()
    plt.title('Time-offset from master-clock')
    plt.xlabel('Day/Time')
    plt.ylabel('Offset in milliseconds')
    ax = fig.add_subplot(111)

    scale_y = 1e-3
    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y))
    ax.yaxis.set_major_formatter(ticks_y)

    ax.axhline(color="k")

    sorted_keys = sorted(list(data.keys()))
    for key in sorted_keys:
        lines[key] = ax.errorbar(data[key][0], data[key][1], yerr=data[key][2], fmt='o', capsize = 5)

    plt.legend(["Master-clock"] + sorted_keys)
    ax.relim()
    ax.autoscale()
    plt.show(block=True)


def plot_max_differences(update_interval):
    files = get_files(DIR)
    set_global_start_time(files[0])

    for file in files:
        garther_statistics_data(file)

    if update_interval > 0:
        plt.ion()

    fig = plt.figure()
    plt.title('Time-offset differences (max distance between two nodal mean-values)')
    plt.xlabel('Interval#')
    plt.ylabel('Offset in microseconds')
    ax = fig.add_subplot(111)

    scale_y = 1e-6
    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale_y))
    ax.yaxis.set_major_formatter(ticks_y)

    ax.axhline(color="k")

    stat_values = calc_max_differences(data)
    line, = ax.plot(stat_values[0], stat_values[1])

    if update_interval <= 0:
        plt.legend(["Reference-zero","difference from common mean"])
        ax.relim()
        ax.autoscale()
        plt.show()

    while update_interval > 0:
        start_time = time.time()
        files = get_files(DIR)
        set_global_start_time(files[0])

        for file in files:
            garther_statistics_data(file)

        stat_values = calc_max_differences(data)
        line.set_xdata(stat_values[0])
        line.set_ydata(stat_values[1])

        plt.legend(["Reference-zero", "difference from common mean"])
        ax.relim()
        ax.autoscale()
        plt.show()
        print("updated plot in ", time.time() - start_time, "seconds")

        try:
            plt.pause(update_interval)
        except Exception:
            break


# max differences of mean-values
def calc_max_differences(data):
    min_len = 1e20

    for key, value in data.items():
        min_len = min(min_len, len(value[1]))

    last_time_point = 0
    time_points = []
    max_differences_from_each_other = []

    for i in range(0, min_len, 1):
        means = []
        for key in data.keys():
            last_time_point = data[key][0][i]
            means.append(data[key][1][i])

        time_points.append(last_time_point)
        means.sort()
        max_differences_from_each_other.append(means[-1] - means[0])

    return (time_points, max_differences_from_each_other)


"""
main entry-point of the program
"""
if len(sys.argv) < 2:
    print("usage: python3", sys.argv[0],"<timing-file directory>", "<optional only last n minutes>",
          "<optional update-interval in seconds>", "<optional statistics interval/window size (in seconds)>")
    exit(-1)

DIR = sys.argv[1]
ONLY_LAST_N_MINUTES = timedelta(minutes = int(sys.argv[2])) if len(sys.argv) >= 3 and int(sys.argv[2]) != 0 else None
update_interval = int(sys.argv[3]) if len(sys.argv) >=4 else 0
INTERVAL_SIZE = timedelta(seconds = int(sys.argv[4])) if len(sys.argv) >= 5 else INTERVAL_SIZE

print("directory:", DIR)
print("only last n minutes:", ONLY_LAST_N_MINUTES)
print("graph update-interval:", update_interval)
print("statistics interval size:", INTERVAL_SIZE, "\n")

plot_offset_information(update_interval)
plot_offset_statistics()
plot_max_differences(update_interval)
