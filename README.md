# OANDA-bot
Hey guys this is the readme for an ongoing project :-) 

It is based on the brilliant work of Sergey Malchevskiy - 

https://github.com/quantroom-pro/pyrenko and it is recommended to read -

https://towardsdatascience.com/renko-brick-size-optimization-34d64400f60e for a good understanding. 

As you can see, I have added on how to use it with historical data from OANDA and a demo account key to be used with the build_history function. 

Then the prices from the pricing stream are transformed to a list with the .tolist() function. Like this it is possible to be iterated/enumerated with the do_next function inside of a for loop. 

The idea now is to use this in combination with a while loop. Like this the actual price stream from def get_candles can be used to form the renko prices and append the prices step by step over time. Lets try to build  a chart that updates with every cycle of the loop. 

The optimal brick size is chosen from the second example, were the evaluate_renko function is used for the optimization.

Any hints on how to improve the code and add the trading logic and the market orders for buy and sell are welcome!

In the near future, I will try to replace the ATR that is right now calculated with Ta-Lib with a hand coded version, for the ease of use and installation. 


Hope you enjoy!

=======
Any hints on how to improve the code are welcome!

Needed packages:

Linux:
=======
pip3 install -U setuptools  
pip3 install numpy  
pip3 install matplotlib  
pip3 install TA-Lib  
pip3 install --upgrade ta  
pip3 install pandas_ta  
pip3 install duckdb  
For fetching data from Yahoo finance  
pip3 install yfinance  

------------------------  
TODO: Switch to clickhouse from duckdb - https://clickhouse.tech/#quick-start
sudo apt-get install apt-transport-https ca-certificates dirmngr
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E0C56BD4

echo "deb https://repo.clickhouse.tech/deb/stable/ main/" | sudo tee \
    /etc/apt/sources.list.d/clickhouse.list
sudo apt-get update

sudo apt-get install -y clickhouse-server clickhouse-client

sudo service clickhouse-server start
clickhouse-client
------------------------  

more details on ta-lib: https://blog.quantinsti.com/install-ta-lib-python/#install-ta-lib-on-linux
