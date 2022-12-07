dag = input('welke dag is het? | ma/di/wo/do/vr/za/zo : \n')

ma= 'Maandag'
di= 'Dinsdag'
wo= 'Woensdag'
do = 'Donderdag'
vr= 'Vrijdag'
za = 'Zaterdag'
zo = 'Zondag'


while dag == 'ma':
    print('di, wo, do, vr, za, zo')
    break
while dag == 'di':
    print('wo, do, vr, za, zo, ma')
    break
while dag == 'wo':
    print('do, vr, za, zo, ma, di,')
    break
while dag == 'do':
    print('vr, za, zo, ma, di, wo,')
    break
while dag == 'vr':
    print('za, zo, ma, di, wo, do ')
    break
while dag == 'za':
    print('zo, ma, di, wo, do, vr')
    break
while dag == 'zo':
    print('ma, di, wo, do, vr, za')
    break