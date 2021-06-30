# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key. The historical prices are transformed to a list that can be iterated with the do_next function. The idea now is to use this in combination with a while loop. Like this the actual price stream from def get_candles can be used to form the renko prices and append them over time. Like this I want to build  a chart that updates with every cycle of the loop. 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization.

Any hints on how to improve the code and add the trading logic and the market orders for buy and sell are welcome!

In the near future, I will try to replace the ATR that is right now calculated with Ta-Lib with a hand coded version, for the ease of use. 

Hope you enjoy!

