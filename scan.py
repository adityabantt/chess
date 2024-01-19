from PIL import Image
import pyautogui

TOP_LEFT_X, TOP_LEFT_Y = 190, 83
BOX = 122
PATH = "D:\\Code\\Git\\Main\\chess\\pieces\\"



def scan():
    fen = ""
    counter = 0
    replace_colors = [(244, 246, 128), (187, 204, 68), (119, 153, 84), (233, 237, 204)]
    for i in range(8):
        for j in range(8):
            img = pyautogui.screenshot(region=(j * BOX + TOP_LEFT_X, i * BOX + TOP_LEFT_Y, BOX, BOX))
            pixels = img.load() 

            for y in range(img.size[1]): 
                for x in range(img.size[0]): 
                    if pixels[x, y] in replace_colors:
                        pixels[x, y] = (255, 255, 255)
            img_path = 'images/' + str(i+1) + str(j+1) + '.png'
            img.save(img_path)
            
            if pyautogui.locate(PATH + "bb.png", img_path, confidence=0.4):
                fen += "b"
            elif pyautogui.locate(PATH + "bk.png", img_path, confidence=0.4):
                fen += "k"
            elif pyautogui.locate(PATH + "bn.png", img_path, confidence=0.4):
                fen += "n"
            elif pyautogui.locate(PATH + "bp.png", img_path, confidence=0.4):
                fen += "p"
            elif pyautogui.locate(PATH + "bq.png", img_path, confidence=0.4):
                fen += "q"
            elif pyautogui.locate(PATH + "br.png", img_path, confidence=0.4):
                fen += "r"
            elif pyautogui.locate(PATH + "wb.png", img_path, confidence=0.4):
                fen += "B"
            elif pyautogui.locate(PATH + "wk.png", img_path, confidence=0.4):
                fen += "K"
            elif pyautogui.locate(PATH + "wn.png", img_path, confidence=0.4):
                fen += "N"
            elif pyautogui.locate(PATH + "wp.png", img_path, confidence=0.4):
                fen += "P"
            elif pyautogui.locate(PATH + "wq.png", img_path, confidence=0.4):
                fen += "Q"
            elif pyautogui.locate(PATH + "wr.png", img_path, confidence=0.4):
                fen += "R"    
            else:
                fen += "1"
        fen += "/"
    # repacle the 1s with the correct number
    for i in range(8):
        for j in range(1, 9):
            fen = fen.replace("1"*j, str(j))
    print(fen)

scan()