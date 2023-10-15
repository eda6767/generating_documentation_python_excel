
#### Generating excel documentation using python scripts

<sub/>

<p align="center">
<img width="500" alt="Zrzut ekranu 2023-09-23 o 17 56 24" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/1a685de6-ce39-4bba-962a-3b201f5f4efd">
</p>


In this project I will represent solution how to create automatical documentation for metrics calculated on database. Metrics definitions are represented in relational database, 
<br>
</br>

where we have given columns like metric name, gropouping key, destinantion table, source table, sql code, used columns, function etc. For business is more convenient to use 

documentation in form excel rather than using database. Moreover metrics are logically grouped into business areas like credit cards, credit products, deposits etc. Therefore 

that's why it was a requirement to represents metrics divided into business areas - each area in different excel file. Within an excel file metrics are grouped based 

on destination table - all metrics from given table are represented in separated sheet.


In this solution I created an python object represented business area with atributes like metric list, data etc.

<br>
</br>
So, for example we can have an area: credit cards with all metrics calculating values like: average balance on credit card, average amount of transations in given month, numer of transations in gas stations etc. Metrics within area are grouped based on destination table. In one table you can have up to 1000 metrics

<br>
</br>

<p align="center">

<img width="600" alt="Zrzut ekranu 2023-09-23 o 19 10 28" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/7e7435c2-3569-4f95-87f1-7d751c664f9a">
</p>

<p align="center">
<img width="450" alt="Zrzut ekranu 2023-09-23 o 19 19 55" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/d1cee10c-0d99-445d-94cc-6b64aa806077">

</p>

Our goal is to obtain an excel document, where each sheet will represent metrics wihin one target table, as below:

<br>
</br>

<p align="center">
<img width="1411" alt="Zrzut ekranu 2023-10-15 o 17 11 01" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/3c04b033-316f-4a42-affc-728314e3d827">
</p>


<br>
</br>

For this purpose I created an object Catalog which afterwards will represent each area with list of metrics and other artibutes.


```
class Catalog:
    
    def __init__(self, area, user=None, tables=None, data=None, file_name=None, columns= None, extra_columns=None):
        self.area = area
        self.data = data
        self.tables = tables
        self.file_name = file_name
        self.columns = columns
        self.extra_columns = extra_columns
        self.user = user

```

Next, for creating excels I used writer - ExcelWriter

```
 writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
```

