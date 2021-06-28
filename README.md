# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key. Right now the prices from the Live Stream are being downloaded, but they don´t form the Renko Chart or Pattern like they should and plot a graphic. The values from the stream should get appended to the pandas dataframe but right now it is only showing NAN values. The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization. 

Hope you enjoy!
Any hints on how to improve the code and add the market orders for buy and sell are welcome!
