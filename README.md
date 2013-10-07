cloropleth_viz
==============

This code is for making a visualization of number and predominant race of executed offenders in Texas counties between 1982 and 2013. 

Written by Natalia Y. Bilenko, (c) 2013

Run from command line:

>> python create_map.py > map_name.svg

![alt tag](https://raw.github.com/nbilenko/cloropleth_viz/master/executed_prisoners_TX.png) { width: 200px; }

The code can be adapted for creating a cloropleth map of U.S. counties (though the visualization is Texas-specific).
It is based on a tutorial by Nathan Yau of Flowing Data (flowingdata.com):
http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

Data source:
Texas Department of Criminal Justice
http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html

Other resources used:
US FIPS Codes (Source: http://www.schooldata.com/pdfs/US_FIPS_Codes.xls)
Wikimedia US county svg map (Source: http://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg)
ColorBrewer (http://colorbrewer2.org/)