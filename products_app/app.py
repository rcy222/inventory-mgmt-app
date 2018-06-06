import csv
import os
import pdb

def menu(username="@prof-rossetti", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset CSV file to default
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

#Reading from csv file (default file to product.csv)
def read_products_from_file(filename="products.csv"):
    #           concatenate current python directory      filename
    #          ____________ _________________________  ______________
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #product_count = 0
    #dir_name = os.path.dirname(__file__)
    #print(dir_name)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    #TODO: open the file and populate the products list with product dictionaries
    products = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            products.append(dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)

    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department","price"])
        writer.writeheader() # uses fieldnames set above
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)

#credit @s2t2
def price_check(price):
    try:
        float(price)
        return True
    except Exception as e: # e can be the error message and you can print e
        return False

#def aisle_check(product_aisle):
#    product_aisle = [p for p in products if p["aisle"]==product_aisle]
#    for
#    if
#        return False
#    except Exception as e: # e can be the error message and you can print e
#        return True

#def product_match(product)

def run():
    # First, read products from file...
    products = read_products_from_file()
    #print(len(products))
    #user = input("Please enter user name ")
    # Then, prompt the user to select an operation...
    # credit @s2t2, Question: Why do I need to call out my_menu and input(menu(username="@rcy222", products_count=len(products)))


    operation = input(menu(username="@rcy222", products_count=len(products)))

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #TODO: handle selected operation
    line = "----------------------------------------------------------------------------"
    if operation != "List" and operation != "list" and operation != "Show" and operation != "show" and operation != "Create" and operation != "create" and operation != "Update" and operation != "update" and operation != "Destroy" and operation != "destroy" and operation != "Reset" and operation != "reset":
        quit("Wrong operation.  Try again")
    elif operation == "List" or operation == "list":
        List_statement = "LISTING "+ str(len(products)) + " PRODUCT(S):"
        print(line)
        print(List_statement.center(len(line),' '))
        print(line)
        for p in products:
            print(" #" + str(p["id"] + ": " + p["name"]))

    elif operation == "Show" or operation == "show":
        Show_statement = "SHOWING A PRODUCT:"
        #print("Show operation")
        print(line)
        print(Show_statement.center(len(line),' '))
        print(line)
        show_id = input("Please specify the product's identifier: ")  #Str input, not int input
        show_product = [p for p in products if p["id"]==show_id]      #Str match, not int match
        while not show_product:                                       #While loop until a product id match
            print("Item not found, please try again")
            show_id = input("Please specify the product's identifier: ")
            show_product = [p for p in products if p["id"]==show_id]  # assume no duplicate id, and it will be assigned automatically in create function
        print(show_product)

    elif operation == "Create" or operation == "create":
            all_ids = [int(p["id"]) for p in products]          #find the max product id
            p_max = max(all_ids)
            p_id = p_max + 1
            new_p = {}                  #create new dictionary
            new_p["id"] = p_id
            new_p["name"] = input("Please enter the new product name ")
            new_p["aisle"] =input("Please enter the new product aisle ")
            all_aisles = [p["aisle"] for p in products]
            while new_p["aisle"] not in all_aisles:
                print(all_aisles)
                new_p["aisle"] = input("Wrong Aisle, try again with an aisle in the list above ")


            #print(aisle_check)
            #while not aisle_check:
            #    for p in products: print(p["aisle"])
            #    input("Wrong Aisle, try again with an aisle in the list above ")
            #    aisle_check = [p for p in products if p["aisle"]==new_p["aisle"]]
            new_p["department"] =input("Please enter the new product department ")
            all_departments = [p["department"] for p in products]
            while new_p["department"] not in all_departments:
                print(all_departments)
                new_p["department"] = input("Wrong department, try again with an department in the list above ")
            new_p["price"] =input("Please enter the new product price ")
            while price_check(new_p["price"])==False:
                new_p["price"] =input("Not a valid price input. Try again using format like 3.99 ")
            products.append(new_p)
            create_statement = "CREATING NEW PRODUCT"
            print(line)
            print(create_statement.center(len(line),' '))
            print(line)
            print(new_p)

    elif operation == "Update" or operation == "update":
        #check for valid input
        update_id = input("Please input product identifier you want to update: ")
        update_p = [p for p in products if p["id"]==update_id]  # assume no duplicate id, and it will be assigned automatically in create function
        while not update_p:                                       #While loop until a product id match
            print("Item not found, please try again")
            update_id = input("Please specify the product's identifier you want to update: ")
            update_p = [p for p in products if p["id"]==update_id]  # assume no duplicate id, and it will be assigned automatically in create function

        #once valid input is created, count ID match and update the list
        count_pid = 0
        for product in products:
            count_pid = count_pid + 1                   #loop through all products in the for loop
            if product["id"] == update_id:
                matching_product = product
                selected_id = count_pid - 1              #fixed result, the -1 is to account for the starting point of 0
        update_name = input("Please input new product name you want to update, currently '" + matching_product['name'] + "': ")
        update_aisle = input("Please input new product aisle you want to update, currently '" + matching_product['aisle'] + "': ")
        update_dept = input("Please input new product department you want to update, currently '" + matching_product['department'] + "'' ")
        update_price = input("Please input new product price you want to update, currently '" + matching_product['price'] + "' ")
        while price_check(update_price) == False:
            update_price =input("Not a valid price input. Try again using format like 3.99 ")
        products[selected_id] = {'id': update_id, 'name': update_name, 'aisle': update_aisle, 'department': update_dept, 'price':update_price}
        update_statement = "UPDATED A PRODUCT"
        print(line)
        print(update_statement.center(len(line),' '))
        print(line)
        print(products[selected_id])

    elif operation == "Destroy" or operation == "destroy":
        #check for valid input
        destroy_id = input("Please input product identifier you want to destroy: ")
        destroy_p = [p for p in products if p["id"]==destroy_id]  # assume no duplicate id, and it will be assigned automatically in create function
        while not destroy_p:                                       #While loop until a product id match
            print("Item not found, please try again")
            destroy_id = input("Please specify the product's identifier you want to destroy: ")
            destroy_p = [p for p in products if p["id"]==destroy_id]  # assume no duplicate id, and it will be assigned automatically in create function
        #once valid input is created, begin destruction
        destroy_pid = 0
        for product in products:
            destroy_pid = destroy_pid + 1                   #loop through all products in the for loop
            if product["id"] == destroy_id:
                matching_product = product
                selected_id = destroy_pid - 1              #fixed result, the -1 is to account for the starting point of 0
        destroy_statement = "DESTRUCTION COMMENCING"
        print(line)
        print(destroy_statement.center(len(line),' '))
        print(line)
        print(products[selected_id])
        del products[selected_id]

    elif operation == "Reset" or operation == "reset":
        reset_products_file()

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(filename="products.csv",products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions, preventing reset.py from running
if __name__ == "__main__":
    run()
