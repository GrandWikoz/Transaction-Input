
def reset_transaction(dict):
    """
    Input: transaction ID user wishes to be deleted
    Output: deleted transaction
    """
    trx_id = input("Transaction ID: ")
    del dict[trx_id]
    print("Transaction deleted.")

def delete_item(dict):
    """
    Input:
    1. Transaction ID user wishes to be deleted
    2. Item name user wishes to be deleted
    Output: deleted item
    """
    trx_id = input("Transaction ID: ")
    item_name = input("Item Name: ")
    cek_index = 0
    for i in dict[trx_id]:
        if item_name in i:
            cek_index = i
    item_index = dict[trx_id].index(cek_index)
    del dict[trx_id][item_index]
    print(f"Item [{item_name}] deleted")