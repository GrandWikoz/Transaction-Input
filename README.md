# Transaction-Input
A simple mechanism to record store transaction
# Background
A newly established store has no database regarding its item, type, amount or price. Therefore, this project is intended to help it set up a simple mechanism to record transaction.
# Requirement
1. Transaction ID
2. Item name
3. Item amount
4. Item price
# Flow
1. This project uses to four kinds of input (transaction ID, item name, amount and price) to record transaction
2. This project allows users to input multiple transaction IDs and items
3. User input will be processed to generate output in form of `dictionary` with `transaction ID` as key and `item name, amount and price` as values
4. Input from user will be stored in variabel `dict` which then could be manipulated, mainly through `update` module (explained below)

![Screenshot (1265)](https://user-images.githubusercontent.com/122712029/212676502-82437b1e-bb74-44f8-a8c2-7d4898767819.png)

# Functions/Attributes Explanation
This project made up of four different modules, namely:
1. transaction_input, used to start the project by inputing transaction ID, item name, amount and price
2. update, used to update item details (name, amount and/or price)
3. delete, used to delete transaction and/or item
4. finishing, used to show purchase summary and price to pay
# Demonstration

# Conclusion
