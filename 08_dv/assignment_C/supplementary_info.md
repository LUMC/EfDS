# Assignment C

The assignment is published on the github repository under de data visualisation section `08_dv` [https://github.com/LUMC/EfDS/](https://github.com/LUMC/EfDS/tree/main/08_dv/assignment_C). 

Below you will find additional information on the questions in the assignment.    

## Q1: Metadata

The metadata has clearly 3 &nbsp;separate tables with key/title/description headings:

- emission sectors containing 59 keys , e.g. 1050010, B000579, B000580 ...
- emission types containing 14 emissions, e.g. &nbsp;TotalCO2_1, CO2ExclBiomass_2, CO2Biomass_3 ...
- periods with periods, e.g. 1990JJ00, 1991JJ00, 1992JJ00

You only need the first two. The tables in the snapshot of the data have specific 
coordinates, to fetch them you need to manually inspect them to find out those 
coordinates.&nbsp; &nbsp;After reading the metadata csv file, you can fetch them 
using slices of the DataFrame and process them further to create GWP.emission_sources 
and GWP.emission.&nbsp; There may exist more sophisticated solutions to fetch 
arbitrary number of DataFrames from an untidy DataFrame.

The variables `Date` and `Source` are added to the raw data `GWP.data` as shown in the 
instance output `gwp.data.dtypes`.

## Q2: Greenhouse equivalents

Different gases have different levels of contribution to greenhouse gas. The following 
description is given in the metadata under 'Greenhouse gas equivalents':

_"A measure of the degree to which a substance contributes to the greenhouse effect. 
A greenhouse gas equivalent equals the effect that the emission of 1 kg of carbon 
dioxide (CO2) has, as a reference. The emission of 1 kg of methane (CH4) is equal 
to 25 greenhouse gas equivalents, and the emission of 1 kg of nitrous oxide gas 
(N2O) equal to 298 greenhouse gas equivalents. The fluorine (chlorine) gases each 
have a high CO2 equivalent, but because the emitted quantities are relatively small, 
their contribution to the national total is small. The fluorine (chlorine) gases 
are only included in the total, but they are not specified."_

As it mentions the `fluorine (chlorine)` or HFC is included in the total greenhouse 
gas equivalent (GreenhouseGasEquivalents_6).&nbsp; In order to calculate HFC column 
you'll need to convert N2O and CH4&nbsp; to CO2-equivalents based on the rates 
given above.&nbsp; We have Total CO2 (TotalCO2_1) then:

> total CO2-equivalents&nbsp; = Total CO2&nbsp; &nbsp;+ N2O CO2-equivalents + CH4 CO2-quivalents.

The difference between *'total CO2-equivalents'* and *GreenhouseGasEquivalents_6* 
represents all other minor gases that are not specified as a separate variable. 
Since fluorine (chlorine) was explicitly mentioned we assign this difference 
to variable HFC (hydrofluorocarbons).


> **Update April 16th, 2024** 

HFC calculation may contain negative values. Possible reasons for these fluctuations
may be due to reporting, measurement etc. We are not investigating the sources of these
fluctuations, so you may ignore this and leave the data as it is as long a new column HFC
is created based on the description here above.


## Q3: Implement a plot method that produces the figure below.

As some of have correctly pointed out, the question is not clear and specific enough. 
The example plot in question 4 with the query 'transport' uses exact match on the 
word 'transport' and not the pattern 'transportation', so it will miss those words in 
the search.&nbsp; Your results therefore may differ. Both pattern and word search 
implementations are accepted.

Another point is whether the 'Title' variable should be included in the search 
alongside the description variable. You may include the 'Title' also in your search 
but using only the 'Description' variable will suffice.

## Q4: Emission categories

HFC is wrongly categorised under *air pollution*, it should belong to&nbsp; greenhouse 
gases. That is the reason HFC does not show up in the plot in question 4.

> **Update April 16th, 2024**

The example plot shows 4 emission sources based on the pattern `transport`. The search here
was done on the `emmision_sources.Description` only. A pattern search on `emmision_sources.Title` will 
result into more hits. A third option would be to take the union of hits in both 
columns in `emission_sources`. All choices are counted as correct as long is the 
search function is in place.