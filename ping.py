#import argparse
import csv
import subprocess
import sys
import time


#parser = argparse.ArgumentParser()
#parser.add_argument('domain', help='name or IP of the website', type=str)
#parser.add_argument('-p','--parameters', help='https://www.tutorialspoint.com/unix_commands/ping.htm')
#args = parser.parse_args()

# list will contain each statement that builds the cmd
usr_cmd = []
# list contains ['ping', 'somedomainname']
usr_cmd.extend(('ping', 'www.youtube.com'))

# when params are passed in add them to the array
#if args.parameters:
#    usr_cmd.extend(args.parameters.split(' '))
# when no params are included add -c 3
# pings 3 times
# fail safe, prevents from infinitely pinging
#else:
param = '-n'
count = '5'
usr_cmd.extend((param, count))

# By default -D is added
# -D includes a timestamp
# time = '-D'
#usr_cmd.append(time)

# prints out user command
print(usr_cmd)

# will store parsed data
unix_time = []
resp_time = []

# Saves the ping data to raw_data.txt
with open('raw_data.log', 'w') as out:
    # Runs users request through the terminal
    result = subprocess.Popen(usr_cmd, stdout=subprocess.PIPE)
    
    for line in iter(result.stdout.readline, b''):
        # create a timestamp
        ts = time.time()
        # convert line to a string    
        str_line = line.decode('utf-8')
        # displays to terminal
        sys.stdout.write(str_line)
        # writes to file
        out.write(str_line)
        split_up = str_line.split()
        # parses the data
        if (str_line.find('time=') != -1):
            # gets the time a ping was sent
            unix_time.append(ts)
            #unix_time.append(str_line[str_line.find('[')+1:str_line.find(']')])
            # gets the response time for a ping
            resp_time.append(split_up[4][5:-2])
            
# Creates a tuple of unix_time and resp_time
# example: (1527198659, 59)
parsed_data = zip(unix_time, resp_time)

# Saves unix_time, resp_time to a csv file
with open('parsed_data.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['unix_time','response_time'])
    for row in parsed_data:
        csv_out.writerow(row)
