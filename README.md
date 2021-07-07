# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key to be used with the build_history function. 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization by using optimal_brick_sfo. 

The candles from the pricing stream are downloaded and added to a pandas data frame inside of a while loop. They form the Renko Bars according to the actual data. It is missing a step to append the data from the pricing stream over time in a correct way to build a chart with all the data since the start with every new cycle. 

Any hints on how to improve the code and add the trading logic and the market orders for buy and sell are welcome!

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
