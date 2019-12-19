import os
import glob
import psycopg2
import pandas as pd
from queries import *
from pyspark.sql import SparkSession
from pyspark.sql.types import *
spark = SparkSession \
     .builder \
     .appName("Lake Dataset Project") \
     .config("spark.some.config.option", "some-value") \
     .getOrCreate()    
sc = spark.sparkContext


def process_lake_data(cur, filepath):
    """Read a lake file and
    insert data to lake table in database
    Args:
        cur (psycopg2.cursor): The psycopg2 cursor
        filepath (str): The location of the lake file
    """
    # open lake file
    lake_df = sc.textFile(filepath)
    header = lake_df.first()
    log_rows = lake_df.filter(lambda line: line != header)
    temp_var = log_rows.map(lambda k: k.split("\t"))
    df      =  temp_var.toDF(header.split("\t"))
    
    cur.execute(drop_lakes_table)
    cur.execute(create_lakes_table)
    for row in df.collect():
        record_to_insert = tuple(row.asDict().values())
        cur.execute(lake_insert_query, record_to_insert)
     
     



def process_data(cur, conn, filepath, func):
    """Read all files from the given location and
    execute the specified function
    Args:
        cur (psycopg2.cursor): The psycopg2 cursor
        conn (psycopg2.connection): The database connection
        filepath (str): The location of files to be processed
        func (function): The function to execute
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.txt'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
    print("inserted")




def main():
    
    conn = psycopg2.connect("dbname=mn_lakes user=kapil")
    cur = conn.cursor()
    process_data(cur, conn, filepath='Data/Lake data', func=process_lake_data)
    #process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()