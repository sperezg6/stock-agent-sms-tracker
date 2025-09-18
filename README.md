# STOCK-AGENT-SMS-TRACKER

*Transforming Stock Insights into Action Instantly*

![last commit](https://img.shields.io/github/last-commit/sperezg6/stock-agent-sms-tracker?style=flat-square&color=blue)
![languages](https://img.shields.io/github/languages/count/sperezg6/stock-agent-sms-tracker?style=flat-square&color=green)
![top language](https://img.shields.io/github/languages/top/sperezg6/stock-agent-sms-tracker?style=flat-square&color=orange)

**Built with the tools and technologies:**

![TypeScript](https://img.shields.io/badge/-TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Twilio](https://img.shields.io/badge/-Twilio-F22F46?style=flat-square&logo=twilio&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white)

---

## Table of Contents

• [Overview](#overview)  
• [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
• [Installation](#installation)  
• [Configuration](#configuration)  
• [Usage](#usage)  
• [Architecture](#architecture)  
• [Features](#features)  
• [Testing](#testing)  
• [Contributing](#contributing)  
• [License](#license)

---

## Overview

Stock-agent-sms-tracker is an intelligent serverless solution that automates stock monitoring, research, and SMS notifications using AWS infrastructure. It leverages AI agents to analyze market data, research recent news, and deliver actionable insights directly to your mobile device.

### Why stock-agent-sms-tracker?

This project simplifies the complex process of stock market monitoring through a modern, serverless architecture. The core features include:

🤖 **AI-Powered Research**: Utilizes OpenAI agents for intelligent stock analysis and market research  
📱 **SMS Notifications**: Real-time alerts delivered via Twilio integration  
☁️ **Serverless Architecture**: Built on AWS Lambda with automated scaling and cost efficiency  
🔄 **Automated Scheduling**: Configurable execution via EventBridge (default: weekdays at 8 AM)  
📈 **Multi-Stock Tracking**: Monitor multiple stocks with customizable watchlists  
🔍 **News Integration**: Web search capabilities for latest market news and analysis

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed and configured:

**Required Software:**
- [Node.js](https://nodejs.org/) (v18 or later)
- [Python](https://python.org/) (v3.11 or later)
- [AWS CLI](https://aws.amazon.com/cli/) configured with your credentials
- [AWS CDK](https://docs.aws.amazon.com/cdk/) (v2.214.0 or later)

**Required API Keys:**
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [Finnhub API Key](https://finnhub.io/dashboard) (for stock data)
- [Twilio Account](https://console.twilio.com/) (Account SID, Auth Token, Phone Numbers)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/stock-agent-sms-tracker.git
   cd stock-agent-sms-tracker
   ```

2. **Install dependencies:**
   ```bash
   npm install
   pip install -r lambda/requirements.txt
   ```

3. **Bootstrap AWS CDK (if not already done):**
   ```bash
   cdk bootstrap aws://YOUR-ACCOUNT-ID/us-east-1
   ```

---

## Configuration

### Environment Variables

Create the following secrets in your deployment environment:

**For Local Development (.env file):**
```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TO_PHONE_NUMBER=+1234567890
FROM_PHONE_NUMBER=+1098765432
FINNHUB_API_KEY=your_finnhub_api_key
OPENAI_API_KEY=your_openai_api_key
```

**For GitHub Actions (Repository Secrets):**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TO_PHONE_NUMBER`
- `FROM_PHONE_NUMBER`
- `FINNHUB_API_KEY`
- `OPENAI_API_KEY`

### Stock Watchlist Configuration

Edit `lambda/lib/stocks_lists.json` to customize your tracked stocks:

```json
[
  "AAPL",
  "GOOGL",
  "MSFT",
  "TSLA",
  "VOO"
]
```

---

## Usage

### Local Development & Testing

1. **Test the agent locally:**
   ```bash
   cd lambda
   python -m pytest tests/
   ```

2. **Run the Jupyter notebook for interactive testing:**
   ```bash
   jupyter notebook lambda/tests/agents.ipynb
   ```

### Deployment

**Deploy using AWS CDK:**
```bash
cdk deploy --context twilioAccountSid="YOUR_SID" \
           --context twilioAuthToken="YOUR_TOKEN" \
           --context toPhoneNumber="+1234567890" \
           --context fromPhoneNumber="+1098765432" \
           --context finnhubApiKey="YOUR_FINNHUB_KEY" \
           --context openaiApiKey="YOUR_OPENAI_KEY"
```

**Deploy using GitHub Actions:**
Push to the `main` branch to trigger automatic deployment via GitHub Actions.

### Manual Lambda Invocation

```bash
aws lambda invoke \
  --function-name stock-agent-tracks-lambda \
  response.json
```

---

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   EventBridge   │───▶│   AWS Lambda     │───▶│   Twilio SMS    │
│   (Scheduler)   │    │   (Python 3.11) │    │   (Notifications)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │   External APIs  │
                       │  • OpenAI GPT-4  │
                       │  • Finnhub       │
                       │  • Web Search    │
                       └──────────────────┘
```

**Key Components:**
- **AWS Lambda**: Serverless compute running the Python agent
- **EventBridge**: Scheduled execution (weekdays at 8 AM EST)
- **Lambda Layer**: Dependencies bundled for faster cold starts
- **IAM Roles**: Secure permissions for AWS resource access

---

## Features

### 🎯 **Intelligent Stock Analysis**
- Real-time price fetching via Finnhub API
- AI-powered market research using OpenAI agents
- Automated news sentiment analysis
- Price movement explanations and context

### 📱 **Smart Notifications**
- Personalized SMS reports for each tracked stock
- Formatted messages with price data and analysis
- Customizable message templates
- Error handling and delivery confirmation

### ⚙️ **Automated Operations**
- Serverless execution with zero maintenance
- Configurable scheduling via EventBridge
- Automatic dependency management
- Built-in error handling and logging

### 🔧 **Developer Experience**
- Infrastructure as Code with AWS CDK
- TypeScript for type-safe infrastructure
- Python for AI agent implementation
- Comprehensive testing suite
- CI/CD pipeline with GitHub Actions

---

## Testing

**Run unit tests:**
```bash
npm test
```

**Test Lambda function locally:**
```bash
cd lambda
python main.py
```

**Interactive testing with Jupyter:**
```bash
jupyter notebook lambda/tests/agents.ipynb
```

---

## Example Output

The system generates SMS messages like:

```
Hello Santiago 👋,

Tesla Inc. (TSLA) surged 7.36% to $395.94. The sharp rise is linked to a record compensation proposal for CEO Elon Musk and optimism on Tesla's AI/robotics future. The board's support boosts investor sentiment.

Best regards,
Your Stock Tracker Bot 🤖
```

---

## Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support

If you found this project helpful, please give it a ⭐️ on GitHub!

For questions or support, please open an issue or contact [your-email@example.com](mailto:your-email@example.com).