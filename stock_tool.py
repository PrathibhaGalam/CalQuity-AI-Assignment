import yfinance as yf
import matplotlib.pyplot as plt

class StockTool:
    """A tool to fetch and visualize stock prices using yfinance."""

    @staticmethod
    def fetch_stock_data(ticker, start_date, end_date):
        """Fetch stock data for a given ticker and date range."""
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        return data

    @staticmethod
    def plot_stock_data(data, ticker):
        """Visualize stock closing prices."""
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'{ticker} Stock Price')
        plt.legend()
        plt.show()
