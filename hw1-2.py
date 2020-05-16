# Выполнить логические побитовые операции «И», «ИЛИ» и др.
# над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.\

a = 5
b = 6

a_and_b = a & b
a_xor_b = a ^ b
a_or_b = a | b

a_mov_left = 00 >> a
a_mov_right = a << 00


print('5 AND 6 = ', a_and_b, ',5 XOR 6 = ', a_xor_b, ',5 OR 6 = ', a_or_b, ',5 MOV left', a_mov_left, ', 5 MOV right', a_mov_right)
