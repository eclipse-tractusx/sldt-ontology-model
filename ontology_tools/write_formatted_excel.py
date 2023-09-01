# Copyright (c) 2022,2023 T-Systems International GmbH
# Copyright (c) 2022,2023 Bayerische Motoren Werke Aktiengesellschaft (BMW AG) 
# Copyright (c) 2022,2023 ZF Friedrichshafen AG 
# Copyright (c) 2022,2023 Mercedes-Benz AG 
# Copyright (c) 2022,2023 Contributors to the Catena-X Association
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
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