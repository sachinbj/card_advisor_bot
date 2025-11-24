def choose_card(category: str, amount: float, platform: str):
    # Grocery
    if category == "grocery":
        if platform == "offline":
            return "HSBC Live+ Credit Card", "10% cashback on groceries"
        if platform in ["flipkart", "bigbasket"]:
            return "HDFC Infinia (Primary)", "Voucher via SmartBuy (25 RP/150)"
        return "HSBC Live+ Credit Card", "General grocery cashback"

    # Dining
    if category == "dining":
        if platform in ["swiggy", "zomato"]:
            return "HDFC Swiggy Credit Card", "10% cashback on Swiggy/Zomato"
        return "HSBC Live+ Credit Card", "10% offline dining cashback"

    # Online Shopping
    if category == "online_shopping":
        if platform in ["amazon", "flipkart", "myntra"]:
            return "HDFC Infinia (Primary)", "Voucher via SmartBuy (25 RP/150)"
        return "HDFC Infinia (Primary)", "General online shopping"

    # Fuel
    if category == "fuel":
        return "HDFC Tata Neu Infinity", "Best fuel rewards among your cards"

    # Utilities
    if category == "utilities":
        return "HDFC Infinia (Primary)", "Amazon Pay vouchers via SmartBuy"

    # Bhima
    if category == "bhima":
        return "HDFC Infinia (Primary)", "High return using AP vouchers"

    # Jewellery
    if category == "jewellery":
        return "HSBC Live+", "Infinia/Emeralde give zero"

    # Others
    return "ICICI Emeralde Private Metal", "Helps progress 10L annual waiver"
