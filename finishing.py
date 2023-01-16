import pandas as pd
def check_order(dict):
    trx_id = input("Transaction ID: ")
    if trx_id in dict.keys():
        list = dict[trx_id]
        total_price = 0
        for item in list:
            sub_total_price = float(item[1]) * float(item[2])
            item.append(sub_total_price)
            total_price += item[3]
        df = pd.DataFrame(list, columns=("Item", "Amount", "Price", "Sub Total"))
        df.index = [x for x in range(1, len(df.values)+1)]
        df.index.name = "No."
        disc = 0
        if total_price >500_000:
            disc = 0.1
        elif total_price > 300_000:
            disc = 0.08
        elif total_price > 200_000:
            disc = 0.05
        else:
            disc = 0
        disc_price = disc * total_price
        final_price = total_price - disc_price
        print("")
        print(df)
        print("=============================================")
        print("")
        print(f"Total Price: {total_price}\nDiscount Price: {disc_price}\nFinal Price: {final_price}") 
    else:
        print("Transaction ID not found. Please try again.")
