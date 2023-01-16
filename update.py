"""
Updating item with value fed from transaction_input module
"""

def update_item_name(dict):
    """
    Input:
    1. Transaction ID to decide which to transaction to update
    2. Item name to update
    3. Updated name
    Output: item with updated name
    Process:
    1. Uses branching to check if given transaction ID exists in the dictionary
    2. Also branching to check if users want to continue updating item name
    """
    trx_id = input("Transaction ID: ")
    if trx_id in dict.keys():
        while True:
            item_name = input("Item to be updated: ")
            check = 0
            for purchase_list in dict[trx_id]:
                if item_name in purchase_list:
                    updated_item_name = input("Update name: ")
                    dict[trx_id][dict[trx_id].index(purchase_list)][0] = updated_item_name
                    check += 1
                else:
                    pass
            if check == 0:
                print("Item not found. Please try again.")
            else:
                pass
            next_update = input("Continue update (Y for Yes, any others for No): ")
            if next_update.lower() != "y":
                break
            else:
                pass
        return(dict[trx_id])

    else:
        print("Transaction ID not found. Please try again.")

def update_item_amount(dict):
    """
    Input:
    1. Transaction ID to decide which to transaction to update
    2. Item name to update
    3. Updated amount
    Output: item with updated amount
    Process:
    1. Uses branching to check if given transaction ID exists in the dictionary
    2. Also branching to check if users want to continue updating item amount
    3. Try/excep to avoid error from unfit input such as non-numerical amount
    """
    trx_id = input("Transaction ID: ")
    if trx_id in dict.keys():
        while True:
            item_name = input("Item to be updated: ")
            check = 0
            for purchase_list in dict[trx_id]:
                if item_name in purchase_list:
                    updated_item_amount = input("Update amount: ")
                    try:
                        if float(updated_item_amount) <= 0:
                            print("Amount must be greater than 0")
                        float(updated_item_amount)
                    except ValueError:
                        print("Amount must be numerical")
                    dict[trx_id][dict[trx_id].index(purchase_list)][1] = updated_item_amount
                    check += 1
                else:
                    pass
            if check == 0:
                print("Item not found. Please try again.")
            else:
                pass
            next_update = input("Continue update (Y for Yes, any others for No): ")
            if next_update.lower() != "y":
                break
            else:
                pass
        return(dict[trx_id])
    else:
        print("Transaction ID not found. Please try again.")

def update_item_price(dict):
    """
    Input:
    1. Transaction ID to decide which to transaction to update
    2. Item name to update
    3. Updated price
    Output: item with updated amount
    Process:
    1. Uses branching to check if given transaction ID exists in the dictionary
    2. Also branching to check if users want to continue updating item price
    3. Try/excep to avoid error from unfit input such as non-numerical price
    """
    trx_id = input("Transaction ID: ")
    if trx_id in dict.keys():
        while True:
            item_name = input("Item to be updated: ")
            check = 0
            for purchase_list in dict[trx_id]:
                if item_name in purchase_list:
                    updated_item_price = input("Update price: ")
                    try:
                        if float(updated_item_price) <= 0:
                            print("Price must be greater than 0")
                        float(updated_item_price)
                    except ValueError:
                        print("Price must be numerical")
                    dict[trx_id][dict[trx_id].index(purchase_list)][2] = updated_item_price
                    check += 1
                else:
                    pass
            if check == 0:
                print("Item not found. Please try again.")
            else:
                pass
            next_update = input("Continue update (Y for Yes, any others for No): ")
            if next_update.lower() != "y":
                break
            else:
                pass
        return(dict[trx_id])
    else:
        print("Transaction ID not found. Please try again.")
