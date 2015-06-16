# A script to send all this mail and setup mailboxes.
import subprocess
import os, sys, re
from get_ratings import get_rating

# A function to send e-mail messages.
def send_message(recipient, subject, body):
    process = subprocess.Popen(['mail', '-s', subject, recipient],
                               stdin=subprocess.PIPE)
    process.communicate(body)
    print 'Sent message ' + subject


def main():
    exclude = raw_input('Enter directories to exclude, separated by a space: ')
    exclude = exclude.split(' ')
    defaultexclude = ['images','parser','results']
    exclude += defaultexclude

    print "Excluding directories " + str(exclude)

    for path, subdirs, files in os.walk(".", topdown=True):

        subdirs[:] = [i for i in subdirs if i not in exclude]

        if "spam" in path:

            for filen in files:
                with open(path+'/'+filen,'r') as f:

                    # Remove the subject from the body                  
                    subject = re.split('Subject: ',f.readline())[1]
                    
                    body = f.read().decode('utf-8', errors='ignore')

                    send_message(sys.argv[1],subject.strip(),body)
                    get_rating(body,'spam')

if __name__ == '__main__':
    main()