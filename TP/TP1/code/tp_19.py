def carte(li):
    x = 0
    y = 0
    for i in range(len(li)):
        if str((li[i])[1]) == 'n':
            y += int((li[i])[0])
        elif str((li[i])[1]) == 's':
            y -= int((li[i])[0])
        elif str((li[i])[1]) == 'o':
            x += int((li[i])[0])
        elif str((li[i])[1]) == 'e':
            x -= int((li[i])[0])
        else:
            print("erreur")
    if y >= 0:
        y = [y,'n']
    else:
        y = [abs(y),'s']
    if x >= 0:
        x = [x,'o']
    else:
        x = [abs(x),'e']
    return [y,x]
print(carte([[50,'n'],[20,'e'],[30,'s'],[82,'e'],[48,'n'],[43,'o'],[51,'s'],[18,'n'],[46,'e']]))     