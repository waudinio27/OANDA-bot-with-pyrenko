import pandas as pd
import pandas_ta as ta

# The Awesome Oscillator is an indicator used to measure market momentum.
# AO calculates the difference of a 34 Period and 5 Period Simple Moving Averages.
# The Simple Moving Averages that are used are not calculated using closing price but rather 
# each bar’s midpoints.
# AO is generally used to affirm trends or to anticipate possible reversals.
# 
# From: https://www.ifcm.co.uk/ntx-indicators/awesome-oscillator
# Awesome Oscillator is a 34-period simple moving average, plotted through the central points of the bars (H+L)/2, and subtracted from the 5-period simple moving average, graphed across the central points of the bars (H+L)/2.
# MEDIAN PRICE = (HIGH+LOW)/2
# AO = SMA(MEDIAN PRICE, 5)-SMA(MEDIAN PRICE, 34)
# where
# SMA — Simple Moving Average.


# Create a DataFrame so 'ta' can be used.
df = pd.DataFrame()

# Help about this, 'ta', extension
help(df.ta)

# List of all indicators
df.ta.indicators()

# Help about an indicator such as bbands
help(ta.ao)