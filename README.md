# News to Tweets

Welcome to the "News to Tweets" repository! This project aims to convert news articles into concise, tweet-sized summaries automatically. By doing so, it saves users time by eliminating the need to manually compile news and craft tweets. "News to Tweets" is designed to keep you updated with minimal effort.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
- [Usage](#usage)



## Getting Started

Follow these instructions to set up "News to Tweets" on your local machine.

### Prerequisites

Ensure you have the following installed before proceeding:
- Python 3.6 or later
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KiranM27/news-to-tweets.git
```

2. Navigate to the project directory:
```bash
cd news-to-tweets
```

3. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### Environment Setup
To configure the application settings, you need to set up the .env file based on the provided .env.template.
Copy the .env.template file and rename it to .env:
```bash
cp .env.template .env
```

Open the .env file in your favorite text editor.
Fill in the required settings, such as API keys and other configurations, as per the instructions in the template.


## Usage

After setting up the project, you can start converting news into tweets by running the main script:

```bash
python app.py
```

Follow the prompts in the terminal to generate the tweets and post them to your Twitter account.