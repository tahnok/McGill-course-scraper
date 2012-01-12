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
outputfile.write("<html><body>")
for course in courses:
	page = urllib.urlopen("http://www.mcgill.ca/study/2011-2012/courses/" + course.replace(" ", "-"))
	soup = BeautifulSoup.BeautifulSoup(page.read())
	page.close()
	title = soup.findAll('h1')
	outputfile.write(str(title[1]).replace("h1", "h3"))
	result = soup.findAll('div', 'content')
	"""Assuming it's the 3rd such div, but this might change!"""
	outputfile.write(result[2].prettify())
	outputfile.write("\n<br><hr>")
outputfile.write("</body></html>")

outputfile.close()
