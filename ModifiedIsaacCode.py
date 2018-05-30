import argparse
import csv
import subprocess
import sys
import time


parser = argparse.ArgumentParser()
parser.add_argument('domain', help='name or IP of the website', type=str)
parser.add_argument('-p','--parameters', help='https://www.tutorialspoint.com/unix_commands/ping.htm')
args = parser.parse_args()

# list will contain each statement that builds the cmd
usr_cmd = []
# list contains ['ping', 'somedomainname']
usr_cmd.extend(('ping', args.domain))

# when params are passed in add them to the array
if args.parameters:
    usr_cmd.extend(args.parameters.split(' '))
# when no params are included add -c 3
# pings 3 times
# fail safe, prevents from infinitely pinging
else:
    param = '-n'
    count = '86400'
    usr_cmd.extend((param, count))

# By default -D is added
# -D includes a timestamp
# time = '-D'
#usr_cmd.append(time)
            
    
#Converts Unix time to the years, days, hours, minutes, seconds, and milliseconds
def convert(a):
    y = a/31557600               #31557600 seconds in a year (365.25 day---includes leap years)
    d = ((y-int(y)) * 365.25)    #365.25 days in a year
    h = ((d-int(d)) * 24)        #24 hours in a day
    m = ((h-int(h)) * 60)        #60 minutes in an hour
    s = ((m-int(m)) * 60)        #60 seconds in a minute
    ms = (s-int(s)) * 1000       #1000 milliseconds in a second
    return(int(y),int(d),int(h),int(m),int(s),int(ms))
    
# prints out user command
print(usr_cmd)

# will store parsed data
unix_time = ""
resp_time = ""
unix_conv_time = ""

first_time = 0

# Saves the ping data to raw_data.txt
with open('raw_data.log', 'w') as log, open('parsed_data.csv', 'w') as parsed:
    if first_time == 0:
        csv_out=csv.writer(parsed)
        csv_out.writerow(['unix_time','response_time', 'Years', 'Days', 'Hours', 'Minutes', 'Seconds', 'Milliseconds'])
        first_time += 1
    
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
        log.write(str_line)
        split_up = str_line.split()
        # parses the data
        if (str_line.find('time=') != -1):
            # gets the time a ping was sent
            unix_time = ts
            #unix_time.append(str_line[str_line.find('[')+1:str_line.find(']')])
            # gets the response time for a ping
            resp_time = split_up[4][5:-2]
            unix_conv_time = convert(unix_time)
            y = unix_conv_time[0]
            d = unix_conv_time[1]
            h = unix_conv_time[2]
            m = unix_conv_time[3]
            s = unix_conv_time[4]
            ms = unix_conv_time[5]
            csv_out.writerow([unix_time,resp_time,y,d,h,m,s,ms])
            
            
            
            