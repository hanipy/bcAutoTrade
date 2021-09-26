import pyupbit

access = "2PpVZds2hxs1nxvz4nWIKaLGBC6JmvEPrOLxnWzS"          # 본인 값으로 변경
secret = "a4yWvmQyiqkoEycpYUO3lD8nOy2YAGBD7QdOD7xL"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회