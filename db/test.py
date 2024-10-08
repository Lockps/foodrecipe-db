import emoji
import re

# Sample input data
data = """
recipe_23840390: หมูซีอิ๊ว
หมูสันคอ•น้ำมันหอย•ซีอิ๊วขาว•ซีอิ๊วหวาน•ดอกเกลือ
30 นาที 1 เสิร์ฟ
รัตน์ (Rat Sri)
recipe_23926544: สุกี้หมูแห้ง
หมูชิ้น•น้ำจิ้มสุกี้ที่ชื่นชอบ•ผักกาดขาว•ผักบุ้ง•ขึ้นฉ่าย•วุ้นเส้น•ไข่ไก่•พริกสด•กระเทียม•น้ำมัน•น้ำมันหอย•ผงปรุงรส
ArWarai
recipe_23924407: คั่วกลิ้งหมูชิ้นใส่เห็ด
หมูสันนอก•ก้านเห็ดชิเมจิ หั่นชิ้นเล็กๆ•พริกแกงคั่วกลิ้ง•กะปิ•ใบมะกรูดซอย•ข่าอ่อนหั่นแว่นบางๆ•ตะไคร้ซอย•กระเทียมจีนซอย•น้ำตาล
20 นาที 2 เสิร์ฟ
Paipai
recipe_23895787: ยำหมูย่าง
สันในหมู•น้ำยำ•ตะไคร้
40 นาที 2 คน
Paipai
recipe_23883081: “หมูทอดเสียบไม้”
หมูหั่นชิ้น•มันแข็งหั่นชิ้น•น้ำตาลปี๊บ•ผงปรุงรส•เบกกิ้งโซดา•พริกไทยป่น•เกลือ•กระเทียมตำ•รากผักชีตำ•น้ำมันหอย•น้ำมันงา•ซีอิ๊วขาว
1 ชั่วโมง ทั้งครอบครัว
ImAiw Wattanakorn
recipe_16455206: หมูผัดเห็ด
เนื้อหมู•เห็ดชิเมจิ•เห็ดหูหนู•ยอดฟักแม้ว•หอมใหญ่ซอย•พริกจินดาซอย•น้ำมันหอย•ซอสปรุงรส•ซีอิ๊วขาว•น้ำมันงา•น้ำมันพืช
รัตน์ (Rat Sri)
recipe_22672607: ข้าวกล่องเมนูเด็ก ผัดผักบุ้ง หมูทอดน้ำปลา ไข่ต้ม
หมูสันในหั่นชิ้น•ผักบุ้ง•กระเทียม•น้ำมันหอย•น้ำปลา•น้ำตาล•น้ำปลา•น้ำตาล•ไข่ต้ม•ข้าวสวย•ผลไม้ตามชอบ
40 นาที 1 คน
Paipai
recipe_22661278: หมูสันนอกหมักข้าวคั่วทอดกรอบ🌶️🧄
หมูสันนอก 1 ก้อน + แป้งโกกิ สำหรับชุบก่อนทอด•ข้าวคั่ว 1 ช้อนโต๊ะ + พริกป่น 2 ช้อนชา•น้ำมันรำข้าว•น้ำตาลทราย•ซีอิ๊วดำ•เกลือ 1 ช้อนชา + ซีอิ๊วขาว+ น้ำปลา 2 ช้อนโต๊ะ•ไข่ 4 ใบ + ชะอม 2 กำ + ซีอิ๊วขาว และแป้งทอดกรอบ 1 ช้อนโต๊ะ
30 นาที 2 ที่
Boon🥬
recipe_22659124: ผัด พริกเเกง หมู
หมู หั่นชิ้น•พริกเเกง 1 ซ้อนโต๊ะ•ข่า ครึ่งชีก•ตะไคร้•ใบมะกรูด หั่นฝอย•น้ำปลา 1 ซ้อน โต๊ะ•ชูรส 1 ซ้อนชา•รสดี 1 ซ้อนชา•น้ำตาล ครึ่ง ซ้อนชา
25นาที
Terappat Pimsamantitikun
recipe_16673333: หมูผัดหอมใหญ่
หมูชิ้น•หอมใหญ่ซอย•โชยุ•มิริน•สาเก•เกลือ•เนย
รัตน์ (Rat Sri)
recipe_22614173: แกงป่าหมูกับปลาหมูจิ๋วๆทอดสมุนไพร🧄🐽🫚🌶️
เนื้อหมูสันใน 1 เส้นเล็ก•ผักที่ชอบ ข้าวโพดอ่อน มะเขือเปราะ เห็ดขอน•ผักเครื่องปรุง กระชาย ใบมะกรูด ยี่หร่า และกระเพรา พริกจินดา•ผิวมะกรูด•ตะไคร้•หอมแดง 10 หัว + กระเทียม 1 หัว•ขมิ้นสด ยาวข่ามะแขว่นกะชายถั่วเน่าย่างปลาแห้งย่าง
30 นาที 2 ที่
Boon🥬
recipe_22612824: มาม่าผัดซอสแพนงหมู
เนื้อหมูสันในหั่นชิ้น•เส้นมาม่าลวกแล้ว•น้ำกะทิ•ใบมะกรูดหั่นฝอย•น้ำปลา•พริกแกงแพนง•น้ำตาลปี๊บ
10 นาที 1 คน
Rak Chantang
recipe_22601850: บะหมี่ผักผัดหมูสไลซ์
หมูสไลซ์•บะหมี่ผักโมโรเฮยะ 2 ก้อน หรือจะใช้มาม่าก็ได้•ผักคะน้า•ผักกวางตุ้ง•กะหล่ำปลี•กระเทียม•เห็ดหอม•น้ำมันพืช•ซีอิ๊วขาว•น้ำมันหอย•น้ำตาล•น้ำมันหอย
25 นาที 2 คน
Paipai
recipe_22598798: น้ำพริกข่า กวางตุ้ง ผักกาดขาวลวก ทานคู่หมูอบ🫚🧄🌶️
เนื้อหมูสันใน เส้นเล็ก•ผักชีพร้อมราก•พริกไทย 15 เม็ด+ เกลือ 1/4 ช้อนชา•กระเทียม 3 กลีบ+ ตะไคร้ 1/2 ต้น + น้ำตาล 2 ช้อนชา + ซีอิ๊ว 1/2 ช้อนโต๊ะ + น้ำมันงา 2 ช้อนชา + น้ำตาล 1 ช้อนชา•ข่า 3 แว่น ตะไคร้ 1 ต้นกระเทียมจีน 1 หัว หอมแดง 5 หัวพริกแห้งมะแขว่นน้ำมะขามเปียก 3 ช้อนโต๊ะ + มะนาว2 ซีกน้ำตาลทรายเกลือ 1/2 ช้อนชา + น้ำปลานิดหน่อยกวางตุ้ง ผักกาดขาว กระเจี๊ยบ
30 นาที 2 ที่
Boon🥬
recipe_17290776: หมูม้วนกะหล่ำปลี
หมูสไลด์•กะหล่ำปลีหั่นฝอย•เกลือ พริกไทยบด•น้ำมันพืช•โชยุ•มิริน,สาเก อย่างละ•แป้งสาลี•น้ำ
จินนี่ (Jinny)
recipe_17172721: มักกะโรนีข้องอ หมูก้อน
หมูก้อน•มักกะโรนีข้องอ•ผักกวางตุ้งไต้หวัน•ดอกเกลือ
รัตน์ (Rat Sri)
recipe_22581248: ผักตำลึงใส่หมู
หมู•ตำลึง 1 กำใหญ่•กระเทียมใหญ่•ไข่ไก่ใหญ่•ซอสปรุงรส•ซอสหอย
1 ชม 1 เสิร์ฟ
apple
recipe_22573593: ผัดไวไวใส่หมู
เนื้อหมู•ไวไว•ซอสฝาเขียว•คะน้า•ใบกะเพรา•กระเทียมไทย•ไข่ไก่
1 ชม 2 เสิร์ฟ
apple
recipe_22572669: ยำวุ้นเส้นหมูย่างมะเขือยาวย่าง🧄🌶️
หมูสันใน 1 เส้นเล็ก•วุ้นเส้น•มะเขือยาวย่าง•หอมแดง•กระเทียมจีน•พริกจินดาแดง•มะนาว•น้ำปลา•น้ำตาล•ถั่วลิสงคั่ว•ไข่ต้ม
30 นาที 2 ที่
Boon🥬
recipe_22553553: หมูกะปิพริกแกงใต้
หมูสันนอกหั่นเต๋า•กะปิ•พริกแกงไต้•น้ำตาลทราย•ผงชูรส•ใบมะกรูด•พริกลูกโดด•น้ำเปล่า
35นาที 4คน
H Luxdee Thailand
recipe_16780881: Katsu-Don (ข้าวหน้าหมูทอด)
หมู 2 ชิ้นๆ ละ 120 กรัม•เกลือ พริกไทยบด•แป้งข้าวโพด พอควร•ขนมปังป่นพรมน้ำนิดนึง พอควร•น้ำมันพืชใช้ทอด พอควร•หอมใหญ่•น้ำสะอาด•ไข่•โชยุ มิริน สาเก อย่างละ•น้ำตาลทราย
จินนี่ (Jinny)
recipe_17313891: หมูทอด
หมู•กระเทียมไทย•แป้งมัน•ซอสหอย•ซอสฝาเขียว•พริกไทยป่น•แป้งข้าวโพด
50 นาที 1 เสิร์ฟ
apple
recipe_17300199: แกงเผ็ดหมู
หมู•น้ำปลา•กะทิกล่อง 1 250มล•ผงปรุง•ใบโหระพา•พริกแกงเผ็ด•มะเขือเปราะ•ใบมะกรูด
1 ชม 1 เสิร์ฟ
apple
recipe_17284851: ผัดกระเพราหมู
หมูติดมัน•กระเทียม 10 เม็ดไทย•ผงปรุงรส•น้ำปลา•ซีอิ๊วขาว•ใบกะเพรา•หอมใหญ่•พริกสด
1 ชม 1 เสิร์ฟ
apple
recipe_17280707: เส้นหมี่หมูย่างตะไคร้🌶️🧄น้ำจิ้มข้าวคั่วโหระพากระชาย🫚
หมูสันใน•หมี่ขาว•ตะไคร้•มะแขว่น•กระเทียม•เกลือ•ซีอิ๊วขาว•น้ำตาลทราย•แป้งข้าวโพด•โหระพา 1 ช้อนโต๊ะ + ผักชีลาว ผักชีฝรั่งเล็กน้อย•กระชาย•น้ำมะนาว
30 นาที 2 ที่
Boon🥬
recipe_17271987: แกงอ่อมหมูใส่ผักหวาน
หมูชิ้น•ผักชีลาว
30 นาที 3 ที่
Emon Hannok
recipe_17268527: หมูตงพอ (สูตรดัดแปลง)
หมู 1 กก. (หมูติดมัน หรือเนื้อก็ได้)•น้ำตาลปี๊บ•อู่เซียงเฝิ่น 1/8 ถ้วยตวง (ผงเครื่องเทศจีน คล้ายๆ ผงพะโล้ ถ้าไม่มีก็ใช้ผงพะโล้ได้)•น้ำเปล่า•ซีอิ๊วดำหวาน 1 ถ้วยตวง•ซีอิ๊วขาว 0.5 ถ้วยตวง•พริกไทยดำ 1 ช้อนชา•ขิงแก่แป้งข้าวโพด 1-2 ช้อนโต๊ะผักชีและหอมเจียวสำหรับแต่งหน้า
1.5 ชั่วโมง 4 คน
ครุฑดำ
recipe_17266615: ก้อยมะกอกหมูทอดกรอบ(สูตรหมักมะแขว่น)🌶️🧄🥭
หมูสันใน•มะกอกสุก•ผักชีฝรั่ง ต้นหอม ผักชี หอมแดง กระเทียมซอย 1/2 ถ้วย (หอมแดง 5 หัว + กระเทียม 3 กลีบ)•ขิงซอย 1 แง่งเล็ก +เนื้อมะม่วงเบาลูกจิ๋ว 3 ลูก•ข่าสับ + รากผักชี•น้ำปลา•เกลือ•น้ำตาลอ้อยพริกป่นเองข้าวคั่วใหม่น้ำซีอิ๊วเกลือ
30 นาที 2 ที่
Boon🥬
recipe_17262861: ผัดพริกแกงหมูหน่อไม้ใส่เต้าหู้
หมู•เต้าหู้•หน่อไม้•กระเทียมไทย•พริกแกงเผ็ด•ผงปรุง•น้ำปลา•ซีอิ๊วขาว
1 ชม 1 เสิร์ฟ
apple
recipe_17261930: พล่าหมูย่างกับผักน้ำและโทงเทง🌶️🧄
หมูสันนอก•น้ำมันรำข้าว สำหรับน่างหมูในกะทะ•ซีอิ๊วขาว•เกลือ•ซีอิ๊วดำ•น้ำตาลปี๊บ•แป้งข้าวโพด•กระเทียม พริกไทย รากผักชี•น้ำยำพล่า•พริกขี้หนู•น้ำมะนาว 2 ลูก และ น้ำมะขามเปียก 1 ช้อนโต๊ะน้ำปลา
20 นาที 2 ที่
Boon🥬

"""


def remove_emoji(text):
    return emoji.replace_emoji(text, replace='')


# Split the data into individual recipes
recipes = re.split(r'\n(?=recipe_\d+:)', data.strip())

# Extract the first and second lines from each recipe and remove emojis
extracted_lines = []
for recipe in recipes:
    lines = recipe.split('\n')
    if len(lines) >= 2:
        recipe_id = remove_emoji(lines[0])
        ingredients = remove_emoji(lines[1])
        extracted_lines.append((recipe_id, ingredients))

# Write the extracted lines to a file
with open("./db/extracted_recipes.txt", "a", encoding='utf-8') as file:
    for recipe_id, ingredients in extracted_lines:
        file.write(f"{recipe_id}\n{ingredients}\n\n")

print("Extraction complete. Data written to extracted_recipes.txt.")
