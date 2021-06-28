# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key. Right now the prices from the Live Stream are being downloaded, but they don´t form the Renko Chart or Pattern like they should and plot a graphic. The values from the stream should get appended to the pandas dataframe but right now it is only returning NAN values. Also in the orignal work the date does not get added to the renko prices ... 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization.

Any hints on how to improve the code and add the trading logic and the market orders for buy and sell are welcome!

In the near future, I will try to replace the ATR that is right now calculated with Ta-Lib with a hand coded version, for the ease of use. 

Hope you enjoy!

