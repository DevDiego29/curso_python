larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print('sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(larg, alt, área))
tinta = área / 2
print('para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
