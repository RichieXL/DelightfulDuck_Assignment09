# Name:Josh Slocomb, Richie James
# email:slocumjt@mail.uc.edu, james2c4@mail.uc.edu, 
# Assignment Number: Assignment 09
# Due Date:04/03/2025
# Course/Section:IS4010 001
# Semester/Year:Spring 2025
# Brief Description of the assignment: pulls data from database, implement a SQL statment and then implements a summarized comment
# Brief Description of what this module does: initalizes all code from packages and implements final answer/statment
# Citations: N/A
# Anything else that's relevant: N/A

#main.py 



from db_package.db_handler import DatabaseHandler
from data_package.data_processor import ProductReportBuilder

def main():
    # Initialize database connection (Assignment Setup)
    """
    Main program execution file
    @param
    Combines database operations and data processing to fulfill assignment requirements
    """
    db = DatabaseHandler()
    if not db.connect():
        return
    
    try:
        # Assignment Step 1: Get all products
        products = db.get_products()
        if not products:
            print("No products found in database")
            return
        
        # Assignment Step 2: Select random product
        selected = ProductReportBuilder.select_random_product(products)
        product_id, _, description, manufacturer_id, brand_id = selected
        
        # Assignment Steps 3-4: Get manufacturer
        manufacturer = db.get_manufacturer(manufacturer_id)
        
        # Assignment Step 5: Get brand
        brand = db.get_brand(brand_id)
        
        # Assignment Step 6: Get sales data
        sales = db.get_sales_data(product_id)
        
        # Assignment Step 7: Generate and print output
        report = ProductReportBuilder.build_report_string(
            description, manufacturer, brand, sales
        )
        print(report)
        
    finally:
        db.conn.close()

if __name__ == "__main__":
    main()

