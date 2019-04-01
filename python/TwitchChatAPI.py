import subprocess
output = str(subprocess.check_output(['twitch-chatlog', '402442338']))

outputList = output[2:-1]
outputList = outputList.split('\\n')

print (outputList)