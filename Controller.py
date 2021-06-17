from Database import DB


class Account:
    __connection = None

    def __init__(self):
        self.__connection = DB("database.db").Connect()

    def Login(self, users):
        """
        This code is the logic of login.
        """
        if self.__IsValidLogin(users):
            if self.__IsAuthentic(users):
                self.__Authorize(users)
            else:
                users.setMessage("Incorrect username or password!")
        else:
            users.setMessage("Please write a username and a password!")

    def __IsValidLogin(self, users):
        """
        This code is check the login is valid.
        """
        if users.getUsername() != "" and users.getPassword() != "":
            return True
        return False

    def __IsAuthentic(self, users):
        """
        This code is check the login is authentic.
        """
        cur = self.__connection.cursor()
        cur.execute("SELECT id FROM accounts WHERE username = '" +
                    users.getUsername()+"' AND password = '"+users.getPassword()+"'")
        record = cur.fetchone()
        if record != None:
            users.setId(record[0])
            return True
        return False

    def __Authorize(self, users):
        users.setMessage("Successfully logged in, Welcome " +
                         users.getUsername() + " ID:["+str(users.getId())+"]")


class ProductsController:
    __connection = None

    def __init__(self):
        self.__connection = DB("database.db").Connect()

    def getAllProducts(self):
        """
        This code is get all products from the database.
        """
        cur = self.__connection.cursor()
        cur.execute("SELECT * FROM products")
        records = cur.fetchall()

        return records

    def UpdateProduct(self, data, selected):
        """
        This code is update the selected product.
        """
        if self.__IsValidData(data):
            cur = self.__connection.cursor()
            cur.execute("UPDATE products SET name='"+data.getName()+"', brand='"+data.getBrand()+"', release_date='"+data.getReleaseDate()+"', display_size='"+data.getDisplaySize() +
                        "', display_type='"+data.getDisplayType()+"', cpu='"+data.getCPU()+"', ram='"+data.getRAM()+"', nocamera='"+data.getNoCameras()+"' WHERE id = '"+str(selected)+"'")
            self.__connection.commit()
            data.setMessage("Update was successful!")
        else:
            data.setMessage("Please fill every blank form!")

    def DeleteProduct(self, data, selected):
        """
        This code is delete the selected product.
        """
        if selected != "":
            cur = self.__connection.cursor()
            cur.execute("DELETE FROM products WHERE id = '" +
                        str(selected) + "'")
            self.__connection.commit()
            data.setMessage("Delete was successful!")
        else:
            data.setMessage("Select a row!")

    def AddProduct(self, data):
        """
        This code is add a new product to the database.
        """
        if self.__IsValidData(data):
            cur = self.__connection.cursor()
            cur.execute("INSERT INTO products (name, brand, release_date, display_size, display_type, cpu, ram, nocamera) VALUES('"+data.getName()+"','"+data.getBrand() +
                        "','"+data.getReleaseDate()+"','"+data.getDisplaySize()+"','"+data.getDisplayType()+"', '"+data.getCPU()+"', '"+data.getRAM()+"', '"+data.getNoCameras()+"')")
            self.__connection.commit()
            data.setMessage("Insert was successful!")
        else:
            data.setMessage("Please fill every blank form!")

    def __IsValidData(self, data):
        """
        This code is check the datas from the forms are valid.
        """
        if data.getName() != "" and data.getBrand() != "" and data.getReleaseDate() != "" and data.getDisplaySize() != "" and data.getDisplayType() != "" and data.getCPU() != "" and data.getRAM() != "" and data.getNoCameras() != "":
            return True
        return False
