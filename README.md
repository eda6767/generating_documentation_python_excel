
#### Generating excel documentation using python scripts



<p align="center">
<img width="700" alt="Zrzut ekranu 2023-10-15 o 19 46 21" src="https://github.com/eda6767/generating_documentation_python_excel/assets/102791467/45715de9-83cf-47b5-a6b5-fa2d996c91bf">
</p>



<sub> In this project I will represent solution how to create automatical documentation for metrics calculated on database. Metrics </sub> 
definitions are represented in relational database, where we have given columns like metric name, gropouping key, destinantion table, source table, sql code, used columns, function etc. For business is more convenient to use documentation in form excel rather than using database. Moreover metrics are logically grouped into business areas like credit cards, credit products, deposits etc. Therefore that's why it was a requirement to represent metrics divided into business areas - each area in different excel file. Within an excel file metrics are grouped based on destination table - all metrics from given table are represented in separated sheet.


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


```python
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
<br>
</br>

As connected to database, we are fetching all metrics definitions to data frame, and then we choose unique list of areas. Then, we are able to 

create a list of objects,where each element corresponds to invidual area.
<br>
</br>

```python
    areas=connector.data['area_name'].unique()
    print(areas)
    
    logging.info('Creating an object class Catalog')

    areas_objects=[]
    for i in areas:
        areas_objects.append(Catalog(i))
```


Next, for creating excels I used writer - ExcelWriter

```python
 writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
```

Then, for each object represented area od aggregation we will create excel file :

```python
    for i in areas_objects:
        print('\n\n Creating documentation for area: {} \n\n'.format(i.area))
        file_name='Metrics_catalog_{}.xlsx'.format(i.area)
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        input_to_excel=pd.DataFrame()
```

Apart from the first sheet, which stands for intro to the documentation - subsequent workbooks contain definitions divided into target tables

```python
        for t in i.tables:
            print('Creating a workbook for target table: {}'.format(t))
            custom_dict = {'PROD': 0, 'TEST': 1, 'DRAFT': 3}
            sheet_i = i.data[i.data['target_table']==t].sort_values(by=['status'], key=lambda x: x.map(custom_dict))
            sheet_i.to_excel(writer, sheet_name=t, startrow = 1, index = False)
            workbook = writer.book
            worksheet = writer.sheets[t]
            style_header1= workbook.add_format({'bg_color': '#d2d1cb', 'align': 'center', 'font_size': 10, 'bold': False, 'font_color': 'black', 'border': 1, 'border_color':'white', 'text_wrap': True})
            style_header= workbook.add_format({'bg_color': '#2f2c1c', 'align': 'center', 'font_size': 10, 'bold': True, 'font_color': 'white'})
            style_describtions=workbook.add_format({'font_size': 11, 'italic': True, 'text_wrap': True})
            style_where=workbook.add_format({'font_size': 10, 'text_wrap': True})
            style_view_name=workbook.add_format({'font_size': 10, 'italic': False})
            worksheet.set_column('A:O', 40)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 40)
            worksheet.set_column('D:D', 20)
            worksheet.set_column('F:F', 30)
            worksheet.set_column('G:G', 30)
            worksheet.set_column('H:I', 10)
            worksheet.set_column('J:J', 30)
            worksheet.set_column('K:K', 35)
            worksheet.set_column('L:L', 35)
            worksheet.set_column('M:M', 35)
            worksheet.set_column('N:N', 40)
            worksheet.set_column('O:O', 15)
            worksheet.set_column('Q:T', 20)
            worksheet.write_row("A1:O1", i.extra_columns, style_header1)
            worksheet.write_row("A2:O2", i.columns, style_header)
            worksheet.set_column('E:E', 150, style_describtions)
            worksheet.set_column('N:N', 100, style_where)
            worksheet.set_column('P:P', 200, style_where)
            worksheet.set_column('A:A', 40, style_view_name)
            worksheet.set_zoom(80)
        writer.save()

```

