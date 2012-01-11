import urllib
import BeautifulSoup

inputfile = open("input.txt", "r")
courses = []
for line in inputfile:
	line = line.rstrip()
	if line == "":
		continue
	courses.append(line)
inputfile.close()

outputfile = open("output.html", "w")
for course in courses:
	outputfile.write("<h2>" + course + "</h2>")
	page = urllib.urlopen("http://www.mcgill.ca/study/2011-2012/courses/" + course.replace(" ", "-"))
	soup = BeautifulSoup.BeautifulSoup(page.read())
	page.close()
	result = soup.findAll('div', 'content')
	"""Assuming it's the 3rd such div, but this might change!"""
	outputfile.write(result[2].prettify())
	outputfile.write("\n<br><hr>")

outputfile.close()
