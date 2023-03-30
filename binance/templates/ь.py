from pybit import usdt_perpetual

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='jDLXGEjLiRQTzZKPeq',
    api_secret='CZKKM6Sg3QRtm7cHrgM2Y3oWhovmL9aQcs6U'
)

print(session_auth.set_leverage(
    symbol='BTCUSDT',
    buy_leverage=21,
    sell_leverage=21
))

print(session_auth.place_active_order(
    symbol='BTCUSDT',
    side='Sell',
    order_type='Market',
    qty=0.001,
    time_in_force="GoodTillCancel",
    reduce_only=False,
    close_on_trigger=False
))