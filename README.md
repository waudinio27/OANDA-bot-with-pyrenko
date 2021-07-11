# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key to be used with the build_history function. 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization by using optimal_brick_sfo. This is why there is no need for additional indicators to confirm the signal. As the Renko Bars are built with the best average value from the historic values from the ATR 14 - Average True Range.  

The candles from the pricing stream are downloaded with a while Loop and added to a pandas data frame above the while loop. They should form the Renko Bars according to the actual data. I could not confirm if this is working so far. As the candle that gets downloaded in the stream is the last candle from friday night before the market got closed and just repeats itself.

After the data is added to the DataFrame it is possible to see the implementation of the first part of the trading logic.
There is a function to create orders and the command to open a Long or Short position. What is missing is that the code is checking for open positions at the account and only opens one position at a time. Also the positions need to be closed when direction is changing - this will be the next thing to do before trials with the demo account. 

Any hints on how to improve the code are welcome!

In the near future, I will try to replace the ATR that is right now calculated with Ta-Lib with a hand coded version, for the ease of use and installation. 


Hope you enjoy!

=======
Any hints on how to improve the code are welcome!

Needed packages:

Linux:
pip3 install -U setuptools
pip3 install numpy
pip3 install matplotlib
pip3 install TA-Lib
pip3 install --upgrade ta
pip3 install pandas_ta

For fetching data from Yahoo finance
pip3 install yfinance


more details on ta-lib: https://blog.quantinsti.com/install-ta-lib-python/#install-ta-lib-on-linux
