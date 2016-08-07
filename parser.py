import polygon

# Str => RatPoint
def my_eval(str):
    c = str.split(",")
    return RatPoint(string_to_rat(c[0]), string_to_rat(c[1]))

# Str => {polygons: [RatPoint], lines: [(RatPoint, RatPoint)]}
def parse_input(str):
    polygons = []
    lines = str.split("\n")
    counts = eval(lines[0])
    lines = lines[1:]

    for i in range(0, counts):
        tmp = eval(lines[0])
        lines = lines[1:]
        points = []
        for j in range(0, tmp):
            points.append(my_eval(lines[0]))
            lines = lines[1:]
        polygons.append(points)

    ls = []
    for i in range(0, eval(lines[0])):
        p = lines[0].split(" ")
        ls.append((my_eval(p[0]), my_eval(p[1])))
        lines = lines[1:]

    return {polygons: polygons, lines: ls}
