#Código retirado em video do youtube sobre redes neurais em python.
#Youtuber: Lucas Pesquisa
# Link do video=https://www.youtube.com/watch?v=jj9lUzAoYII&list=PLVZlSIIsZ1ruW7wgzSTxhwX1xLJd16r0x&index=2&ab_channel=LucasPesquisa

import pandas as pd

w1=1

w2=1
bias= -1

testing_inputs = [(0,0), (0,1), (1,0),(1,1)]

correct_outputs=[False, False, False, True]

outputs=[]

for test_input, correct_output in zip(testing_inputs,correct_outputs):
    linear_combination = w1 * test_input[0] + w2 * test_input[1]+bias
    output=int(linear_combination >=0)
    is_correct_str='Sim' if output == correct_output else 'Nao'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_str])


wrong_number = len([output[4] for output in outputs if output[4] == 'Nao'])
output_frame = pd.DataFrame(outputs, columns=['Valor 1', '  Valor 2', '  Combinacao Linear', '  Previsao', '  Esta Correto?'])
if not wrong_number:
    print('Parabens esta tudo correto.\n')
else:
    print('Voce errou {}.  Continue  tentando!\n'.format(wrong_number))
print(output_frame.to_string(index=False))

