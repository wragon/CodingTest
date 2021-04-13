#%% #13305
N = int(input())
dist = list(map(int, input().split()))  # 거리
price = list(map(int, input().split()))  # 주유 가격

oil_cost = price[0]
total_cost = 0
for i in range(N-1):
    if oil_cost > price[i]:
        oil_cost = price[i]
    total_cost += dist[i] * oil_cost

print(total_cost)