import csv
import os
import openpyxl
from openpyxl.utils import get_column_letter
import time
import logging


class excel_tool():

    def __init__(self, filename: str):

        self.file_name = filename + ".xlsx"
        self.sheet_name = "Sheet1"

        # 工作簿文件路径
        self.workbook_file_path = os.path.join(os.getcwd(), "logs",
                                               self.file_name)
        # 工作簿当前目录
        self.workbook_dir_path = os.path.dirname(self.workbook_file_path)

        # 如果不存在目录路径,就创建
        if not os.path.exists(self.workbook_dir_path):
            os.makedirs(self.workbook_dir_path)

        if os.path.exists(self.workbook_file_path):
            self.wb = openpyxl.load_workbook(self.workbook_file_path)
        else:
            self.wb = openpyxl.Workbook(write_only=False)  # write only模式，减小内存

    def workbook_rewrite(self, data: list, sheet_name: str = "Sheet1"):
        '''
        : data: if it is a 1dim list, it is one row
        : data: if it is a 2dim list, each entry is one row.
        '''
        if sheet_name in self.wb.sheetnames:
            self.wb.remove(self.wb[sheet_name])


#        sheet_num = len(self.wb.sheetnames)
        self.wb.active
        sheet = self.wb.create_sheet(title=sheet_name, index=0)
        if isinstance(data, list) and isinstance(data[0], (list, tuple)):
            for eachrow in data:
                sheet.append(eachrow)
        elif isinstance(data, list) and isinstance(data[0], (str, int)):
            sheet.append(data)
        self.wb.save(self.workbook_file_path)  # 保存文件

    def workbook_append(self, data: list, sheet_name: str = "Sheet1"):
        '''
        : data: if it is a 1dim list, it is one row
        : data: if it is a 2dim list, each entry is one row.
        '''
        if sheet_name not in self.wb.sheetnames:
            sheet = self.wb.create_sheet(title=sheet_name, index=0)
        else:
            sheet = self.wb[sheet_name]
        # print("before", self.get_sheet_rows())
        if isinstance(data, list) and isinstance(data[0], (list, tuple)):
            for eachrow in data:
                sheet.append(eachrow)
        elif isinstance(data, list) and isinstance(data[0], (str, int)):
            sheet.append(data)
        self.wb.save(self.workbook_file_path)  # 保存文件
        # print("after", self.get_sheet_rows())

    def style(self):
        #from openpyxl.styles import Alignment
        # align=Alignment(horizontal="left",vertical="center",wrap_text=False)
        # sheet.column_dimensions["A"].width = 10  # default value: 8.38
        # sheet.column_dimensions["B"].width = 20  # default value: 8.38
        sheets = self.wb.sheetnames
        for sheet in sheets:
            ws = self.wb[sheet]
            # 计算每列最大宽度，并存储在列表column_widths中
            column_widths = []
            for column in range(1, ws.max_column + 1):  # 每列循环
                lk = 1
                for row in range(1, ws.max_row + 1):  # 每行循环
                    # 获取该列每个单元格的value
                    cell = ws.cell(row=row, column=column).value
                    if isinstance(cell, str):
                        # utf-8 每个中文3个字节, gbk 每个中文2个字节
                        lkn = len(cell.encode("gbk"))
                    else:
                        lkn = len(str(cell))
                    if lk < lkn:
                        lk = lkn
                column_widths.append(lk)  # 将每列的最大列宽加入列表lks中
            # print(column_widths)
            # 设置列宽
            for i in range(1, ws.max_column + 1):
                letter = get_column_letter(i)  # 数字转化为列名
                # 设置列宽，一般+2
                ws.column_dimensions[letter].width = column_widths[i - 1] + 2
        self.wb.save(self.workbook_file_path)

    def write_cell_value(self,
                         row_no,
                         col_no,
                         value,
                         style=None,
                         sheet_name=None):
        if sheet_name is not None:
            self.get_sheet_by_name(sheet_name)
        if style == None:
            style = openpyxl.styles.colors.BLACK
        elif style.upper() == "RED":
            style = openpyxl.styles.colors.RED
        elif style.upper() == "GREEN":
            style = openpyxl.styles.colors.GREEN
        self.ws.cell(row=row_no,
                     column=col_no).font = openpyxl.styles.Font(color=style)
        self.ws.cell(row=row_no, column=col_no).value = value
        self.wb.save(self.workbook_file_path)
        return True

    def workbook_read(self, sheet_name: str):
        '''
        get all the data from the sheet
        retuen a 2dim list
        '''
        if os.path.exists(self.workbook_file_path):
            sheet = self.wb[sheet_name]
            res = list(sheet.values)
            return res

    def get_cell_value(self, sheet_name: str, row: int = 1, col: int = 1):
        '''
        get the data from a cell.
        :param row: 所在行
        :param col: 所在列
        '''
        if os.path.exists(self.workbook_file_path):
            sheet = self.wb[sheet_name]
            res = sheet.cell(row=row, column=col).value
            return res

    def get_sheet_rows(self, sheet_name: str = "Sheet1"):
        '''
        get the max rows of a sheet
        '''
        if os.path.exists(self.workbook_file_path):
            sheet = self.wb[sheet_name]
            max_rows = sheet.max_row
            return max_rows

    def get_sheet_columns(self, sheet_name: str):
        '''
        get the max rows of a sheet
        '''
        if os.path.exists(self.workbook_file_path):
            sheet = self.wb[sheet_name]
            max_columns = sheet.max_column
            return max_columns

    def get_row_data(self, sheet_name: str, row_num: int = 1):
        '''
        get the data for a row
        param row_num: number of the row, int, start from 1
        return: list
        '''
        row_list = excel_tool.workbook_read(self, sheet_name)[row_num - 1]
        return row_list

    def get_column_data(self, sheet_name: str, col_num: int = 1):
        '''
        get the data for a column
        param col_num: number of the column, int, start from 1
        return: list
        '''
        if os.path.exists(self.workbook_file_path):
            sheet = self.wb[sheet_name]
            col_list = []
            for i in list(sheet.columns)[col_num - 1]:
                col_list.append(i.value)
            return col_list

    def get_sheet_by_name(self, sheet_name):
        sheet = self.wb.get_sheet_by_name(sheet_name)
        # sheet = self.wb[sheet_name]  # 方式二也可以
        return sheet

    # 通过索引获取sheet表

    def get_sheet_by_index(self, index):
        sheet_name = self.wb.sheetnames[index - 1]
        self.ws = self.wb[sheet_name]
        return self.ws

    # 获取所有的sheet名,列表格式

    def get_all_sheet_names(self):
        return self.wb.sheetnames

    def write_cell_value(self,
                         row_no,
                         col_no,
                         value,
                         style=None,
                         sheet_name=None):
        if sheet_name is not None:
            self.get_sheet_by_name(sheet_name)
        if style == None:
            style = openpyxl.styles.colors.BLACK
        elif style.upper() == "RED":
            style = openpyxl.styles.colors.RED
        elif style.upper() == "GREEN":
            style = openpyxl.styles.colors.GREEN
        self.ws.cell(row=row_no,
                     column=col_no).font = openpyxl.styles.Font(color=style)
        self.ws.cell(row=row_no, column=col_no).value = value
        self.save_excel()
        return True

    def wookbook_close(self):
        self.wb.close()


def ip_read(filename: str):
    file_path = os.getcwd() + filename
    ip_file = open(file_path, "r")
    ip_list = ip_file.readlines()
    return ip_list


class csv_tool():

    def __init__(self, filename: str):
        cur_time = time.strftime("_%Y%m%d_%H%M%S")
        self.filename = filename + cur_time + ".csv"
        self.file_path = os.path.join(os.getcwd(), "logs", self.filename)
        self.logs_dir_path = os.path.dirname(self.file_path)
        # 如果不存在目录路径,就创建
        if not os.path.exists(self.logs_dir_path):
            os.makedirs(self.logs_dir_path)

        # 创建csv文件，newline="" 去除writerows 后面的空行
        self.f_csv = open(file=self.file_path, mode='w', newline="")
        self.csv_writer = csv.writer(self.f_csv)

    def write_head(self, head: list):
        '''
        : head: a 1dim list, e.g. ["ip","slot","slot_oct"]
        '''
        self.csv_writer.writerow(head)
        self.f_csv.flush()

    def write_rows(self, rows: list):
        '''
        : rows: a 2dim list, e.g. [["1.1.1.1","1","1103"],["2.2.2.2","2","1104"]]
        '''
        self.csv_writer.writerows(rows)
        self.f_csv.flush()

    def csv_close(self):
        self.f_csv.close()


class log_file():

    def __init__(self, filename: str, olt_ip: str):
        # cur_time = time.strftime("%Y%m%d_%H%M%S")
        self.filename = filename + "_" + olt_ip + ".log"
        self.file_path = os.path.join(os.getcwd(), "logs", self.filename)
        self.logs_dir_path = os.path.dirname(self.file_path)
        # 如果不存在目录路径,就创建
        if not os.path.exists(self.logs_dir_path):
            os.makedirs(self.logs_dir_path)

        # 创建csv文件，newline="" 去除writerows 后面的空行
        self.f_log = open(file=self.file_path,
                          mode='a+',
                          newline="",
                          encoding="utf-8",
                          errors="ignore")

    def write(self, output):
        # 如果是bytes，则转换为string
        if type(output) == bytes:
            output = str(output, "utf-8")
        self.f_log.writelines(output)

    def info(self, output: str):
        self.f_log.writelines(output)

    def flush(self):
        self.f_log.flush()

    def close(self):
        self.f_log.close()


class logger():

    def __init__(self, filename: str, ip: str):
        cur_time = time.strftime("_%Y%m%d_%H%M%S")
        self.filename = filename + "_" + ip + cur_time + ".log"
        self.file_path = os.path.join(os.getcwd(), "logs", self.filename)
        self.logs_dir_path = os.path.dirname(self.file_path)
        if not os.path.exists(self.logs_dir_path):
            os.makedirs(self.logs_dir_path)
        # create a logger
        # self.logger_root = logging.getLogger()
        # self.logger_root.setLevel(logging.DEBUG)
        self.logger = logging.getLogger(self.filename)
        self.logger.setLevel(logging.DEBUG)

        # create a handler and set its formatter  #[%(levelname)s]  '%Y-%m-%d %H:%M:%S'
        #fmt = logging.Formatter('[%(asctime)s] %(message)s')
        fmt = logging.Formatter('%(message)s')
        self.fh = logging.FileHandler(self.file_path, encoding="UTF-8")
        self.fh.setFormatter(fmt)
        self.fh.setLevel(logging.DEBUG)

        # add handlerto logger
        self.logger.addHandler(self.fh)
        # print(self.logger.handlers)  handler is a list
        # print(self.logger)  logger is a object, the default is root logger.
        self.fmt_p = logging.Formatter('%(message)s')

    def debug(self, message):
        self.logger_root.debug(message)
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

    # used for pexpect log
    def write(self, message):
        self.fh.setFormatter(self.fmt_p)
        self.logger.info(message)

    def flush(self):
        self.fh.flush()

    def close(self):
        self.logger.removeHandler(self.fh)
        self.fh.close()


if __name__ == "__main__":
    # read the table from db, reture a 2dim list
    import db_class
    time_begin = time.time()
    cursor = db_class.LiteDb("olt_info")
    res_lt_mapping = cursor.query("select * from lt_mapping")
    title_lt_mapping = [["slot", "slot_oct"]]
    res_lt_mapping = cursor.query("select * from lt_mapping")
    title_lt_mapping.extend(res_lt_mapping)
    del res_lt_mapping
    print(title_lt_mapping)
    res_fgltd_pon = cursor.query("select * from fgltd_pon")
    title_fgltd_pon = [["pon", "pon_pom"]]
    title_fgltd_pon.extend(res_fgltd_pon)
    del res_fgltd_pon

    # test the class excel_tool
    myfile = excel_tool("db_readout")
    # myfile.workbook_rewrite(title_lt_mapping, sheet_name="lt_mapping")
    # myfile.workbook_rewrite(title_fgltd_pon, sheet_name="fgltd_pon")
    myfile.workbook_append(title_lt_mapping, sheet_name="lt_mapping")
    myfile.workbook_append(title_lt_mapping, sheet_name="lt_mapping")
    myfile.workbook_append(['slot', 'slot_oct'], sheet_name="lt_mapping")
    myfile.workbook_append(['slot两个黄鹂鸣翠柳，一行白鹭上青天', 'slot_oct12345678'],
                           sheet_name="lt_mapping")
    myfile.style()
    # print(myfile.workbook_read("lt_mapping"))
    # print(myfile.workbook_read(sheet_name="fgltd_pon"))
    # print(myfile.get_sheet_rows("lt_mapping"))
    # print(myfile.get_sheet_columns("lt_mapping"))
    # print(myfile.get_cell_value("lt_mapping", row=2, col=2))
    # print(myfile.get_column_data("lt_mapping", col_num=1))
    # print(myfile.get_row_data("lt_mapping", row_num=1))

    # test the clasee csv_tool
    # mycsv = csv_tool("db_readout")
    # mycsv.write_rows(title_lt_mapping)
    # mycsv.csv_close()
    time_end = time.time()

    # test class logger

    # clilog = logger('clilog', "1.1.1.1")
    # clilog.info('一个info信息')
    # time.sleep(1)
    # clilog.cri('一个致命critical信息 over')

    # octlog = logger('octlog', "1.1.1.1")
    # octlog.info('一个info信息')
    # time.sleep(1)
    # octlog.cri('一个致命critical信息 ')
    #print("script total consume time:" + str(int(time_end-time_begin)))
