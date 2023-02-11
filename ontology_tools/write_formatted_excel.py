import pandas as pd

def write_formatted_excel(df, file='file.xlsx', sheet_name='Sheet1', column_width=15.83):
    writer = pd.ExcelWriter(file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]

    # font format
    column_format = workbook.add_format({'font_name': 'Helvetica Neue', 'font_size': '10'})
    worksheet.set_column(0, len(df.columns)-1, column_width, column_format)

    # class format
    class_format = workbook.add_format({'font_color': 'blue', 'bold': True})
    class_condition = {'type': 'cell', 'criteria': 'equal to', 'value': '"class"', 'format': class_format}
    worksheet.conditional_format('A1:A999', class_condition)

    # relation format
    relation_format = workbook.add_format({'font_color': 'orange'})
    relation_condition = {'type': 'cell', 'criteria': 'equal to', 'value': '"relation"', 'format': relation_format}
    worksheet.conditional_format('A1:A999', relation_condition)

    # attribute format
    attribute_format = workbook.add_format({'font_color': 'purple'})
    attribute_condition = {'type': 'cell', 'criteria': 'equal to', 'value': '"attribute"', 'format': attribute_format}
    worksheet.conditional_format('A1:A999', attribute_condition)

    # write format
    writer.save()