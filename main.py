from datetime import datetime, time, date, timezone
from pytz import timezone


# data_e_hora_atuais = datetime.now()
# fuso_horario = timezone('Brazil/east')
# data_e_hora_GMT_menos3 = data_e_hora_atuais.astimezone(fuso_horario)
# data_e_hora_GMT_menos3_em_texto = data_e_hora_GMT_menos3.strftime('%d/%m/%Y %H:%M')
#
# data_e_hora_atuais = datetime.now()
# fuso_horario = timezone('Brazil/Acre')
# data_e_hora_GMT_menos5 = data_e_hora_atuais.astimezone(fuso_horario)
# data_e_hora_GMT_menos5_em_texto = data_e_hora_GMT_menos5.strftime('%d/%m/%Y %H:%M')
#
# print(data_e_hora_GMT_menos3_em_texto)
# print(data_e_hora_GMT_menos5_em_texto)

def horaAtual(time_zone: str):
    hora_atual: str = datetime.now().astimezone(timezone(time_zone)).strftime('GMT%Z %H:%M')
    return hora_atual

print(horaAtual('Brazil/east'))
print(horaAtual('Brazil/Acre'))

