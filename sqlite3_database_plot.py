import sqlite3
import os


def create_database(database_name = 'Econt_database', table_name = 'Econt_table'):
    conn = sqlite3.connect(f"{database_name}.db")
    # #create curse
    c = conn.cursor()

    # create table
    c.execute(f"""CREATE TABLE  {table_name}(
    chip_number DATATYPE,
    phase_scan_eRx,
    phase_scan_eTx,
    max_phase_width_eRx DATATYPE,
    max2_phase_width_eRx DATATYPE,
    max_phase_width_eTx DATATYPE,
    max2_phase_width_eTx DATATYPE
    )""")
    conn.close()

# load whole database to  XXX:
def load_database( database_name='Econt_database', table_name = 'Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f"SELECT  rowid, * FROM {table_name}")
    return c.fetchall()

# show in rows for each entry
def show_all_plan(database_name='Econt_database', table_name = 'Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f"SELECT  rowid, * FROM {table_name}")
    data = c.fetchall()
    for item in data:
        print(item)

# add new row
def add_one_row(item1,item2,item3,item4,item5,item6,item7,item8, item9, database_name='Econt_database', table_name='Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f"""INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?)""",(item0,item1,item2,item3,item4,item5,item6))
    conn.commit()
    conn.close()

# update one value in row
def update_one_in_row(where, value, row, database_name='Econt_database', table_name='Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f""" UPDATE {table_name} SET '{where}' = '{value}' WHERE rowid = {row} """)
    conn.commit()
    conn.close()

# delete a row
# pass row as string
def delete_one_row(row, database_name='Econt_database', table_name='Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f"""DELETE from {table_name} WHERE rowid = {row} """)
    conn.commit()
    conn.close()

#add many record may rows (list of string)
def add_many_column(list, database_name='Econt_database', table_name='Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.executemany(f"""INSERT INTO {table_name} VALUES (?,?,?,?,?,?,?)""",(list))
    conn.commit()
    conn.close()
# #add many record may rows (list of string)
# def add_many_column(list, database_name='Econt_database', table_name='Econt_table'):
#     conn = sqlite3.connect(f'{database_name}.db')
#     c = conn.cursor()
#     c.executemany(f"""INSERT INTO {table_name} VALUES (?,?,?)""",(list))
#     conn.commit()
#     conn.close()


# find in data database

def lookup(what, value, database_name='Econt_database', table_name='Econt_table'):
    conn = sqlite3.connect(f'{database_name}.db')
    c = conn.cursor()
    c.execute(f""" SELECT rowid, * from {table_name} WHERE {what} = '{value}' """)
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

# getting particular point value  correspaonding to a colum (chip_number=101) from another coulum (phase_scan_eRx)
def get_data_point(from_column='chip_number', chip=101, get_entry='phase_scan_eRx',database='Econt_database',table='Econt_table'):
    conn = sqlite3.connect(f'{database}.db')
    c = conn.cursor()
    c.execute(f"SELECT {get_entry} FROM {table} WHERE {from_column} = {chip}")
    return c.fetchall()

#getting a column (chip_number)
def get_column(column='chip_number',database='Econt_database',table='Econt_table'):
    conn = sqlite3.connect(f'{database}.db')
    c = conn.cursor()
    c.execute(f"SELECT {column} FROM {table}")
    return c.fetchall()
