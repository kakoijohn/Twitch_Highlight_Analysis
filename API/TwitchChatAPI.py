import subprocess

VOD = '405029264'

# output = str(subprocess.check_output(['tcd',
#                                       '-v', VOD,
#                                       '--client-id', 'ln3y6ld5tlvlh24mpn4ekzgeessqf0',
#                                       '-o', './Chat_API_Download']))

chatOutput = open('./Chat_API_Download/' + VOD + '.txt', 'r').read().splitlines()

chatOutDict = []

for listItem in chatOutput:
    chatOutDict.append({"timestamp": listItem[(listItem.find('[') + 1): listItem.find(']')],
                       "username": listItem[(listItem.find('<') + 1): listItem.find('>')],
                       "message": listItem[(listItem.find('>') + 2):]})

print (chatOutDict[0]["timestamp"])