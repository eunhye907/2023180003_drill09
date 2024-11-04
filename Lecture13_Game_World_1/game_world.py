# world[0] : 백그라운드 객체들
# world[1] : foreground 객체들
world = [[], [], []]

def add_object(o, depth):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer: # 이걸 넣지 않으면 존재하지 않는 객체를 지울수도 있기에 오류가 발생할 가능성 O
            layer.remove(o)
            return

    print(f'CRITICAL: 존재하지 않는 객체{o}를 지우려고 합니다.')