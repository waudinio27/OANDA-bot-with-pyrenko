# OANDA-bot
Hey guys, this is my implementation of Renko Bars that are plotted with Live Data :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key to be used with the build_history function. 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization by using optimal_brick_sfo. The Renko Bars are built with the best average value from the historic values from the ATR 14 - Average True Range.  

The candles from the pricing stream are downloaded with a while loop and added to a pandas DataFrame above the while loop. They form the Renko Bars according to the actual Close price. 

After the data is added to the DataFrame I show how a working trading logic can be implemented. 
There is a function to create orders and the command to open Long or Short positions. 



Hope you enjoy!

Happy Trading :-)

=======

Needed packages:

Linux:
pip3 install -U setuptools
pip3 install numpy
pip3 install matplotlib
pip3 install TA-Lib
pip3 install --upgrade ta
pip3 install pandas_ta



more details on ta-lib: https://blog.quantinsti.com/install-ta-lib-python/#install-ta-lib-on-linux

Install TA-Lib with Windows:

https://blog.quantinsti.com/install-ta-lib-python/
