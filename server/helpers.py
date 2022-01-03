import re

def sendData(file):
	pattern = re.compile(r'^\[(\d+\.\d+\.\d+), .+\]\s+([^:]+):\s*(.*)', re.M)

	data = []

	prevday = None

	for line in file:
		if type(line) is bytes:
			line = line.decode("utf-8")

		matches = pattern.findall(line)

		for entry in matches:
			(date, name, msg) = entry

			if prevday and prevday["date"] == date:
				if name in prevday["people"]:
					prevday["people"][name] += 1
				else:
					prevday["people"][name] = 1
			else:
				prevday = {
					"date": date,
					"people": {},
				}
				prevday["people"][name] = 1
				data.append(prevday)
	return data
