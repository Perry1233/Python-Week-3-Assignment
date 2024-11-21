# #Question 1.

# def calculate_discount(price, discount_percent):
#     """
#     Calculate the final price after applying a discount.

#     Parameters:
#     price (float): The original price of the item.
#     discount_percent (float): The discount percentage to be applied.

#     Returns:
#     float: The final price after applying the discount, or the original price if the discount is less than 20%.
#     """
#     if discount_percent >= 20:
#         final_price = price - (price * (discount_percent / 100))
#         return final_price
#     else:
#         return price

# # Example usage:
# original_price = 100.0
# discount = 25  # 25%
# print(calculate_discount(original_price, discount))  # Should print 75.0


#Question 2.

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.

    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Display the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"After applying the discount, the final price is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for the price and discount percentage.")
