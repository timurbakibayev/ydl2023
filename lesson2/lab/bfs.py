from PIL import Image, ImageDraw
canvas = Image.new('RGB', (500, 500), color=(73, 109, 137))
img = ImageDraw.Draw(canvas)

# # Draw a rectangle
# img.rectangle((100, 100, 400, 400), fill=(255, 255, 255), outline=(0, 0, 0))
# img.ellipse((200, 200, 300, 300), fill=(255, 0, 0), outline=(0, 0, 0))
#
# # save the image
# canvas.save('rectangle.png')

# BFS - Breadth First Search
# Метод поиска в ширину

a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

b = []
for i in range(len(a)):
    b.append([])
    for j in range(len(a[i])):
        b[i].append(0)

b[5][6] = 1

w = 30


def draw(img, w, a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                img.rectangle((j * w, i * w, j * w + w, i * w + w), fill=(0, 0, 0), outline=(0, 0, 0))
            if b[i][j] > 0:
                img.text((j * w + 10, i * w + 10), str(b[i][j]), fill=(255, 255, 255))


def one_step(k):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if b[i][j] == k:
                if a[i - 1][j] == 0 and b[i-1][j] == 0:  # There is no wall above us
                    b[i - 1][j] = k + 1  # We can go up
                if a[i + 1][j] == 0 and b[i+1][j] == 0:  # There is no wall below us
                    b[i + 1][j] = k + 1  # We can go down
                if a[i][j - 1] == 0 and b[i][j-1] == 0:  # There is no wall to the left of us
                    b[i][j - 1] = k + 1
                if a[i][j + 1] == 0 and b[i][j+1] == 0:  # There is no wall to the right of us
                    b[i][j + 1] = k + 1


for i in range(1, 100):
    one_step(i)

current_i = 9
current_j = 3

draw(img, w, a, b)


while b[current_i][current_j] > 1:
    k_minus_one = b[current_i][current_j] - 1
    if b[current_i - 1][current_j] == k_minus_one:
        current_i = current_i - 1
    elif b[current_i][current_j + 1] == k_minus_one:
        current_j = current_j + 1
    elif b[current_i + 1][current_j] == k_minus_one:
        current_i = current_i + 1
    elif b[current_i][current_j - 1] == k_minus_one:
        current_j = current_j - 1
    else:
        print('Path not found')
        break
    img.ellipse((current_j * w + 10, current_i * w + 10, current_j * w + w - 10, current_i * w + w - 10),
                fill=(255, 0, 0), outline=(0, 0, 0))

canvas.show()
