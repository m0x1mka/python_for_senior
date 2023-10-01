from functools import partial

to_Timur = partial(send_email, "Тимур", "timyrik20@beegeek.ru")
text_to_user = "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут...."
send_an_invitation = partial(send_email, text=text_to_user)
