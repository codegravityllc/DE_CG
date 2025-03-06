--Check_Active Process
SHOW PROCESSLIST;
employees--Verifying_Open_Session
SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST;
--Check_Running_queries_from_Pycharm
SHOW FULL PROCESSLIST;
--Verifying_Open_Database_Connection
SHOW STATUS WHERE `variable_name` = 'Threads_connected';
--See_Active _Transcation
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
 --Check_open_User_Session
SELECT user, host FROM mysql.user;
