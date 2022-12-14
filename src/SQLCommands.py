createInventory = """
    CREATE TABLE Inventory (
        Name VARCHAR(255), Count INT,
        PRIMARY KEY (Name)
    )
    """
insertInventory = """
    INSERT INTO INVENTORY(Name, Count) VALUES(%s, %s)
    """

insertInventoryIndex = """ 
CREATE INDEX InventoryIndex
ON INVENTORY (Name, Count)
"""

createEmployees = """
    CREATE TABLE Employees (
        Employee_ID INT, Name VARCHAR(255), Salary INT,
        Job VARCHAR(255),
        PRIMARY KEY (Employee_ID)
    )
    """
insertEmployee = """
    INSERT INTO Employees(Employee_ID, Name, Salary, Job) VALUES(%s, %s, %s, %s)
    """
insertEmployeeIndex = """ 
CREATE INDEX EmployeeIndex
ON Employees (Name) 
"""
createCustomer = """
    CREATE TABLE Customer (
        Customer_ID INT, Name VARCHAR(255),
        Place_in_line INT, Order_ID INT,
        PRIMARY KEY (Customer_ID),
        FOREIGN KEY (Order_ID) REFERENCES User_order(Order_ID)
    ) 
    """
insertCustomer = """
    INSERT INTO Customer(Customer_ID, Name, Place_in_line, Order_ID) VALUES(%s, %s, %s, %s)
    """
insertCustomerIndex = """ 
CREATE INDEX CustomerIndex
ON Customer (Name) 
"""
createProtein = """
    CREATE TABLE Protein (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price DOUBLE, Extra_price DOUBLE,
        PRIMARY KEY (Name)
    )   
    """
insertProtein = """
    INSERT INTO Protein(Name, Volume, Calories, Fat, Price, Extra_price) VALUES(%s, %s, %s, %s, %s, %s)
    """
insertProteinIndex = """ 
CREATE INDEX ProteinIndex
ON Protein (Name, Price) 
"""
insertProteinIndex2 = """ 
CREATE INDEX ProteinIndex2
ON Protein (Name, Volume)
"""
createIngredient = """
    CREATE TABLE Ingredient (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price DOUBLE, Extra_price DOUBLE,
        PRIMARY KEY (Name)
    )
    """
insertIngredient = """
    INSERT INTO Ingredient(Name, Volume, Calories, Fat, Price, Extra_price) VALUES(%s, %s, %s, %s, %s, %s)
    """
insertIngredientIndex = """ 
CREATE INDEX IngredientIndex
ON Ingredient (Name, Price) 
"""
insertIngredientIndex2 = """ 
CREATE INDEX IngredientIndex2
ON Ingredient (Name, Volume) 
"""
createOrder = """
    CREATE TABLE User_order (
        Order_ID INT, Customer_ID INT, Employee_ID INT,
        Name VARCHAR(255),
        PRIMARY KEY (Order_ID),
        FOREIGN KEY (Employee_ID) REFERENCES Employees(Employee_ID)
    )
    """
insertOrder = """
    INSERT INTO User_Order(Order_ID, Customer_ID, Employee_ID, Name) VALUES(%s, %s, %s, %s)

    """
createProteinList = """
    CREATE TABLE Protein_list (
        Order_ID INT, Name VARCHAR(255)
    )
    """
insertProteinList = """
    INSERT INTO Protein_list(Name) VALUES(%s)
    """
createIngredientList = """
    CREATE TABLE Ingredient_list (
        Order_ID INT, Name VARCHAR(255)
    )
    """
insertIngredientList = """
    INSERT INTO Ingredient_list(Name) VALUES(%s)
    """

