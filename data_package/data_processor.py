# Name:Josh Slocomb, Richie James
# email:slocumjt@mail.uc.edu, james2c4@mail.uc.edu, 
# Assignment Number: Assignment 09
# Due Date:04/03/2025
# Course/Section:IS4010 001
# Semester/Year:Spring 2025
# Brief Description of the assignment: pulls data from database, implement a SQL statment and then implements a summarized comment
# Brief Description of what this module does: implements the correct components to answer questions for assignment
# Citations: N/A
# Anything else that's relevant: N/A

#data_processor.py 

import random

class ProductReportBuilder:
    """
    Builds product reports from database data
    @param
    Data processing and output generation components
    @param
    Handles business logic for assignment requirements
    @return
    implements random product selection
    then generates a final output sentance from SQL statement
    """
    
    def select_random_product(products: list) -> tuple:
        if not products:
            raise ValueError("Empty product list provided")
        return random.choice(products)
    
    def build_report_string(description: str, manufacturer: str, brand: str, sales: int) -> str:
        base = f"The {description.strip()} manufactured by {manufacturer.strip()}"
        brand_info = f" ({brand.strip()} brand)" if brand else ""
        
        if sales > 0:
            items = "item" if sales == 1 else "items"
            return f"{base}{brand_info} has sold {sales} {items}."
        return f"{base}{brand_info} has not sold any items."
