
#### Generating excel documentation using python scripts

<sub/>

<p align="center">

<img width="600" alt="Zrzut ekranu 2023-09-23 o 17 56 24" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/a0b9fc5f-df3a-42e9-83ae-918794e06b1d">
</p>



In this project I will represent solution how to create automatical documentation for metrics calculated on database. Metrics definitions are represented in relational database, 
<br/> 

where we have given columns like metric name, gropouping key, destinantion table, source table, sql code, used columns, function etc. 
<br/> 

For business is more convenient to use documentation in form excelrather than using database. Moreover metrics are logically grouped into business areas like credit cards, credit 
<br/> 

products, deposits etc. Therefore that's why it was a requirement to represents metrics divided into business areas - each area in different excel file. Within an excel file metrics 
<br/> 

are grouped based on destination table - all metrics from given table are represented in separated sheet.
<br/> 
<br/> 


<br/> 
<br/> 
In this solution i created an python object represented business area with atributes like metric list, data etc.

<br/> 
<br/> 
<p align="center">

<img width="1150" alt="Zrzut ekranu 2023-09-23 o 19 10 28" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/cd2607b4-a389-40cd-82c2-ff03dbe01b8a">
</p>
