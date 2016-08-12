import sys
import csv
import os
import pickle

def progressBar(done , total):
    cur_progress = float(done)/total*100
    if cur_progress == 100.0:
        sys.stdout.write("\ndone!")
    else:
        sys.stdout.write('\r'+'%6.2f'%cur_progress + r'%')
    sys.stdout.flush()

def doneCount(done):
    sys.stdout.write('\r'+'%6d'%done)
    sys.stdout.flush()

def cutoffLine(line_type='*'):
    if line_type == '*': print '\n' + '*' * 50
    if line_type == '-': print '\n' + '-' * 50

def timekeeper(start_time,end_time):
    duration = end_time - start_time
    if duration > 3600:
        duration = float(duration)/3600
        unit = 'h'
    elif duration > 60:
        duration = float(duration)/60
        unit = 'm'
    else:
        unit = 's'
    return '%.2f%s' % (duration, unit)

def writeCSV(items, file_name):
    w_file = file(file_name, 'w')
    writer = csv.writer(w_file)
    for item in items: writer.writerow(item)
    w_file.close()

def readCSV(file_name,fun):
    r_file = file(file_name, 'r')
    reader = csv.reader(r_file)
    result = []
    for line in reader:
        result.append(map(fun, line))
    r_file.close()
    return result


def floatrange(start, stop, steps):
    ''' Computes a range of floating value.
        Input:
            start (float)  : Start value.
            stop   (float)  : End value
            steps (integer): Number of values

        Output:
            A list of floats

        Example:
            print floatrange(0.25, 1.3, 5)
            [0.25, 0.51249999999999996, 0.77500000000000002, 1.0375000000000001, 1.3]
    '''
    return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]