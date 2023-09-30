
#### Generating excel documentation using python scripts

<sub/>

<p align="center">

<img width="500" alt="Zrzut ekranu 2023-09-23 o 17 56 24" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/1a685de6-ce39-4bba-962a-3b201f5f4efd">

</p>


In this project I will represent solution how to create automatical documentation for metrics calculated on database. Metrics definitions are represented in relational database, 
where we have given columns like metric name, gropouping key, destinantion table, source table, sql code, used columns, function etc. For business is more convenient to use documentation in form excelrather than using database. Moreover metrics are logically grouped into business areas like credit cards, credit products, deposits etc. Therefore that's why it was a requirement to represents metrics divided into business areas - each area in different excel file. Within an excel file metrics are grouped based on destination table - all metrics from given table are represented in separated sheet.
In this solution i created an python object represented business area with atributes like metric list, data etc.


<p align="center">

<img width="600" alt="Zrzut ekranu 2023-09-23 o 19 10 28" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/7e7435c2-3569-4f95-87f1-7d751c664f9a">
</p>

<p align="center">
<img width="450" alt="Zrzut ekranu 2023-09-23 o 19 19 55" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/d1cee10c-0d99-445d-94cc-6b64aa806077">

</p>

