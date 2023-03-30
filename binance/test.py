from pybit import usdt_perpetual

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='jDLXGEjLiRQTzZKPeq',
    api_secret='CZKKM6Sg3QRtm7cHrgM2Y3oWhovmL9aQcs6U'
)

side = 'Sell'

qty2 = session_auth.my_position(
    symbol='FTMUSDT'
)

for i in qty2['result']:
    print(i)
    if str(i['side']) == side:
        qty2 = i['size']



print(qty2)

print(session_auth.place_active_order(
    symbol='FTMUSDT',
    side='Buy',
    order_type='Market',
    qty=float(qty2),
    time_in_force="GoodTillCancel",
    reduce_only=True,
    close_on_trigger=True
))