#!/usr/bin/python

import openpyxl
import json
import pandas as pd
import os

def excel_to_json(path):
    wb = openpyxl.load_workbook(path)
    excel_data = {}
    for sheet in wb.sheetnames:
        data = []
        for rows in wb[sheet]:
            row_data=[]
            for col in rows:
                row_data.append(col.value)
            data.append(row_data)
        excel_data[sheet]=data
    
    with open('tmp.json', mode='w', encoding='utf-8') as jf:
        json.dump(excel_data, jf, indent=2, sort_keys=True, ensure_ascii=False)

def json_load():
    with open('tmp.json', 'r') as jf:
        data = json.load(jf)
    # print(type(data))
    return data

def module_connection_gen(data):
    sheet = data['Sheet1']
    with open('result.v', 'w') as f:

        # signal defination
        for i in range(1, len(sheet)):      
            connect_signal = sheet[i][2]
            signal_type = sheet[i][3]
            signal_bits = sheet[i][4]
            if(signal_type != None):
                line = "%s      [ %d : 0 ] \t %-15s; \n" % (signal_type, signal_bits-1, connect_signal)
                f.write(line)
                print(line)
        line = '\n'
        f.write(line)
        print(line)

        # signal connection
        for i in range(1, len(sheet)):      
            if(sheet[i][0] != None): top_name = sheet[i][0]

            top_module = sheet[i][0]
            module_signal = sheet[i][1]
            connect_signal = sheet[i][2]
            if(top_module != None):                                 # module top line 
                line = "\n /*############# \t %s module start \t ###############*/ \n" %(top_name)
                f.write(line)
                # print(line)
                line = "\n%s  %s_inst ( \n"  %(top_name, top_name)
                f.write(line)
                # print(line)
            elif(i == len(sheet)-1 or sheet[i+1][0] != None):        # module end line
                line = "\t .%-15s ( %-15s \t) \n" %(module_signal, connect_signal)
                f.write(line)
                # print(line)
                line = '); \n'
                f.write(line)
                # print(line)
                line = "\n /*############# \t %s module end \t ###############*/ \n" %(top_name)
                f.write(line)
                # print(line)
            else:                                                   # module middle line
                line = "\t .%-15s ( %-15s \t), \n" %(module_signal, connect_signal)
                f.write(line)
                # print(line)
            




if __name__=='__main__':
    file_path = './reg_table.xlsx'
    excel_to_json(file_path)
    data = json_load()
    module_connection_gen(data)
