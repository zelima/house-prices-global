The residential property price statistics collate data from different countries. The data comes [from Bank For International Settlements BIS](http://www.bis.org/statistics/pp.htm).

## data

Dataset will contain seprate CSV files with annual property price series for each country. Data will be structured as follows:

```
country-name-property-price.csv (Norway in this case)

year,code,price,unit
1819,A:NO:0:1:0:0:0:0,21.67,"Index 1912 = 100 (Units)"
1819,A:NO:0:1:0:0:1:0,0.0404,"Norwegian Krone (Thousands)"
1819,A:NO:2:1:0:0:0:0,21.67,"Index, 1912 = 100 (Units)"
...
...
1841,A:NO:0:1:0:0:0:0,20.38,"Index 1912 = 100 (Units)"
1841,A:NO:0:1:0:0:1:0,0.038,"Norwegian Krone (Thousands)"
1841,A:NO:2:1:0:0:0:0,20.38,"Index, 1912 = 100 (Units)"
1841,A:NO:2:1:0:0:1:0,0.1231,"Norwegian Krone (Thousands)"
```

The "code" column by itself means verius other options like

`Covered area, Real estate type, Real estate vintage, Compiling agency, Priced unit, Seasonal adjustment, Availability, Collection Indicator`

The definitions for "code" colum is provided on "documentation" sheet.

## license

Sources: National sources, BIS Residential Property Price database, www.bis.org/statistics/pp.htm.