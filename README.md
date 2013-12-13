choropleth-viz
==============

This code is for making a visualization of number and predominant race of executed offenders in Texas counties between 1982 and 2013. 

Written by Natalia Y. Bilenko, (c) 2013

Run from command line:

>> python create_map.py > map_name.svg

<img src="https://raw.github.com/nbilenko/cloropleth_viz/master/executed_offenders_TX.png" alt="Executed offenders in Texas" width="500">

The code can be adapted for creating a choropleth map of U.S. counties (though the visualization is Texas-specific).<br>
It is based on a <a href="http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/">tutorial</a> by Nathan Yau of <a href="http://flowingdata.com">Flowing Data</a>.

Data source:<br>
Texas Department of Criminal Justice:
<a href="http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html">Executed Offenders in Texas</a>

Other resources used:<br>
US FIPS Codes (<a href="http://www.schooldata.com/pdfs/US_FIPS_Codes.xls">Source</a>)<br>
Wikimedia US county svg map (<a href="http://commons.wikimedia.org/wiki/File:USA_Counties_with_FIPS_and_names.svg">Source</a>)
<a href="http://colorbrewer2.org/">ColorBrewer</a>