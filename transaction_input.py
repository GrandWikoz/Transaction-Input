
class Transaction:
    """
    This class defines mechanisem to ask user for transaction ID. Later this ID will be used to mark all purchases with one unique ID.
    """
    
    pass

    def input():
        id = input("Transaction ID: ")
        return id

def trx_input():
    """
    Input: transaction ID, item name, item amount and item price.
    Output: creating a dictionary with transaction ID as key and list of purchases as value. Therefore, value is modeled as a nested list with [purchase] consisting individual item details (name, amount and price) and [purchase_list] consisting of all the purchases.
    Process:
    1. This module permits multiple transactions done at one go, which means the output will consist of different transaction IDs.
    2. It also uses branching to ask user whether want to input another transaction and/or another item
    3. It uses try/except to avoid error from unfit inputs, such as non-numerical amount or negative price.
    """
    
    trx_list = {}
    
    while True:
        trx_id = Transaction.input()
        
        purchase_list = []
        
        while True:
            purchase_item = input("Item: ")
            if purchase_item.lower() == "done":
                break
            
            purchase_amount = input("Amount: ")
            try:
                if purchase_amount.lower() == "done":
                    break
                if float(purchase_amount) <= 0:
                    print("Amount must be greater than 0")
                    break
                float(purchase_amount)
            except ValueError:
                print("Amount must be numerical")
                break

            purchase_price = input("Price: ")
            try:
                if purchase_price.lower() == "done":
                    break
                if float(purchase_price)  <= 0:
                    print("Price must be greater than 0")
                    break
                float(purchase_price)
            except ValueError:
                print("Price must be numerical")
                break

            purchase = [purchase_item, float(purchase_amount), float(purchase_price)]
            purchase_list.append(purchase)
    
        trx_per_id = {trx_id:purchase_list}
        trx_list[trx_id] = purchase_list
        
        next_trx = input("Next transaction (Y for Yes, any others for No): ")
        if next_trx.lower() != "y":
            break
        else:
            pass

    return(trx_list)
