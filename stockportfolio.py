import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=["Symbol", "Shares", "Purchase Price", "Current Price"])
    
    def add_stock(self, symbol, shares, purchase_price):
        """Add a stock to the portfolio."""
        if symbol in self.portfolio['Symbol'].values:
            print(f"{symbol} already exists in the portfolio.")
        else:
            current_price = self.get_current_price(symbol)
            new_row = pd.DataFrame({
                'Symbol': [symbol],
                'Shares': [shares],
                'Purchase Price': [purchase_price],
                'Current Price': [current_price]
            })
            self.portfolio = pd.concat([self.portfolio, new_row], ignore_index=True)
    
    def remove_stock(self, symbol):
        """Remove a stock from the portfolio."""
        self.portfolio = self.portfolio[self.portfolio['Symbol'] != symbol]
    
    def get_current_price(self, symbol):
        """Fetch the current price of a stock."""
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")["Close"].iloc[-1]
        return current_price
    
    def update_prices(self):
        """Update current prices of all stocks in the portfolio."""
        for index, row in self.portfolio.iterrows():
            current_price = self.get_current_price(row["Symbol"])
            self.portfolio.at[index, "Current Price"] = current_price
    
    def portfolio_summary(self):
        """Show the performance of the portfolio."""
        self.update_prices()
        self.portfolio['Market Value'] = self.portfolio['Shares'] * self.portfolio['Current Price']
        self.portfolio['Profit/Loss'] = (self.portfolio['Current Price'] - self.portfolio['Purchase Price']) * self.portfolio['Shares']
        
        total_investment = sum(self.portfolio['Shares'] * self.portfolio['Purchase Price'])
        total_value = sum(self.portfolio['Market Value'])
        total_profit_loss = sum(self.portfolio['Profit/Loss'])
        
        print("\nPortfolio Summary:")
        print(self.portfolio[['Symbol', 'Shares', 'Purchase Price', 'Current Price', 'Profit/Loss']])
        print(f"\nTotal Investment: ${total_investment:.2f}")
        print(f"Total Market Value: ${total_value:.2f}")
        print(f"Total Profit/Loss: ${total_profit_loss:.2f}")
    
    def plot_performance(self):
        """Plot the portfolio performance over time."""
        portfolio_value = []
        for symbol in self.portfolio['Symbol']:
            stock = yf.Ticker(symbol)
            historical_data = stock.history(period="1y")
            portfolio_value.append(historical_data['Close'].iloc[-1])
        
        plt.bar(self.portfolio['Symbol'], portfolio_value)
        plt.xlabel('Stocks')
        plt.ylabel('Current Price')
        plt.title('Stock Portfolio Performance')
        plt.show()

# Example usage
portfolio = StockPortfolio()

# Add some stocks
portfolio.add_stock('AAPL', 10, 150)  # Apple stock with 10 shares at $150
portfolio.add_stock('TSLA', 5, 800)   # Tesla stock with 5 shares at $800

# Print portfolio summary
portfolio.portfolio_summary()

# Plot performance
portfolio.plot_performance()
