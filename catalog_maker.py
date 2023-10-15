# -*- coding: utf-8 -*-


from connect_database import Connector
from catalog import Catalog
import pandas as pd
import logging
import os


print(os.getcwd())

def create_catalogs(user=None):
    user = input('Enter your database user: ')

    connector=Connector("KMB_PRE", user)
    connector.connect_database()
    
    areas=connector.data['area_name'].unique()
    print(areas)
    
    logging.info('Creating an object class Catalog')

    areas_objects=[]
    for i in areas:
        areas_objects.append(Catalog(i))

    for i in areas_objects:
        print(i.tables)
        print(i.area)
        print(i.columns)

    for i in areas_objects:
        i.choose_metrics(connector)

    for i in areas_objects:
        i.pick_tables(i.data)

    for i in areas_objects:
        i.pick_columns(i.data)

    for i in areas_objects:
        i.pick_extra_columns()
    
    
    for i in areas_objects:
        i.data['metric_id'] = i.data['metric_id'].astype(str)
        i.data['metric_id'] = i.data['metric_id'].apply(lambda x: x.replace(',', '.'))


    for i in areas_objects:
        print('\n\n Creating documentation for area: {} \n\n'.format(i.area))
        file_name='Metrics_catalog_{}.xlsx'.format(i.area)
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        x=pd.DataFrame()


        logging.info('Creating worksheet for Intro')
        x.to_excel(writer, sheet_name='Intro', startrow = 0, index = False)
        workbook = writer.book
        bg_format1 = workbook.add_format({'bg_color': '#ffffff'})
        worksheet = writer.sheets['Intro']

        for inx in range(0,50):
            worksheet.set_row(inx, cell_format= bg_format1)

        title_style= workbook.add_format({'font_size': 20, 'bold': True, 'font_color': 'black', 'text_wrap': True})
        worksheet.set_column('B:B', 60)
        worksheet.insert_image('A1', 'intro1.png')
        worksheet.insert_image('D10', 'intro2.png')
        worksheet.insert_image('A31', 'intro3.png')
        name=file_name.replace('_', ' ')[:-5]
        worksheet.write('B19', name, title_style)
    
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


if __name__ == "__main__":
    create_catalogs()
