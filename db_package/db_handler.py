# File Name : db_handler
# Student Name: Josh Slocumb, Richie James
# email:slocumjt@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   04/03/2025
# Course #/Section:  IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  

# Brief Description of what this module does: Database connection and query handler for Grocery Store Simulator
#Handles all SQL Server interactions 
# Citations: Perplexity AI


import pyodbc

class DatabaseHandler:
    """Manages database connections and executes all SQL queries"""
    
    def __init__(self):
        """Initialize database connection parameters"""
        self.conn = None
        self.connection_string = (
            'Driver={SQL Server};'
            'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
            'Database=GroceryStoreSimulator;'
            'uid=IS4010Login;'
            'pwd=P@ssword2;')
    
    def connect(self) -> bool:
        """Establish database connection"""
        try:
            self.conn = pyodbc.connect(self.connection_string)
            return True
        except pyodbc.Error as e:
            print(f"Database connection failed: {str(e)}")
            return False
    
    def get_products(self) -> list:
        """Execute product query (Assignment Step 1)"""
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        return self._execute_query(query)
    
    def get_manufacturer(self, manufacturer_id: int) -> str:
        """Get manufacturer name (Assignment Step 3-4)"""
        query = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?"
        return self._execute_query(query, [manufacturer_id])[0][0]
    
    def get_brand(self, brand_id: int) -> str:
        """Get brand name (Assignment Step 5)"""
        query = "SELECT Brand FROM tBrand WHERE BrandID = ?"
        return self._execute_query(query, [brand_id])[0][0]
    
    def get_sales_data(self, product_id: int) -> int:
        """Get sales numbers (Assignment Step 6)"""
        query = """
            SELECT SUM(tTransactionDetail.QtyOfProduct) 
            FROM tTransactionDetail
            INNER JOIN tTransaction 
                ON tTransactionDetail.TransactionID = tTransaction.TransactionID 
            WHERE tTransaction.TransactionTypeID = 1
                AND tTransactionDetail.ProductID = ?
        """
        result = self._execute_query(query, [product_id])
        return result[0][0] if result and result[0][0] else 0
    
    def _execute_query(self, query: str, params=None) -> list:
        """Internal method for safe query execution"""
        try:
            with self.conn.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except pyodbc.Error as e:
            print(f"Query execution failed: {str(e)}")
            return []