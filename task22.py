import os

def get_portfolio_input(available_stocks):
    """
    Gets stock names and quantities from the user.
    Returns a dictionary of user's portfolio: {stock_name: quantity}.
    """
    portfolio = {}
    print("\nEnter your stock holdings. Type 'done' when finished.")
    
    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL, TSLA) or 'done': ").upper()
        if stock_name == 'DONE':
            break
        
        if stock_name not in available_stocks:
            print(f"Error: '{stock_name}' is not a recognized stock symbol. Please choose from: {', '.join(available_stocks.keys())}")
            continue
            
        while True:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                else:
                    portfolio[stock_name] = quantity
                    break # Exit quantity loop
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
    return portfolio

def calculate_investment(portfolio, stock_prices):
    """
    Calculates the total investment for the given portfolio.
    Returns a tuple: (detailed_investments, total_investment_value).
    detailed_investments is a list of tuples: (stock, quantity, price, value).
    """
    detailed_investments = []
    total_investment_value = 0.0
    
    for stock, quantity in portfolio.items():
        price = stock_prices.get(stock, 0.0) # Get price, default to 0 if not found (shouldn't happen with validation)
        value = quantity * price
        detailed_investments.append((stock, quantity, price, value))
        total_investment_value += value
        
    return detailed_investments, total_investment_value

def display_results(detailed_investments, total_investment_value):
    """
    Displays the stock portfolio and total investment.
    """
    print("\n--- Your Stock Portfolio ---")
    print(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Value':<10}")
    print("-" * 40)
    for stock, quantity, price, value in detailed_investments:
        print(f"{stock:<10} {quantity:<10} ${price:<9.2f} ${value:<9.2f}")
    print("-" * 40)
    print(f"{'Total Investment:':<30} ${total_investment_value:<9.2f}")
    print("-" * 40)

def save_results(detailed_investments, total_investment_value, filename="stock_portfolio.txt"):
    """
    Saves the portfolio results to a text file.
    """
    try:
        with open(filename, 'w') as f:
            f.write("--- Stock Portfolio Report ---\n")
            f.write(f"Generated on: {os.path.basename(__file__)}\n\n") # Basic timestamp
            f.write(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Value':<10}\n")
            f.write("-" * 40 + "\n")
            for stock, quantity, price, value in detailed_investments:
                f.write(f"{stock:<10} {quantity:<10} ${price:<9.2f} ${value:<9.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"{'Total Investment:':<30} ${total_investment_value:<9.2f}\n")
            f.write("-" * 40 + "\n")
        print(f"\nPortfolio saved successfully to '{filename}'")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    """
    Main function to run the Stock Portfolio Tracker.
    """
    # Hardcoded dictionary for stock prices
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.50,
        "GOOG": 150.75,
        "MSFT": 400.20,
        "AMZN": 190.10,
        "NVDA": 1000.00,
        "META": 490.00
    }
    
    print("--- Welcome to the Stock Portfolio Tracker! ---")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price:.2f}")

    user_portfolio = get_portfolio_input(stock_prices)

    if not user_portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    detailed_investments, total_investment = calculate_investment(user_portfolio, stock_prices)
    
    display_results(detailed_investments, total_investment)
    
    save_option = input("Do you want to save these results to a text file? (yes/no): ").lower()
    if save_option == 'yes':
        save_results(detailed_investments, total_investment)
    else:
        print("Results not saved.")

if __name__ == "__main__":
    main()