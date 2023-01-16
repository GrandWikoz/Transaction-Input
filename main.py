"""
This module acts as the main area to execute the program and includes four other modules necessary
"""

# Import all related modules
import transaction_input as trx
import update as upd
import delete as dlt
from finishing import check_order

# Execute trx to trigger data input from user. Data consists of transaction ID, item name, amount and price which will be stored in dictionary called `dict` to be manipulated later by other modules
dict = trx.trx_input()

# Check input data
print(dict)

# If user wishes to update their purchases then use this module. There are three updates available, namely name update, amount update and price update
upd.update_item_amount(dict)

upd.update_item_price(dict)

# Check updated data
print(dict)

# If user wishes to delete data, then there are two options available, namely reset_transaction to delete all items and delete_item to delete specific item
dlt.delete_item(dict)

# Check updated data
print(dict)

# Show purchase summary in a table using Pandas DataFrame and total_price along discount_price and, finally, final__price for customers to pay
check_order(dict)