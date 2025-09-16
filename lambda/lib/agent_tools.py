import finnhub
import os
from pydantic import BaseModel
from typing import Optional
import time
import json
from agents import function_tool
from twilio.rest import Client


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
to_phone_number = os.environ.get("TO_PHONE_NUMBER")
from_phone_number = os.environ.get("FROM_PHONE_NUMBER")
finnhub_api_key = os.environ.get("FINNHUB_API_KEY")
client = Client(account_sid, auth_token)


class StockPriceResponse(BaseModel):
    current_price: float
    previous_close: float
    change: Optional[float] = None
    change_percent: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None

def get_stock_price(symbol: str) -> StockPriceResponse:
    """
    Get stock price using Finnhub API
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    
    Returns:
        StockPriceResponse with current and previous close prices
    
    Raises:
        Exception: If API call fails or returns invalid data
    """
    # Initialize Finnhub client with API key from .env
    api_key = os.getenv('FINNHUB_API_KEY')
    if not api_key:
        raise ValueError("FINNHUB_API_KEY not found in .env file")

    finnhub_client = finnhub.Client(api_key=api_key)
    
    try:
        # Get quote data for the symbol
        quote = finnhub_client.quote(symbol.upper())
        
        # Check if we got valid data
        if not quote or quote.get('c') is None:
            raise ValueError(f"No data available for symbol: {symbol}")
        
        # Extract the data
        current_price = quote['c']  # Current price
        previous_close = quote['pc']  # Previous close
        
        # Create response with additional data if available
        return StockPriceResponse(
            current_price=current_price,
            previous_close=previous_close,
            change=quote.get('d'),  # Change ($)
            change_percent=quote.get('dp'),  # Change (%)
            high=quote.get('h'),  # Day high
            low=quote.get('l'),  # Day low
            open=quote.get('o')  # Day open
        )
        
    except Exception as e:
        raise Exception(f"Failed to fetch stock price for {symbol}: {str(e)}")



def get_tracker_list():
    with open("lib/stocks_lists.json", "r") as f:
        tracker_list = json.load(f)

    return tracker_list



def send_sms( body: str) -> str:
    """
    Send SMS using Twilio API
    
    Args:
        to: Recipient phone number (in E.164 format, e.g., '+1234567890')
        body: Message body
        from_: Sender phone number (Twilio number)
    
    Returns:
        Message SID if sent successfully
    
    Raises:
        Exception: If sending fails
    """
    try:
        message = client.messages.create(
            body=body,
            from_=from_phone_number,
            to=to_phone_number
        )
        return message.sid
    except Exception as e:
        raise Exception(f"Failed to send SMS to {to_phone_number}: {str(e)}")




@function_tool
async def fetch_stock_price(ticker: str) -> str:
    """
    Fetch the current stock price for a given ticker symbol.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    Returns:
        A formatted string with the stock price information.
    """
    stock_price = get_stock_price(ticker)
    if stock_price:
        return stock_price
    return f"Failed to fetch stock price for {ticker}."


@function_tool
async def get_tracker_list_tool() -> str:
    """
    Fetch the current stock price for a given ticker symbol.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
    Returns:
        A formatted string with the stock price information.
    """
    tracker_list = get_tracker_list()
    if tracker_list:
        return tracker_list
    return f"Failed to fetch tracker list."


@function_tool
async def send_stock_sms(body: str) -> str:
    """
    Send an SMS with stock price information.
    
    Args:
        ticker: Stock ticker symbol (e.g., 'AAPL', 'GOOGL')
        price: Current stock price
        change: Price change
        change_percent: Percentage change
    
    Returns:
        Message SID if sent successfully.
    """

    message_sid = send_sms(body)
    return message_sid