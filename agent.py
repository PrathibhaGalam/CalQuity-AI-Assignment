from autogen import AssistantAgent, UserProxyAgent
import yfinance as yf
import matplotlib.pyplot as plt

class StockTool:
    """A tool to fetch and visualize stock prices using yfinance."""
    
    @staticmethod
    def fetch_stock_data(ticker, start_date, end_date):
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)
        return data

    @staticmethod
    def plot_stock_data(data, ticker):
        plt.figure(figsize=(10, 5))
        plt.plot(data.index, data['Close'], label='Closing Price', color='blue')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'{ticker} Stock Price')
        plt.legend()
        plt.show()

# Define the assistant agent
assistant = AssistantAgent(name="StockAssistant")

# Define the user agent with access to the stock tool
class StockUserAgent(UserProxyAgent):
    def __init__(self, name, stock_tool):
        # Disable Docker execution here
        super().__init__(name, code_execution_config={"use_docker": False})
        self.stock_tool = stock_tool

    def get_stock_info(self, ticker, start_date, end_date):
        print(f"Fetching stock data for {ticker} from {start_date} to {end_date}...")
        data = self.stock_tool.fetch_stock_data(ticker, start_date, end_date)
        self.stock_tool.plot_stock_data(data, ticker)

# Instantiate the user agent
stock_tool = StockTool()
user_agent = StockUserAgent(name="StockUser", stock_tool=stock_tool)

# Simulate agent interaction
user_agent.get_stock_info("AAPL", "2024-01-01", "2024-02-01")
