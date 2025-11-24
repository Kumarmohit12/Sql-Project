import pymysql
try:
    con_obj=pymysql.connect(
        user='root',
        password='Mohit@2003',
        host='127.0.0.1'
    )
    cur_obj=con_obj.cursor()
    # print(cur_obj)
    # cur_obj.execute('create database user_details')
    # print('database is created')
    # cur_obj.execute('create table user_details.user_info(name varchar(20), age int(10),address varchar(20))')
    # print('table is created')
    try:
        name=input('Enter Name : ')
        age=int(input("Enter Age : "))
        address=input('Enter Address : ')
        qry='insert into user_details.user_info(name,age,address) values(%s,%s,%s)'
        cur_obj.execute(qry,(name,age,address))
        con_obj.commit()
        print(cur_obj.rowcount,'rows are inserted')
        try:
            cur_obj.execute('select * from user_details.user_info   ')
            for table in cur_obj:
                print(table)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
except Exception as e:
    print(e)
