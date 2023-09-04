print("----------hiro-------------------")
# 引っ越し
h_move = 274680 + 1698818 + 102000 
#生活費
h_life = 220240 + 245729
print("引っ越し")
print(h_move)
print("生活費")
print(h_life)

print("----------mami-------------------")
m_food = 15337 + 33316
m_kids = 18089
m_life = m_food + m_kids
m_move = 108032 + 400000
print("引っ越し")
print(m_move)
print("生活費")
print(m_life)
print("-------------支払い--------------")

print('--------------引っ越し支払い------------------')
pay_move = (h_move + m_move) / 2
print('マミの払い')
print(pay_move - m_move - 600000)
print('ゆきちんの払い')
print(pay_move - h_move + 600000)

print('--------------生活費支払い------------------')
#print(hiro)
h_pay_life = (h_life + m_life) / 2 + 100000 - h_life
m_pay_life = (h_life + m_life) / 2 - 100000 - m_life
print('マミの払い')
print(m_pay_life)
print('ゆきちんの払い')
print(h_pay_life)



