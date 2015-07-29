/* Simple C program that connects to MySQL Database server*/

//gcc testMySqlC1.c -o testMySqlC1 `mysql_config --cflags --libs`

#include <mysql.h>
#include <stdio.h>
main() {
   MYSQL *conn;
   MYSQL_RES *res;
   MYSQL_RES *res2;
   MYSQL_ROW row;
   char *server = "localhost";
   char *user = "test";
   char *password = "test"; /* set me first */
   char *database = "test";
   conn = mysql_init(NULL);
   /* Connect to database */
   if (!mysql_real_connect(conn, server,
         user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      //exit(1);
   }
   /* send SQL query */
   if (mysql_query(conn, "show tables")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      //exit(1);
   }
   res = mysql_use_result(conn);
   /* output table name */
   printf("MySQL Tables in mysql database:\n");
   while ((row = mysql_fetch_row(res)) != NULL)
      printf("%s \n", row[0]);
   /* close connection */

   if (mysql_query(conn, "SELECT * FROM col2;")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      //exit(1);
   }

   res2 = mysql_use_result(conn);

   while ((row = mysql_fetch_row(res2)) != NULL)
      printf("%s, %s \n", row[0], row[1]);

   mysql_free_result(res);
   mysql_close(conn);
}
