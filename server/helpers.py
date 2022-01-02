import re

def startsWithDateAndTime(s):
	pattern = '\[([0-9]+(\.[0-9]+)+),*.(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?(:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?)+)*.[a-zA-Z]+]'
	result = re.match(pattern, s)
	if result:
		return True
	return False

def getDateOfMessage(s):
	pattern = '([0-9]+(\.[0-9]+)+)'
	result = re.compile(pattern)
	return result.search(s).group(1)

def getName(string):
	withOutDate = re.sub("[\(\[].*?[\)\]]", "", string)
	newText = []
	for i in withOutDate:
		if i == ' ' or i == '\u200e':
			continue
		if i != ':':
			newText.append(i)
		else:
			return ''.join(newText)

def findDateInData(date, data):
	for x in range(len(data)):
		if data[x]['date'] == date:
			return x
	return None


def sendData(file):
	line_count = 0
	usersCount = {}
	data = []
	for line in file:
		if type(line) is bytes:
			line = line.decode("utf-8")
			
		if startsWithDateAndTime(line):
			dateOfMsg = getDateOfMessage(line)
			user = getName(line)
			dateIndex = findDateInData(dateOfMsg, data)
			if dateIndex is not None:
				try:
					data[dateIndex][user] += 1
				except KeyError:
					data[dateIndex][user] = 1
			else:
				toData = {
					"date": dateOfMsg,
				}
				toData[user] = 1
				data.append(toData)
			line_count += 1

			try:
				usersCount[user] += 1
			except KeyError:
				usersCount[user] = 1
	return data
