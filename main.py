from PIL import Image
import numpy as np

input_image = Image.open("./i.jpg")
pixel_map = input_image.load()
width, height = input_image.size

for i in range(width):
  for j in range(height):
    
    R, G, B = input_image.getpixel( (i, j) )
    largest = max([R,G,B])
    med = int((R + G + B) / 3)
    result = (0,0,0)

    matriz = np.array([
      [largest, med, med],
      [med, largest, med],
      [med, med, largest]
    ])

    matriz = np.array([
      [R, G, B],
      [R, G, B],
      [R, G, B]
    ])

    mult_me = np.array([
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ])

    av = np.linalg.eigvals(matriz)
    #print(av)
    
    q, r = np.linalg.qr(matriz)
    #matriz = np.matmul(matriz, mult_me)
    matriz = r
    matriz = matriz.astype(int)

    av = av.astype(int)
    
    def mtx(a,b):
      return matriz[a][b]

    ##if(largest == R):
    ##  result = ( mtx(0,0), mtx(0,1), mtx(0,2) )
    ##elif(largest == G):
    ##  result = ( mtx(1,0), mtx(1,1), mtx(1,2) )
    ##elif(largest == B):
    ##  result = ( mtx(2,0), mtx(2,1), mtx(2,2) )

    ##result = ( av[0] , av[1], av[2]  )
    
    pixel_map[i, j] = result

input_image.save("result.jpg", format="png")