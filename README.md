# Matched-Fine
A user-friendly system to cluster markets movements, and to calculate the expected value of individual stocks.

## To install locally and run
```bash
git clone https://github.com/ColeDnought/Matched-Fine.git
cd Matched-Fine
pip install -r requirements.txt
```

## To edit

1. The main.py file uses most of the code
2. After editing, run the following command to check for errors
```bash
python main.py
```

## To push changes to github
```bash
git add .
git commit -m "Your message here"
git push
```

## To do
- [ ] Create the underlying python program
- [ ] Create the web app

## Method 
We will use the data from Yahoo Finance to create a database of stock prices. Then, when given a stock ticker and a date range, we will calculate the expected value of the stock based on the movements of other stocks with the most similar movement.
