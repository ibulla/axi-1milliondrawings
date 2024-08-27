from axi import Device, Drawing
import json
import requests
from datetime import datetime

################################################
###        by 1milliondrawings.com           ###
###                                          ###
### 1. go to 1milliondrawings.com	     ###
### 2. save your drawing                     ###
### 3. plot your DRAWING-ID                  ###
###                                          ###
################################################

def printer(PATH):
    drawing = Drawing(PATH)
    d = Device()
    d.enable_motors()
    d.run_drawing(drawing)
    d.disable_motors()

def bigChar(letter,millimeter,plusX,plusY):
    faktor = float((millimeter / 20.0) / 640.0) #1=20mm  Xmm/20mm=640px
    if plusX:
        XX = ((plusX * 500) * faktor)
    else:
        XX = 0
    if plusY:
        YY = ((plusY * 650) * faktor)
    else:
        YY = 0
    neuA = []
    zahlA = 0
    for a in letter:
        for aa in a:
            ax = round(XX + (a[zahlA][0] * faktor),3)
            ay = round(YY + (a[zahlA][1] * faktor),3)
            neuA.append((ax,ay))
            zahlA += 1
    return neuA

def smallChar(letter,millimeter,plusX,plusY):
    faktor = float((millimeter / 20.0) / 640.0) #1=20mm  Xmm/20mm=640px
    if plusX:
        XX = ((plusX * 640) * faktor)
    else:
        XX = 0
    if plusY:
        YY = ((plusY * 680) * faktor)
    else:
        YY = 0
    neuA = []
    zahlA = 0
    for a in letter:
        for aa in a:
            ax = round(XX + (a[zahlA][0] * faktor),3)
            ay = round(YY + (a[zahlA][1] * faktor),3)
            neuA.append((ax,ay))
            zahlA += 1
    return neuA

def print_rectangle(startX,startY,lang,hoch):
    langx = float(lang / 20.0) #1=20mm
    langy = float(hoch / 20.0) #1=20mm
    startx = float(startX / 20.0) #1=20mm
    starty = float(startY / 20.0) #1=20mm
    neuA = []
    neuA.append((startx,starty))
    neuA.append(((startx+langx),starty))
    neuA.append(((startx+langx),(starty+langy)))
    neuA.append((startx,(starty+langy)))
    neuA.append((startx,starty))
    return neuA

def print_logoPos(letter,millimeter,plusX,plusY):
    faktor = float((millimeter / 20.0) / 640.0) #1=20mm  Xmm/20mm=640px
    XX = float(plusX / 20.0)
    YY = float(plusY / 20.0)
    neuA = []
    zahlA = 0
    for a in letter:
        for aa in a:
            ax = round(XX + (a[zahlA][0] * faktor),3)
            ay = round(YY + (a[zahlA][1] * faktor),3)
            neuA.append((ax,ay))
            zahlA += 1
    return neuA

def print_logo(h,x,y):
    logo = []
    logo.append([(19.3,61.9),(25.2,58.2),(31.6,50.4),(37.8,42.1),(41.7,36.6),
    (41.7,41.1),(40.5,56.1),(38.8,75.1),(37.3,97.2),(37,112.1),(38.3,118.7)])
    logo.append([(51.6,84.6),(52.8,80.3),(54,82.5),(54,88.1),(52.8,95.8),(52.8,104.9),
    (54,114.9),(55.4,117),(59.1,112.8),(63.4,97.3),(65.2,88.9),(67.9,81.8),(69.5,81.5),
      (70.9,83.9),(70.9,87.3),(70.9,96),(70.1,107.8),(70.9,115.5),(73.6,117),(76.2,114.9),
      (80.2,104.3),(84.4,90),(87.2,79.6),(88.6,80.2),(87.9,88.3),(87.4,101.9),(87.8,111.9),
      (89.4,115.8),(91.6,117.6),(96.1,116.5),(98.8,111.9),(103.6,100.4),(107.4,83.8),
    (108.9,76.7),(107.4,88.3),(105.7,103.8),(106.2,111.1),(107,114.9),(109.5,117.6),
      (112.8,117.6),(115.2,113.5),(120.8,99.2),(131.4,77.3),(138,55.9),
    (139.2,42.1),(139.2,32.4),(136.1,26.1),(134.2,26.1),(133,28),(128.6,42.1),
      (124.9,63),(123.5,80.2),(123.2,100.6),(124.5,109),(127.8,115.9),(130.8,118.4),
      (134.4,119.1),(137,116.9),(141.2,109.3),(151.6,88.1),(159.8,66.9),(164.5,47.4),
      (165.2,36.8),(164.5,32.6),(163.1,29),(161.1,27.9),(159,28.6),(158,30.8),(156.8,34.5),
      (154.5,44),(152.6,54.1),(150.6,69.3),(149.4,84.6),(148.8,99.3),(149.5,106.1),
      (151,111.5),(153.8,115.9),(155.8,117.8),(159.8,119.1),(162.6,117.8),(166.1,113.3),
      (169.9,104.6),(173.5,93.3),(176.6,76.8),(176.6,75),(175.5,75.1),(173.5,98.5),
      (173.5,109.3),(174.8,114.1),(176.6,117.3),(178.8,118.3),(180.8,117.6),(182.8,115),
      (185,108.6),(189.1,95.1),(190.4,90.1),(193.4,79.4),(194.6,75.3),(197,70.9),
    (199.1,70.6),(206,72.6),(207.9,77.3),(209,88.6),(208.8,106.4),(203.6,116.4),
      (198,119.1),(193.5,118.3),(190.6,112.5),(189,105.3),(190.1,96.3),(196.5,72.1),
      (202.6,70.4),(206.1,75),(208.4,86),(208.8,92.4),(208.8,95.1),(210,99.9),(213.4,101.1),
      (217.5,100),(219.4,97.3),(221.4,92.6),(223.8,86.8),(226.2,77.5),(226.9,75.9),
      (225.9,86.5),(225.4,98.5),(225.9,108.1),(226.5,113.3),(229,116.8),(231.2,115.5),
      (233.8,107.8),(236.4,96.1),(238.6,88.3),(241.1,80),(242.4,73.8),(241.1,72.6),
      (242.4,83.1),(242.4,94),(242.4,103.8),(243.9,111.5),(245.1,115.6),(247,117.5),
      (250.2,117),(253.2,113.6),(255.8,107.3),(259.9,94),(262,84.9),(264.2,74.3),
      (270.1,70.5),(277.4,73.1),(271.8,69.6),(269.9,69.9),(266.4,73.6),(260.5,89.3),
      (257.4,106.6),(258.8,113.9),(260.4,118.1),(264,119.1),(267.6,117),(274.3,106.9),
      (276.4,99),(279.9,72.6),(282.5,45.5),(284.5,24.4),(286.1,24.4),(278.9,74.9),
      (277,90.9),(275.9,108.6),(277.2,115),(279.2,118.1),(282,119.1),(284.9,115),
      (289.2,102.9),(293,90),(296.8,74.5),(296.9,73.3),(297.5,68.6),(296.6,61.9),
    (295.4,59),(294.2,60.3),(294.2,64.1),(294.6,67.1),(296,70.8),(300.5,75.1),
      (304.2,78.5),(305.9,85),(305.9,94),(305.9,102.9),(305.2,111.4),(306.5,115),
    (309.6,118.3),(312.8,117),(315.1,113.3),(317.9,104.1),(320,94.9),(322.6,84.3),
      (323.9,79),(326.5,73.3),(329.9,71),(332.6,71.8),(335.9,74.5),(336.9,77.8),
      (337.6,85.9),(335.4,75.5),(331.5,72.3),(328.9,72.4),(325.5,76.5),(321.5,92),
      (320,100.6),(319.1,109.9),(319.2,114.6),(320,117.8),(322.6,120.4),(325.9,120.4),
      (329,117),(331.4,111.6),(333.5,103.8),(336.6,90.4),(340.1,79.4),(338.9,78.8),
      (336.5,95.9),(335.4,103.1),(335.4,107.3),(335.8,112),(336.9,115.6),(339,118.6),
      (341.6,119.3),(345.1,115.6),(348.5,108.4),(351.8,98.5),(356.1,82.5),(357.5,75.1),
      (356.6,73.5),(355.6,75.1),(353,97.5),(352.8,103.6),(353,109.5),(354.1,115.5),
      (356.5,118.3),(359.8,118.4),(362.9,113.8),(365.9,106.8),(368.1,94),(369.2,81.4),
      (369.2,76.9),(367.5,76.1),(367.5,81),(367.6,102.3),(369.2,110.8),(371.1,115.6),
      (373.5,117),(376.5,115.6),(379.2,111.4),(380.8,104.6),(383.4,86.6),(384.4,75.1),
      (384.4,70.1),(383,67.3),(381.5,68),(381.2,71.8),(381.1,82),(382.4,89.3),(384.1,94.5),
      (387.9,96.1),(391.2,95.9),(394.2,91.4),(396.4,85.6),(398.4,80.1),(398.9,75.3),
      (397.8,74),(396.4,75.1),(394.2,98.5),(394.2,107),(394.9,112.9),(396.4,116.8),
      (398.9,118.5),(402,117),(404.2,113.4),(408,105.8),(411.6,93.6),(415.2,79),(413.5,78),
      (414.1,100.6),(415.2,110),(416.9,117.8),(418.2,117.8),(421.6,110.1),(423.8,100),
      (428.6,79.8),(429.9,73.1),(431.1,74.4),(431.1,82),(431.1,91.6),(431.1,103.9),
      (432,111.5),(433.9,116.8),(436.6,119.3),(439.6,116),(444.1,108),(446.8,97.6),
      (450.6,80.6),(453.6,71.1),(455.8,70),(458.6,71.3),(464.1,74.5),(469,78.8),(456.3,69.9),
      (453.6,73.1),(445.5,102.4),(445.4,111.8),(446.7,116.8),(449.8,120.4),(453.4,120.4),
      (457.5,116.8),(461.4,109.9),(464,96.4),(467.6,82.9),(470.4,72.6),(462.8,106.5),
      (462.1,116.8),(462.8,126),(463.8,142.4),(463.8,154.8),(461.5,162.9),(457.9,168.8),
      (452.9,171.9),(446.8,172.5),(441.5,171.4),(437.1,168.8),(432.6,164.8),(430.4,161),
      (429,155.3),(429.4,148.6),(431.4,145.3),(433.8,142.3),(437.9,139.6),(442.2,137.1),
      (447.5,135.3),(452.1,133.8),(458.1,132.5),(469,131.5),(473.9,131.8),(480.4,131.9),
      (482,131.9),(476.2,131)])
    logo.append([(464.3,100.7),(469.9,97.8),(475,91.8),(478.4,85.3),(481.1,76.1),
      (482.6,70.1),(482.6,67.6),(481.4,67.6),(480.9,69.1),(480.9,72.5),(481.2,80.3),
      (482.6,87.1),(485,94.9),(486.8,102.3),(487.8,108.9),(487.8,113.1),(486.6,116.8),
      (485,118.5),(482.8,119.5),(479.9,119.5),(478,118.8),(476.9,117.8),(475.5,115.5),
      (475.2,113.6),(475.1,111.8)])
    logo.append([(504,114.6),(501.8,116),(501.8,118.6),(504,119.7),(505.6,118.6),
      (505.6,116.4),(504,114.6)])
    logo.append([(524.2,77.8),(524.2,76.6),(522.4,73.5),(519.9,73.5),(517.2,75.6),
      (515.9,78.9),(513.6,89.1),(512.8,97.1),(512.8,105.5),(514.4,113.1),(516.4,116.8),
      (519,118.5),(523.2,117.3),(525.5,114.3),(528.9,108.6),(531.4,102),(533.4,95.4),
      (536.1,83.3),(539.1,75.3),(540.6,71.6),(544.2,69.9),(547.4,71.6),(551.8,76.5),
      (548.2,72.6),(544.1,70.6),(540.5,72.6),(536.1,84.3),(534,97.6),(534,107.4),(535.6,115),
	  (537.4,116.8),(541.2,118.5),(545,117.6),(548.2,113.5),(551.6,103.9),(554,90.5),
      (554,80.8),(550.6,72.6),(548.3,74),(548.2,78.6),(548.3,85.3),(550.1,93.5),(554.2,98.5),
      (558.4,99.3),(562.8,97.5),(564.2,94.5),(566.6,87.6),(568.9,78.1),(567.9,85.8),
      (567.9,96.4),(568.2,106.5),(568.9,113.1),(569.6,116.8),(570.9,118.5),(573.2,118.5),
      (574.9,116.8),(576.8,111.5),(578.5,102.8),(580.1,94.5),(581.9,87.6),(583.2,82.9),
      (584.9,79.9),(586.2,79.6),(587.5,81),(587.5,82.9),(587.5,88.3),(586.8,97.6),
      (586.5,106.5),(586.9,112.4),(587.5,116.8),(588.8,118.5),(590.5,118.5),(591.6,117.4),
	  (594.6,113),(597.4,105.9),(600.6,95.9),(602.4,90.5),(605.4,81.4),(605.4,77.8),
      (602.1,76.8),(601,83.1),(601.8,99.5),(603.4,110.9),(604.4,115),(606.2,117.6),
      (608.6,118.5),(611,117.9),(614.2,114),(617.6,105.8),(621.1,94.4),(623.5,83.8),
      (624.2,76.5)])
    logo.append([(399.9,39),(397.2,40.8),(397.2,44),(399.9,45.3),(401.9,44),
      (401.9,41.3),(399.9,39)])
    logo.append([(179.2,38.8),(176.3,40.7),(176.3,44.2),(179.2,45.5),
      (181.3,44.2),(181.3,41.2),(179.2,38.8)])
    logo.append([(111.4,38.7),(108.4,40.7),(108.4,44.2),(111.4,45.6),
      (113.6,44.2),(113.6,41.2),(111.4,38.7)])
    ausgabeAxi = []
    for sign in logo:
        axiready = print_logoPos([sign],h,x,y)
        ausgabeAxi.append(axiready)
    return ausgabeAxi


def bigChars(letter,h,x,y):
    buchstabe = []
    if letter =="A" or letter == "a":
        buchstabe.append([(408.8,71.9),(208.6,74.9),(62.4,586.2),(196.1,577.5),(257.1,359.2),
        (362.3,357.8),(425,585.5),(572.7,585.3),(408.8,71.9)])
        buchstabe.append([(351.8,286),(270.4,285.8),(310,154.3),(351.8,286)])
    if letter == "B" or letter == "b":
        buchstabe.append([(113.8,108.2),(108.7,579.7),(394.2,587.2),(518,482.3),(364.9,347.7),
        (485.2,193.5),(311,61.3),(113.8,108.2)])
        buchstabe.append([(250.9,180.2),(250.9,273.2),(315.9,203.3),(250.9,180.2)])
        buchstabe.append([(250.9,411.9),(250.9,492.3),(315.9,456.4),(250.9,411.9)])
    if letter == "C" or letter == "c":
        buchstabe.append([(502.2,78.9),(471.1,250.1),(293.5,282.1),(265.6,424.4),
        (432.4,399.3),(498,548.9),(211,596.5),(94.2,457),(154.1,141),(502.2,78.9)])
    if letter == "D" or letter == "d":
        buchstabe.append([(137.6,574.6), (291.5,575.4), (410.3,556.6), (516.6,463.5),
        (531.8,297.7), (448.8,138.2),( 297,79.5), (132.7,83),(137.6,574.6)])
        buchstabe.append([(262.8,211), (268.4,439.6),( 399.1,327.1),(262.8,211)])
    if letter == "E" or letter == "e":
        buchstabe.append([(470,94.8),(123.6,102.9),(129.2,585.4),(504,570.9),(497,458.1),
        (281.7,460.2),(277.5,392.4),(375.4,388.9),(371.9,300.1),(270.5,295.9),
        ( 267.7,220.3),(488,206.4),(470,94.8)])
    if letter == "F" or letter == "f":
        buchstabe.append([(454.4,85.7),(118,108.2),(141.1,567.6),(277.5,562.7),(267,373.2),
        (360.7,362.7),(357.9,266.2),(262.1,267.6),(260,207.5 ),(454.4,197.7),(454.4,85.7)])
    if letter == "G" or letter == "g":
        buchstabe.append([(513.3,190.6), (439.2,275.9), (313.3,239.5), (225.7,364.1),
        (329.7,512.6), (336.2,441.7), (306.1,440.3), (374.7,366.6), (483.3,373.9),
        (472.1,609.6),( 354.5,608.6), (348.6,584.4), (218.7,605.2), (85.2,370.4),
        (230.8,90.6),(513.3,190.6)])
    if letter == "H" or letter == "h":
        buchstabe.append([(281.2,368.9), (281.2,579.3), (151.1,579.3), (137.1,90.5),
        (277.7,85.6), (281.2,298.5), (346.2,298.9), (346.2,89.1), (468.8,89.1),
        (472.3,582.8),( 351.7,579.8),( 348.3,369.6),(281.2,368.9)])
    if letter == "I" or letter == "i":
        buchstabe.append([(450.7,86.1),(168.2,82.6),(168.2,186.1),(227.6,186.1),
        (226.9,504.5),(173.1,508),(172.4,591),(454.9,591),(454.9,506.1),
        (391.3,504.7),(385.7,184),(454.9,181.2),(450.7,86.1)])
    if letter == "J" or letter == "j":
        buchstabe.append([(153.8,95.4),(153.8,216.4),(263.3,252.4),(263.2,201.6),(368.7,197.3),
        (364.5,418.8),(326.4,497.1),(254,505.6),(247.7,404.5),(144,404.5),(147.5,543),
        (250.6,609.3),(389.7,605),( 477.9,472.3),(485.3,95.4),(153.8,95.4)])
    if letter == "K" or letter == "k":
        buchstabe.append([(122.2,134.7),(136.9,573.9),(268.6,573.9),(265.1,415.9),(435.2,601.1),
        (527,472.7),(353.9,330),(488.1,195.1),(374.1,102.8),(260.2,226.4),
        (260.9,97),(122.2,134.7)])
    if letter == "L" or letter == "l":
        buchstabe.append([(319,121.5),(168,117.3),(157.3,576.7),(494.7,567.6),(478.6,443.8),
        (312.6,448),(319,121.5)])
    if letter == "M" or letter == "m":
        buchstabe.append([(66.8,547.5),(207.5,550.1),(251.3,331.3),(322.9,432),(364.9,336.8),
        (408.5,555.7),(556.5,543.3),(458.8,103.9),(349.5,103.9),(306.5,272.3),
        (264.2,113.9),(145,103.9),(66.8,547.5)])
    if letter == "N" or letter == "n":
        buchstabe.append([(251.6,543.8),(103.8,555.7),(110.7,96.3),(245.3,85.1),(381,319.9),
        (381,106.1),(517.3,101.2),(513.1,560.6),(362.8,545.2),(246.7,312.9),(251.6,543.8)])
    if letter == "O" or letter == "o":
        buchstabe.append([(496.3,149.2),(128.5,119.2),(146.7,567.1),(482.4,558),(496.3,149.2)])
        buchstabe.append([(342.3,209.6),(232.7,209.6),(250.1,472.2),(334.6,473.2),(342.3,209.6)])
    if letter == "P" or letter == "p":
        buchstabe.append([(349.6,570.4),(184.7,574.6),(151.2,132.5),(422.2,87.3),(519.9,215.4),
        (461.4,350.8),(335.5,369.7),(349.6,570.4)])
        buchstabe.append([(306.1,201.9),(315.9,291.4),(379.6,232),(306.1,201.9)])
    if letter == "Q" or letter == "q":
        buchstabe.append([(492.1,188.7),(246,55.1),(107.3,232),(88.4,536.8),(271.9,599.8),
        (404.3,569.9),(436.5,597.9),(536.9,522.9),(454.4,443.4),(492.1,188.7)])
        buchstabe.append([(350.4,381.4),(267.4,446.2),(274.7,254.4),(350.4,381.4)])
    if letter == "R" or letter == "r":
        buchstabe.append([(118.7,585.1),(269.1,585.1),(277.5,400.5),(398,585.1),(503.8,499.5),
        (365.8,317.1),(434.8,265),(463.5,166.9),(369.1,69),(132.1,72),(118.7,585.1)])
        buchstabe.append([(250.8,166),(246.8,265.5),(334.6,195),(250.8,166)])
    if letter == "S" or letter == "s":
        buchstabe.append([(525,119.4),(492.1,241.6),(291.6,229.9),(526.8,472.8),(488.6,598.6),
        (93.3,589.7),(109.7,455.7),(310,457.5),(91.9,223.3),(178.2,81.8),(525,119.4)])
    if letter == "T" or letter == "t":
        buchstabe.append([(549.3,95.1),(67.5,89),(78,244.2),(243.8,244.2),(245.4,600.4),
        (395.1,596.2),(394.2,243.5),(555.6,236.3),(549.3,95.1)])
    if letter == "U" or letter == "u":
        buchstabe.append([(243.6,106.3),(77.4,128),(99.1,538.7),(179.9,603.8),(463.1,607.3),
        (523.3,553.4),(565.2,117.6),(378.5,95.2),(372,487.7),(244.1,489.8),(243.6,106.3)])
    if letter == "V" or letter == "v":
        buchstabe.append([(202.5,119.4),(59.1,167),(258.2,595.3),(377.1,598.3),(556.1,142.7),
        (396,107.7),(315,442.3),(202.5,119.4)])
    if letter == "W" or letter == "w":
        buchstabe.append([(185.2,109.1),(42.5,129.7),(134.1,589.8),(252.3,579.3),(309.6,426.8),
        (372.5,589.8),(492.1,585.6),(587.1,146),(442.7,111.7),(393.5,355.5),(310,238),
        (237.9,382.2),(185.2,109.1)])
    if letter == "X" or letter == "x":
        buchstabe.append([(130.5,114.9),(52.9,230.6),(216.2,367.4),(90.3,523.4),(206.2,602.4),
        (323,454.5),(480.7,595.1),(573,492.7),(402.2,343.8),(542.3,168.1),(418.5,94.7),
        (296.4,257),(130.5,114.9)])
    if letter == "Y" or letter == "y":
        buchstabe.append([(165.2,141.2),(75.7,246.3),(241.2,376.7),(117.9,525.1),(235.3,608.2),
        (579.5,204.2),(467.8,113.6),(330,275.5),(165.2,141.2)])
    if letter == "Z" or letter == "z":
        buchstabe.append([(78.1,82.7),(85.8,236.4),(348.7,229.4),(107.9,472.6),(102.3,589.4),
        (536.5,588.2),(536.5,431.5),(325.9,442.1),(531.6,227.3),(529.5,74.9),(78.1,82.7)])
    if letter == "1":
        buchstabe.append([(117.1,221.3),(196.7,332.1),(254,281.5),(246,594.9),(418,594.9),
        (427.5,149.6),(276.1,56.4),(117.1,221.3)])
    if letter == "2":
        buchstabe.append([(79.7,201.1),(167.8,301),(299.9,226),(115.9,490),(125.7,602.6),
        (510.3,590),(519.1,460.8),(292.9,459.4),(473.8,144.8),(342,40.6),(79.7,201.1)])
    if letter == "3":
        buchstabe.append([(98,113),(114.1,248),(326.9,238.9),(173,348.7),(298.8,446.7),
        (129.9,476),(114.8,596.7),(470,586.2),(524.7,424.3),(396.7,349),(524.8,225.3),
        (496.2,79.2),(98,113)])
    if letter == "4":
        buchstabe.append([(100.9,344.5),(292.3,335.9),(257.4,608.4),(393.6,601.8),(427.7,334.7),
        (491.6,331.2),(512.8,214.1),(440.1,215.4),(458.3,95.8),(323.7,101.8),(307.2,218),
        (235.9,220.1),(255.6,71),(143.2,47.1),(100.9,344.5)])
    if letter == "5":
        buchstabe.append([(513.4,68.1),(495.4,209.2),(234.9,199.8),(234.9,245.3),(489.1,308),
        (546.1,447.1),(440.3,612.5),(234,614.4),(118.4,580.2),(116.5,430.3),(347.5,460.3),
        (350.3,393),(101.7,329.2),(88.4,59.4),(513.4,68.1)])
    if letter == "6":
        buchstabe.append([(292,55.3),(408,133.7),(248.9,392.3),(291,473),(280.3,335.9),
        (409.2,328.2),(435.1,559.4),(310.6,612.4),(186.5,566.9),(86.1,375.5),(292,55.3)])
    if letter == "7":
        buchstabe.append([(141.3,104.1),(153.2,238.2),(351.8,234.6),(322.9,289.5),(260.9,290.5),
        (251.8,389.5),(281.9,389.5),(183.9,601.8),(342.3,598.2),(513.9,221.3),
        (437.9,96.5),(141.3,104.1)])
    if letter == "8":
        buchstabe.append([(218.8,320),(119.9,481.1),(216.4,616.1),(416.5,614.6),(503.3,478.9),
        (391.5,325.7),(474.7,166.2),(389.4,55),(204.1,55),(132.1,164.8),(218.8,320)])
        buchstabe.append([(346,166.2),(257.9,166.2),(297.7,230.6),(346,166.2)])
        buchstabe.append([(301.9,429.9),(262.1,494.2),(346,494.2),(301.9,429.9)])
    if letter == "9":
        buchstabe.append([(274.2,610.4),(158.3,532),(334.3,243.4),(298.2,192.7),(285.9,329.7),
        (157,337.4),(161.1,116.2),(295.6,53.3),(419.7,98.8),(490.1,260.2),(274.2,610.4)])
    if letter == "0":
        buchstabe.append([(474.4,87.2),(106.1,80.9),(145.3,594.4),(474.4,594.4),(474.4,87.2)])
        buchstabe.append([(342.3,209.6),(232.7,209.6),(250.1,472.2),(334.6,473.2),(342.3,209.6)])
    if letter == ".":
        buchstabe.append([(293.9,357.2),(208.9,410.8),(154.6,476.1),(210.7,555.6),
        (310.9,609.4),(409.9,526.1),(443.4,444.9),(367.7,386.5),(293.9,357.2)])
    if letter == "?":
        buchstabe.append([(105.1,161.6),(170.2,272),(303,133.6),(371.5,193.8),(232.3,447.9),
        (291.7,461.8),(201.2,541.9),(299.1,628.2),(398.2,529.3),(305.2,464.3),
        (381.6,482.9),(502.8,194.1),(419.7,42.6),(237,29.7),(105.1,161.6)])
    if letter == "=":
        buchstabe.append([(93.3,333.9),(71.3,497.1),(583.7,475.8),(573.4,338.1),(107.4,331),
        (579.4,312.9),(584.2,166.1),(44.1,176.2),(71,334.7),(93.3,333.9)])
    if letter == "/":
        buchstabe.append([(396.3,114.7),(257.1,28.7),(36.9,490.7),(149.5,572.5),(392.3,128.5),
        (187.7,554.2),(315.2,627.1),(591.4,83),(438.7,32.7),(396.3,114.7)])
    if letter == ":":
        buchstabe.append([(392.8,356.8),(334.4,333.6),(415.4,265.4),(443.6,197),(379.9,147.9),
        (317.9,123.3),(246.3,168.4),(200.6,223.3),(247.8,290.2),(328.6,333.5),
        (259.3,377.2),(213.6,432.2),(260.8,499),(345.1,544.3),(428.4,474.2),
        (456.6,405.9),(392.8,356.8)])
    if letter == "#":
        buchstabe.append([(226.3,22.4),(107.5,22.4),(107.5,151.9),(22.4,151.9),
        (22.4,260.7),(107.5,260.7),(106.7,387.1),(22.4,387.1),(22.4,489.8),
        (103.3,489.8),(101.6,618.9),(221.8,618.9),(225.2,488.1),(350.2,488.9),
        (350,618.9),(467.4,618.9),(467.4,486.4),(584,483.8),(584,383.4),(464.8,381.7),
        (464.8,253),(584,250.5),(584,154.5),(460.6,151.9),(461.4,22.4),(343.3,22.4),
        (344.1,151.9),(226.3,151.9),(226.3,22.4)])
        buchstabe.append([(349.1,253.6),(226.4,252.5),(227.4,385.7),
        (346.7,382.3),(349.1,253.6)])
    ausgabeAxi = []
    for sign in buchstabe:
        axiready = bigChar([sign],h,x,y)
        ausgabeAxi.append(axiready)
    return ausgabeAxi


def smallChars(letter,h,x,y):
    buchstabe = []
    if letter =="A" or letter == "a":
        buchstabe.append([(96.5,566.9),(299,91.9),(525,566.9)])
        buchstabe.append([(425,327.4),(296,332.4),(176,329.4)])
    if letter == "B" or letter == "b":
        buchstabe.append([(145,566.9),(136,91.9),(389,91.9),(446,118.9),
        (491,160.9),(498,186.9),(498,229.9),(491,275.9),(470,308.9),(412,329.4),
        (300.5,345.9),(147,345.9),(317,349.9),(425,360.9),(471,381.9),(516,431.9),
        (525,465.9),(525,499.9),(517,536.9),(486,566.9),(434,582.9),(330.5,582.9),
        (145,566.9)])
    if letter == "C" or letter == "c":
        buchstabe.append([(520,124.9),(418,97.9),(259,86.9),(137.5,169.9),(116,391.9),
        (136,499.9),(209,572.4),(330.5,588.9),(464,566.9),(534,509.9)])
    if letter == "D" or letter == "d":
        buchstabe.append([(116,100.9),(125,566.9),(398,566.9),(470,524.9),(525,404.9),
        (534,250.9),(469.6,150.6),(310.8,91.9),(116,100.9)])
    if letter == "E" or letter == "e":
        buchstabe.append([(493,91.9),(105,91.9),(111,582.9),(473,588.9)])
        buchstabe.append([(91,332.4),(262,340.4),(320,336.4)])
    if letter == "F" or letter == "f":
        buchstabe.append([(486,86.9),(129,86.9),(136,582.9)])
        buchstabe.append([(96.5,320),(219,320),(286,327.4)])
    if letter == "G" or letter == "g":
        buchstabe.append([(493,138.9),(330.5,81.9),(205.5,102.9),(129,185.9),
        (105,376.9),(123.6,491.9),(191.2,570.9),(320,587.5),(449,559.9),(486,516.9),
        (468,409.9),(299,378.9),(286,408.9),(300.5,367.9),(477,413.9),(500,566.9)])
    if letter == "H" or letter == "h":
        buchstabe.append([(101,587.5),(96.5,81.9),(91,337.9),(447,336.4),(454,71.9),(460,582.9)])
    if letter == "I" or letter == "i":
        buchstabe.append([(391,76.9),(221,76.9),(300.5,81.9),(306,575.9),(186,587.5),(417,588.9)])
    if letter == "J" or letter == "j":
        buchstabe.append([(136,76.9),(471,71.9),(486,370.9),(486,528.9),(455.7,568.3),
        (402,594.9),(300.5,598.9),(217,598.9),(169.3,569)])
    if letter == "K" or letter == "k":
        buchstabe.append([(153,62.9),(148,588.9),(158,307.9),(398.9,105.9),(224.6,266.3),(387.1,587.5)])
    if letter == "L" or letter == "l":
        buchstabe.append([(129,62.9),(122,575.9),(451,582.9),(486,545.9)])
    if letter == "M" or letter == "m":
        buchstabe.append([(91,588.9),(205.5,66.9),(307.5,323.7),(452,66.9),(525,588.9)])
    if letter == "N" or letter == "n":
        buchstabe.append([(111,588.9),(111,81.9),(481,582.9),(493,66.9)])
    if letter == "O" or letter == "o":
        buchstabe.append([(344,62.9),(182,66.9),(105,193.9),(91,379.9),(109.9,493.9),
        (169.3,569),(273.5,588.9),(363,588.9),(449,559.9),(511,488.8),(539,332.9),
        (518,149.9),(398.9,62.9),(344,62.9)])
    if letter == "P" or letter == "p":
        buchstabe.append([(122,588.9),(116,76.9),(330.5,71.9),(441.2,116.6),(498,194.8),
        (498,266.9),(447,336.4),(389,340.4),(201,345.9),(111,340.4)])
    if letter == "Q" or letter == "q":
        buchstabe.append([(514,169.9),(443.6,81.9),(310.8,62.9),(152.8,81.9),(91,246.9),
        (91,411.9),(116,521.1),(217,598.9),(402,594.9),(468,538),(273.5,320),(525,588.9),
        (479.2,524.8),(525,436.9),(539,261.9),(514,169.9)])
    if letter == "R" or letter == "r":
        buchstabe.append([(136,592.9),(116,66.9),(325,52.9),(472.3,96.8),(521.1,196),
        (500,289.9),(421.4,349.2),(319.9,352.9),(237,355.9),(116,360.9),(318.6,362.9),(508,592.9)])
    if letter == "S" or letter == "s":
        buchstabe.append([(539,215.9),(472.9,108.8),(304,66.9),(176,103.9),(111,184),(151.4,226.9),
        (485.7,381.9),(503.5,435.4),(493,509.4),(433.2,579.4),(299,592.9),(197.1,586.4),(136,531.9),
        (105,424.9),(111,381.9)])
    if letter == "T" or letter == "t":
        buchstabe.append([(311,598.9),(310.8,91.9),(76,71.9),(534,71.9)])
    if letter == "U" or letter == "u":
        buchstabe.append([(136,71.9),(111,445.6),(148,520.4),(275.5,585.6),(398.9,582.9),
        (500,501.4),(539,383.9),(534,91.9),(530,62.9)])
    if letter == "V" or letter == "v":
        buchstabe.append([(96.5,62.9),(286,592.9),(425,588.9),(350.4,585.6),(530,62.9)])
    if letter == "W" or letter == "w":
        buchstabe.append([(91,62.9),(191.2,598.9),(305,285.9),(443,592.9),(534,62.9)])
    if letter == "X" or letter == "x":
        buchstabe.append([(96.5,62.9),(521.1,598.9),(303.3,334.9),(96.5,592.9),(525,52.9)])
    if letter == "Y" or letter == "y":
        buchstabe.append([(122,71.9),(106.8,241.9),(325,292.6),(512,62.9),(129,592.9)])
    if letter == "Z" or letter == "z":
        buchstabe.append([(85,81.9),(549,71.9),(101,587.5),(521.1,588.9)])
    if letter == "1":
        buchstabe.append([(176,246.5),(322,63.4),(320,587.5),(393.4,587.5),(256.2,585.6)])
    if letter == "2":
        buchstabe.append([(137.9,193.5),(228.9,84.9),(344,62.9),(467.4,117.7),(460,202.5),
        (133.8,534.8),(129,576),(176,577),(512,577)])
    if letter == "3":
        buchstabe.append([(122,189.5),(191.8,129.2),(364.3,71.9),(486,165.5),(303.2,327.4),
        (479.9,480.4),(486,534.3),(435.2,577),(266,592.9),(136,499.9)])
    if letter == "4":
        buchstabe.append([(166.8,91.9),(98.6,322.9),(493,320),(330.5,325.9),(335.5,73.9),
        (320,587.5),(266,592.9),(361,592.9)])
    if letter == "5":
        buchstabe.append([(500,98.5),(136.2,100),(122,286.5),(198,255.5),(317,243.5),
        (435,286.5),(512,418.5),(465.2,573.3),(320,587.5),(209,572.4),(105,468.5)])
    if letter == "6":
        buchstabe.append([(436,74.3),(214,187.5),(131.1,357.7),(124.8,370.5),(133.8,534.8),
        (266,592.9),(436,564.3),(469,396.5),(352.9,269.8),(186,301.5),(142.8,352.7)])
    if letter == "7":
        buchstabe.append([(135,85.5),(502,85.5),(360,292),(153,592.9),(353.4,283),
        (435,286.5),(238,282.5)])
    if letter == "8":
        buchstabe.append([(176.6,333.4),(307.3,288.7),(178.4,253.5),(131.4,170.2),(179.6,89.8),
        (280.4,55.1),(437.2,82.9),(498.5,186),(446.3,260.9),(330.9,288.3),(455.1,334.6),
        (502,451.5),(456.6,560.2),(328.8,595.8),(172.9,545.2),(124.8,443.2)])
    if letter == "9":
        buchstabe.append([(154,491.5),(201.1,554.3),(291.1,583.6),(441.2,537.6),(502,216.5),
        (432,63.4),(232,55.1),(135,208.5),(209,325.5),(368,343),(493,239.5)])
    if letter == "0":
        buchstabe.append([(520,276.5),(520,156.5),(393.4,61.8),(236,63.4),(135,178.3),
        (118,333.6),(142,516.5),(234,587.5),(407,587.5),(493,513.5),(520,359.5)])
    if letter == ".":
        buchstabe.append([(293.9,357.2),(208.9,410.8),(154.6,476.1),(210.7,555.6),
        (310.9,609.4),(409.9,526.1),(443.4,444.9),(367.7,386.5),(293.9,357.2)])
    if letter == "?":
        buchstabe.append([(105.1,161.6),(170.2,272),(303,133.6),(371.5,193.8),(232.3,447.9),
        (291.7,461.8),(201.2,541.9),(299.1,628.2),(398.2,529.3),(305.2,464.3),
        (381.6,482.9),(502.8,194.1),(419.7,42.6),(237,29.7),(105.1,161.6)])
    if letter == "=":
        buchstabe.append([(93.3,333.9),(71.3,497.1),(583.7,475.8),(573.4,338.1),(107.4,331),
        (579.4,312.9),(584.2,166.1),(44.1,176.2),(71,334.7),(93.3,333.9)])
    if letter == "/":
        buchstabe.append([(396.3,114.7),(257.1,28.7),(36.9,490.7),(149.5,572.5),(392.3,128.5),
        (187.7,554.2),(315.2,627.1),(591.4,83),(438.7,32.7),(396.3,114.7)])
    if letter == ":":
        buchstabe.append([(392.8,356.8),(334.4,333.6),(415.4,265.4),(443.6,197),(379.9,147.9),
        (317.9,123.3),(246.3,168.4),(200.6,223.3),(247.8,290.2),(328.6,333.5),
        (259.3,377.2),(213.6,432.2),(260.8,499),(345.1,544.3),(428.4,474.2),
        (456.6,405.9),(392.8,356.8)])
    if letter == "#":
        buchstabe.append([(226.3,22.4),(107.5,22.4),(107.5,151.9),(22.4,151.9),
        (22.4,260.7),(107.5,260.7),(106.7,387.1),(22.4,387.1),(22.4,489.8),
        (103.3,489.8),(101.6,618.9),(221.8,618.9),(225.2,488.1),(350.2,488.9),
        (350,618.9),(467.4,618.9),(467.4,486.4),(584,483.8),(584,383.4),(464.8,381.7),
        (464.8,253),(584,250.5),(584,154.5),(460.6,151.9),(461.4,22.4),(343.3,22.4),
        (344.1,151.9),(226.3,151.9),(226.3,22.4)])
        buchstabe.append([(349.1,253.6),(226.4,252.5),(227.4,385.7),
        (346.7,382.3),(349.1,253.6)])
    ausgabeAxi = []
    for sign in buchstabe:
        axiready = smallChar([sign],h,x,y)
        ausgabeAxi.append(axiready)
    return ausgabeAxi

#print_bigChars: char,font-height(mm),lines relative to font-height, max chars to plot
def print_bigChars(word,h,line,maxChar):
    plottableWord = []
    XX = 0
    YY = line
    for w in word:
        if(XX <= maxChar):
            for ww in bigChars(w,h,XX,YY):
                plottableWord.append(ww)
        XX += 1
    return plottableWord

#print_smallChars: char,font-height(mm),lines relative to font-height
def print_smallChars(wort,h,line):
    ausgabeWort = []
    XX = 0
    YY = line
    for w in wort:
        for ww in smallChars(w,h,XX,YY):
            ausgabeWort.append(ww)
        XX += 1
    return ausgabeWort

def print_Plotter(image):
    url = "https://www.wedodraw.com/plotter_axi_by_id.php?nr="+str(image)
    result = requests.get(url).json()	#whole json request
    resultat = []
    for pfad in result["CORD"]:		#all the coordinates to plot the lines
        resu = [(piece['x'], piece['y']) for piece in pfad]
        resultat.append(resu)
    resuanz   = result["KLICK"]     	#how many points the drawing consists of
    resuzeit  = result["ZEIT"]      	#how long the drawing took in seconds
    resudat1  = result["DATUM1"]    	#the date the drawing was drawn
    resuauth  = result["AUTHOR"]    	#the author if provided else "Anonymous Artist"
    resutitl  = result["TITLE"]     	#the provided title
    resuavgc  = result["AVGC"]      	#the avarage color as decimal number
    resuname  = result["NAME"]      	#the drawing name (number)
    today     = datetime.now()
    print_date  = ("{:%d%m%Y%H%M}".format(today))
    # uncomment to see the all coordinates in your terminal window
    # print resultat
    print ("Drawing ID: " +str(resuname) +" consists of "+ str(resuanz) + " points")
    print ("PLOT <" + str(resutitl) + "> by " + str(resuauth))
    plot = raw_input("PLOT OR STOP (y/n)")
    if(plot == "y"):
        printer([
            print_rectangle(-10,-41,140,24),
            print_rectangle(-10,-4,140,140)
            ])
        printer(print_logo(90,15,-70))
        printer(print_bigChars(str(resutitl),11,-3,13)) #max 13 char in that size
        printer(print_smallChars("by "+str(resuauth),4,-3.35))
        printer(resultat) #here we plot the drawing itself from left to right
        printer(print_smallChars("#" + str(resuname),4,30))
        printer(print_smallChars("                   " + str(print_date),4,30))

def Plott():
    drawing = raw_input("PLOT DRAWING NR (ID/n to STOP ): ")
    if(drawing == "n"):
        exit()
    else:
        try:
            print_Plotter(drawing)
        except IOError:
            print 'oops!'

    # TEST NUMBER 2913
while(True):
    Plott()
