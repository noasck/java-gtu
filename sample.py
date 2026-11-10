import math
import sys
import time


def round_by_rule(value):
    return math.floor(value + 0.5 + 1e-9)


def draw_line(field, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1

    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1

    error = dx + dy

    while True:
        field[y0][x0] = "#"

        if x0 == x1 and y0 == y1:
            return

        twice = 2 * error

        if twice >= dy:
            error += dy
            x0 += sx

        if twice <= dx:
            error += dx
            y0 += sy


def create_frame(angle):
    t = (angle % 360) * math.pi / 180
    cos_t = math.cos(t)
    sin_t = math.sin(t)

    vertices = [
        (x, y, z)
        for x in (-1, 1)
        for y in (-1, 1)
        for z in (-1, 1)
    ]

    projected = []

    for x, y, z in vertices:
        xr = x * cos_t - z * sin_t
        zr = x * sin_t + z * cos_t

        column = 10 + round_by_rule(4 * xr + 2 * zr)
        row = 6 + round_by_rule(-3 * y + zr)

        projected.append((column, row))

    field = [["."] * 21 for _ in range(13)]

    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            differences = sum(
                vertices[i][coordinate] != vertices[j][coordinate]
                for coordinate in range(3)
            )

            if differences == 1:
                x0, y0 = projected[i]
                x1, y1 = projected[j]
                draw_line(field, x0, y0, x1, y1)

    return "\n".join("".join(row) for row in field)


def main():
    angle = int(input("Начальный угол: "))

    try:
        sys.stdout.write("\033[2J")

        while True:
            frame = create_frame(angle)

            sys.stdout.write(f"\033[HУгол: {angle % 360:3d}°\n{frame}\n")
            sys.stdout.flush()

            angle += 1
            time.sleep(0.1)

    except KeyboardInterrupt:
        sys.stdout.write("\033[15;1H")
        print("Анимация остановлена.")


if __name__ == "__main__":
    main()
