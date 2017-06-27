Install
=========

* Open terminal

* Go to the path you want create the project and create a folder

  ```
  mkdir tuff && cd tuff
  ```

* Create a virtual machine

    ```
    virtualenv 
    ```

* Open the virtual machine

    ```
    source /bin/activate
    ```

* Create the project

    ```
    django-admin.py startproject --template=https://github.com/pedrosilva88/djagoTemplate/archive/master.zip --extension=py,rst,html tuff
    ```

* Enter in the Prject folder

    ```
    cd tuff
    ```

* Install the requirements
    ```
   pip install -r requirements/local.txt
    ```

 Database
 =========

  * Open Postgres shell (You should have PostGres installed)

   ```
   sudo su - postgres
   ```

 * Create Database

   ```
   CREATE DATABASE tuff;
   ```

 * Create User to manage database

   ```

   CREATE USER  WITH PASSWORD '';
   ALTER ROLE  SET client_encoding TO 'utf8';
   ALTER ROLE  SET default_transaction_isolation TO 'read committed';
   ALTER ROLE  SET timezone TO 'UTC';
   \q
   ```
