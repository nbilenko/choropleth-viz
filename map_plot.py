import numpy as np
import csv
from BeautifulSoup import BeautifulSoup
import xlrd

# This is a visualization of number and predominant race of executed offenders in Texas counties between 1982 and 2013. 

# The code can be adapted for creating a cloropleth map of U.S. counties (though the visualization is Texas-specific).
# It is based on a tutorial by Nathan Yau of Flowing Data (flowingdata.com):
# http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

# Data source: http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html

# Other resources used:
# US FIPS Codes (Source: http://www.schooldata.com/pdfs/US_FIPS_Codes.xls)
# Wikimedia US county svg map (Source: http://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg)
# ColorBrewer (http://colorbrewer2.org/)


# Get FIPS codes for Texas counties:
fips_codes = {}
codebook = xlrd.open_workbook("US_FIPS_Codes.xls")
codesheet = codebook.sheet_by_index(0)
for ri in range(codesheet.nrows):
	try:
		curstate = codesheet.row(ri)[0].value
		curcounty = codesheet.row(ri)[1].value
		curfips = codesheet.row(ri)[2].value + codesheet.row(ri)[3].value
		if curstate == "Texas":
			fips_codes[curcounty] = curfips
	except:
		pass

# Define race groups:
races = ['Black', 'Hispanic', 'White']

# Read in data. Create a vector for each county with an entry for each row.
# For each execution, add 1 to the entry for the corresponding race.
executed = {}
reader = csv.reader(open("executed.csv"), delimiter = ",")
for row in reader:
	try:
		race = row[5]
		race_bin = races.index(race)
		county = row[6]
		try:
			fips = fips_codes[county]
		except:
			fips = "00000"

		if fips not in executed.keys():
			executed[fips] = np.zeros((len(races),))
		
		executed[fips][race_bin] += 1
	except:
		pass

# Load the cloropleth svg and load all paths using BeautifulSoup:
svg = open('counties.svg', 'r').read()
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
paths = soup.findAll('path')

# Choose contrasting colors to represent dominant race in each county:
colors = ["#00BF2F", "#002FBF", "#BF3700"]

# Copy the path style copied from the svg file manually, replace stroke, fill, and fill-opacity with variables to be filled in:
path_style = 'font-size:12px;fill-rule:nonzero;stroke:%s;stroke-opacity:1;stroke-width:0.2;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:%s;fill-opacity:%s'

# Color the counties based on predominant race executed, and determine opacity by number of executed prisoners:
for p in paths:
    if p['id'] not in ["State_Lines"]: # Preserve state lines.
        try:
            ex_num = executed[p['id']]
        except:
        	if p['id'][:2] =='48':
        		p['style'] = path_style % ("#FFFFFF", "#888888", 1)
        	else:
        		p['style'] = path_style % ("#FFFFFF", "#FFFFFF", 1)
        	continue
        race_max = np.argmax(ex_num)
        ex_total = ex_num.sum()
        opacity = min(float(ex_total)/10., 1)
        color = colors[race_max]
        p['style'] = path_style % ("#FFFFFF", color, opacity)
    # else:
        # p['style'] = path_style % ("FFFFFF", "FFFFFF", 1)

# Output map
print soup.prettify()

# Final edits to the visualization were made in Adobe Illustrator.