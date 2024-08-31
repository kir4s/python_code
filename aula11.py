larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt 
print('sua parede tem a dimensâo de {}x{} e sua área é de {}m2.'.format(larg, alt, area))
tinta = area / 2 
print('para pintar essa parede, você precisará de {}L de tinta.'.format(tinta)) 