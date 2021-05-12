import json, requests

while True:
	#==================================================
	from_ = input(">>> Từ: ").upper()
	to = input(">>> Sang: ").upper()
	amount = input(f'>>> Số lượng cần quy đổi từ "{from_}" sang "{to}": ')
	#==================================================


	#==================================================
	file_name = open('file.json')		# mở file token.json
	data = json.load(file_name)			# load file
	#==================================================
	id_from = data["coin"][from_]
	id_to = data["coin"][to]			# Đọc file/đóng file
	file_name.close()
	#==================================================


	#==================================================
	url = f"https://web-api.coinmarketcap.com/v1/tools/price-conversion?amount={amount}&convert_id={id_to}&id={id_from}"

	a = requests.get(url)
										# Dùng module requests để gửi yêu cầu đến trang web
	b = a.json()

	c = b["data"]["quote"][str(id_to)]["price"]
	#==================================================

	print(f"""
==================================================

>>> Từ {amount} {from_} đổi được ~ {round(c, 3)} {to}

==================================================
		""")














