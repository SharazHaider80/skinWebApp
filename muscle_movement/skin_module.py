import cv2
import mediapipe
import random
import io
import numpy
import urllib, base64


def skin_displacment(image1, image2):
    drawingModule = mediapipe.solutions.drawing_utils
    faceModule = mediapipe.solutions.face_mesh

    circleDrawingSpec = drawingModule.DrawingSpec(thickness=2, circle_radius=1, color=(0, 255, 0))
    lineDrawingSpec = drawingModule.DrawingSpec(thickness=2, color=(0, 255, 0))

    X1 = []
    Y1 = []
    Z1 = []
    C1 = []
    with faceModule.FaceMesh(static_image_mode=True) as face:
        image = cv2.imdecode(numpy.fromstring(image1.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)

        results = face.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.multi_face_landmarks != None:
            for faceLandmarks in results.multi_face_landmarks:
                drawingModule.draw_landmarks(image, faceLandmarks, faceModule.FACE_CONNECTIONS, circleDrawingSpec,
                                             lineDrawingSpec)
                for data1 in faceLandmarks.landmark:
                    X1.append(round(data1.x, 5))
                    Y1.append(round(data1.y, 5))
                    Z1.append(round(-data1.z, 5))
                    C1.append(round(data1.x, 5) ** round(data1.y, 5))

    X = []
    Y = []
    Z = []
    C = []
    with faceModule.FaceMesh(static_image_mode=True) as face:
        image2 = cv2.imdecode(numpy.fromstring(image2.read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        results2 = face.process(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

        if results2.multi_face_landmarks != None:
            for faceLandmarks in results2.multi_face_landmarks:
                drawingModule.draw_landmarks(image2, faceLandmarks, faceModule.FACE_CONNECTIONS, circleDrawingSpec,
                                             lineDrawingSpec)

                for data in faceLandmarks.landmark:
                    X.append(round(data.x, 5))
                    Y.append(round(data.y, 5))
                    Z.append(round(-data.z, 5))
                    C.append(round(data.x, 5) ** round(data.y, 5))

    # Import libraries
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Change the Size of Graph using
    # Figsize
    # Creating array points using
    # numpy

    # To create a scatter graph
    # ax.scatter(X, Y, Z, c=C)
    # ax.scatter(X1, Y1, Z1, c=C1)

    img = plt.imread(image1)
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 1, 1, 0])
    lis = [0, 0, 0, 0, 0, 0]
    sh = 1
    point = 0
    color_count = []
    for n1, n2 in zip(Y, Y1):
        color_count.append(n2 - n1)

    leg = plt.legend()
    # get the individual lines inside legend and set line width
    for line in leg.get_lines():
        line.set_linewidth(1)

    color_list = []
    for x in color_count:
        n = random.randint(0, 5)
        if x > max(color_count) / 5 * 4:
            color_list.append('r')
        elif x > max(color_count) / 5 * 3:
            color_list.append('y')
        elif x > max(color_count) / 5 * 2:
            color_list.append('g')
        elif x > max(color_count) / 5 * 1:
            color_list.append('cyan')
        elif x < max(color_count) / 5 * 4:
            color_list.append('b')

    for x, y, z, u, v, w, ran in zip(X, Y, Z, X1, Y1, Z1, color_list):
        if point == 409 or point == 185 or point == 146 or point == 96 or point == 375 or point == 320 or point == 191 or point == 179 or point == 403 or point == 325 or point == 90 or point == 178 or point == 402 or point == 415 or point == 179:
            point = point + 1
            continue;
        if point == 246 or point == 150 or point == 159 or point == 158 or point == 157 or point == 24 or point == 153 or point == 152 or point == 145 or point == 144 or point == 163 or point == 136:
            point = point + 1
            continue;
        if point == 384 or point == 385 or point == 386 or point == 387 or point == 388 or point == 466 or point == 467 or point == 390 or point == 373 or point == 374 or point == 380 or point == 381 or point == 382 or point == 63 or point == 359:
            point = point + 1
            continue;
        plt.plot([x, u], [y, v], [z, w], '<-', color=ran, linewidth=1.0)
        # ax.quiver(x, y, u - x, v - y, angles='xy', scale_units='xy', scale=1.2)

        if point == 103 or point == 67 or point == 109 or point == 10 or point == 338 or point == 297 or point == 332:
            plt.plot([x, u], [y - 0.025, v - 0.025], [z, w], '<-', color=ran, linewidth=1.0)
        point = point + 1
        if sh == 0:
            plt.plot([(x + lis[0]) / 2, (u + lis[3]) / 2], [(y + lis[1]) / 2, (v + lis[4]) / 2],
                     [(z + lis[2]) / 2, (w + lis[5]) / 2], '<-', color=ran, linewidth=1.0)
        # plt.plot([x+0.0150, u+0.0150], [y+0.0150, v+0.0150], [z+0.0150, w+0.0150], '<-', color='y')
        lis = [x, y, z, u, v, w]
        sh = 0
    # trun off/on axis

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    image_string = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_string
    # plt.savefig('foo.png')

    # plt.axis('on')

    # # show the graph
    # plt.show()