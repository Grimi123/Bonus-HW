import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

answer_index = random.randint(0,25)
answer = alphabet[answer_index]  #隨機產生英文序號 並對應設為答案



tries_number = 0
a_d = []
e_h = []
i_l = []
m_p = []
q_t = []
u_x = []
y_z = []

guess = "no"
while guess != answer:
	guess = input("Guess the lowercase alphabet:")  #輸入猜測
	if guess not in alphabet:
		print("Please enter a lower alphabet")
		continue
	guess_index = alphabet.index(guess)  #轉為英文序號
	if guess_index < answer_index:  #界定是否小於答案的英文序號
		print("The alphabet you are looking for is alphabetically higher.")
		tries_number += 1 #猜錯則嘗試數加上一
	if guess_index > answer_index:  #界定是否大於答案的英文序號
		print("The alphabet you are looking for is alphabetically lower.")
		tries_number += 1 #猜錯則嘗試數加上一
	if 0 <= guess_index <= 3: #界定區間並累計*次數
		a_d.append("*")
	if 4 <= guess_index <= 7:
		e_h.append("*")
	if 8 <= guess_index <= 11:
		i_l.append("*")
	if 12 <= guess_index <= 15:
		m_p.append("*")
	if 16 <= guess_index <= 19:
		q_t.append("*")
	if 20 <= guess_index <= 23:
		u_x.append("*")
	if 24 <= guess_index <= 25:
		y_z.append("*")

print("Congratulations! You guessed the alphabet \"%s\" in %d tries." % (answer,tries_number+1))
print()
print("Guess Histogram:")
print("a - d:", "".join(a_d))
print("e - h:", "".join(e_h))
print("i - l:", "".join(i_l))
print("m - p:", "".join(m_p))
print("q - t:", "".join(q_t))
print("u - x:", "".join(u_x))
print("y - z:", "".join(y_z))