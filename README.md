# 这是提交机器人部视觉组的考核作业的仓库

## HW1
内容：本题首先设置了一个‘5x5’的矩形结构元素,对图像进行开运算消除细小物体。再进行图片的颜色空间转化，并进行合适二值化的处理。然后进行连通域处理，将符合题意的连通域部分设置为黄色。最后，再次进行一次开运算消除小部分也变黄的部分，期间经过不断地调参，获得最终结果。

## HW2
内容：本题想通过合适的处理只将符合题意的那个部分定为一个连通域，最后只需画出它的外接矩阵即可。所以首先设置了一个‘9x9’的矩形结构元素，进行开运算，颜色空间转化，二值化处理，连通域处理调整合适的参数，运用连通域函数返回的stats进行外接矩阵的描绘，获得最终结果。

## HW3
内容：本题思路是首先提取红色像素，将其转化为二值化的图片，再进行连通域的处理，画出指定图形的外接矩阵。而inRange函数则完美得匹配了我的想法，所以首先把图片转化为HSV的颜色空间，使用恰当的红色像素的范围配合inRange，连通域的处理，进行合适的调参，画出指定图形的外接矩阵，获得最终结果。