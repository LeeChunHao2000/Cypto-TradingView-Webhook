# Cypto-TradingView-Webhook

A Cypto Trading Frame With TradingView's webhook alerts

## Warning

This is an UNOFFICIAL trading Frame for TradingView's webhook alerts written in Python 3.7

The library can be used to to place trades with Tradingview's webhook alerts

USE THIS FRAME AT YOUR OWN RISK, I WILL NOT CORRESPOND TO ANY LOSES

## Features

- Get Sigal from Trading and place order on FTX exchange (Only for market order)
## Donate

If useful, buy me a coffee?

- ETH: 0xA9D89A5CAf6480496ACC8F4096fE254F24329ef0

## Installation

    $ git clone https://github.com/LeeChunHao2000/Cypto-TradingView-Webhook.git

 - This trading frame depends on several package, so you need to install them first!

    $ pip install -r requirements.txt

## Requirement

1. [Register an account](https://ftx.com/#a=2500518) with FTX exchange _(referral link)_
2. [Generate API key and secret](https://ftx.com/profile), assign relevant permissions to it
3. Set up your own signal with webhook on [TradingView](https://tw.tradingview.com/)
4. Clone this repository, and put in the key and secret
5. Enjoy your own tradingView Trading Bot

## Quickstart

This is an introduction on how to set up your own Trading Bot.

First, we need to start the server that will listen for tradingview's webhooks. 

If you have no sever, heroku could helps you set up your own sever.

Second, configure your api key in config.py:

    API_KEY     = 'PUY_MY_API_KEY_HERE'
    API_SECRET  = 'PUY_MY_API_SECRET_HERE'

Last, set up your the webhook format on TradingView, it will look like json, here is an example:

    {"pair": "BTC-PERP", "side": "buy", "size": "0.01"}

Please make sure everthing is RIGHT, or you may lose your money！

Other than that, it should be good to go! If you have any questions just ask or create an issue on github！
### Version Logs
#### 2020-12-25

 - Birth!

