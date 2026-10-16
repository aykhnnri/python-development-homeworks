from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, Preformatted
from xml.sax.saxutils import escape
import re, os

OUT = 'lesson_13/Lesson_13_Homework.pdf'
os.makedirs('lesson_13', exist_ok=True)
FONT_DIR = '/usr/share/fonts/truetype/dejavu'
pdfmetrics.registerFont(TTFont('DejaVu', os.path.join(FONT_DIR, 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuBold', os.path.join(FONT_DIR, 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuMono', os.path.join(FONT_DIR, 'DejaVuSansMono.ttf')))
PAGE_W, PAGE_H = A4
LEFT = 58; RIGHT = 58; TOP = 55; BOTTOM = 53
styles = {
    'title': ParagraphStyle('title', fontName='DejaVuBold', fontSize=22, leading=26, spaceAfter=15, textColor=colors.black),
    'subtitle': ParagraphStyle('subtitle', fontName='DejaVuBold', fontSize=12, leading=15, spaceAfter=17),
    'h1': ParagraphStyle('h1', fontName='DejaVuBold', fontSize=15, leading=18, spaceBefore=10, spaceAfter=14),
    'h2': ParagraphStyle('h2', fontName='DejaVuBold', fontSize=12, leading=15, spaceBefore=9, spaceAfter=10),
    'h3': ParagraphStyle('h3', fontName='DejaVuBold', fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=7),
    'body': ParagraphStyle('body', fontName='DejaVu', fontSize=10, leading=14.5, spaceAfter=9),
    'body_tight': ParagraphStyle('body_tight', fontName='DejaVu', fontSize=10, leading=14.5, spaceAfter=5),
    'bullet': ParagraphStyle('bullet', fontName='DejaVu', fontSize=10, leading=13.8, leftIndent=12, firstLineIndent=-7, spaceAfter=4),
    'number': ParagraphStyle('number', fontName='DejaVu', fontSize=10, leading=14.2, leftIndent=16, firstLineIndent=-13, spaceAfter=4),
}
INLINE_CODE_RE = re.compile(r'`([^`]+)`'); BOLD_RE = re.compile(r'\*\*([^*]+)\*\*')
def inline(text):
    text = escape(text); text = BOLD_RE.sub(r'<b>\1</b>', text); return INLINE_CODE_RE.sub(r'<font name="DejaVuMono">\1</font>', text)
def P(text, style='body'): return Paragraph(inline(text), styles[style])
def H1(text): return Paragraph(inline(text), styles['h1'])
def H2(text): return Paragraph(inline(text), styles['h2'])
def H3(text): return Paragraph(inline(text), styles['h3'])
def code(text):
    pre = Preformatted(text.strip('\n'), ParagraphStyle('code', fontName='DejaVuMono', fontSize=8.4, leading=11.7))
    t = Table([[pre]], colWidths=[PAGE_W - LEFT - RIGHT], hAlign='LEFT')
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.6,colors.HexColor('#4A4A4A')),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return [t, Spacer(1,9)]
def bullet(text): return Paragraph('• ' + inline(text), styles['bullet'])
def num_item(n,text): return Paragraph(f'{n}. ' + inline(text), styles['number'])
def header_footer(canvas, doc):
    canvas.saveState(); canvas.setFont('DejaVuBold',8); canvas.drawString(52,PAGE_H-29,'HIGH CODE  |  PYTHON BACKEND DEVELOPMENT')
    canvas.setStrokeColor(colors.HexColor('#555555')); canvas.setLineWidth(0.45); canvas.line(52,44,PAGE_W-52,44)
    canvas.setFont('DejaVu',8); canvas.drawString(52,29,'Lesson 13 - Homework'); canvas.drawRightString(PAGE_W-52,29,str(doc.page)); canvas.restoreState()
doc = BaseDocTemplate(OUT,pagesize=A4,leftMargin=LEFT,rightMargin=RIGHT,topMargin=TOP,bottomMargin=BOTTOM,title='Lesson 13 - Homework',author='High Code')
frame = Frame(LEFT,BOTTOM,PAGE_W-LEFT-RIGHT,PAGE_H-TOP-BOTTOM,id='main')
doc.addPageTemplates([PageTemplate(id='homework',frames=[frame],onPage=header_footer)])
story=[]
story += [Paragraph('Lesson 13 - Homework',styles['title']), Paragraph('Error Handling - Xətaların idarə olunması',styles['subtitle']), H1('Mövzu xatırlatmaları')]
story += [P('Python proqramında xəta baş verdikdə proqramın tamamilə dayanmasının qarşısını almaq üçün `try / except` istifadə edə bilərik.'), H3('Əsas struktur')]
story += code('''try:\n    # Xəta yarada biləcək kod\n\nexcept ValueError:\n    # ValueError baş verdikdə işləyəcək kod''')
story += [H2('`try`'),P('Xəta yarana biləcək kod `try` daxilində yazılır.')]; story += code('''try:\n    yas = int(input("Yaşınızı daxil edin: "))''')
story += [H2('`except`'),P('Xəta baş verdikdə proqramın nə etməli olduğunu müəyyən edir.')]; story += code('''try:\n    yas = int(input("Yaşınızı daxil edin: "))\n\nexcept ValueError:\n    print("Yaş rəqəm olmalıdır.")''')
story += [P('Mümkün qədər:','body_tight')]; story += code('''except:'''); story += [P('əvəzinə konkret exception yazmağa çalışın:','body_tight')]; story += code('''except ValueError:''')
story += [H2('Bir neçə `except`'),P('Bir `try` blokunda fərqli xətaları ayrıca idarə edə bilərik.')]; story += code('''try:\n    reqem1 = int(input("Birinci rəqəm: "))\n    reqem2 = int(input("İkinci rəqəm: "))\n\n    netice = reqem1 / reqem2\n\nexcept ValueError:\n    print("Yalnız rəqəm daxil edin.")\n\nexcept ZeroDivisionError:\n    print("Sıfıra bölmək olmaz.")''')
story += [H2('`else`'),P('`try` daxilində heç bir xəta baş verməzsə `else` işləyir.')]; story += code('''try:\n    yas = int(input("Yaş: "))\n\nexcept ValueError:\n    print("Yanlış məlumat.")\n\nelse:\n    print("Məlumat uğurla qəbul edildi.")''')
story += [H2('`finally`'),P('`finally` xəta olsa da, olmasa da işləyir.')]; story += code('''try:\n    yas = int(input("Yaş: "))\n\nexcept ValueError:\n    print("Yanlış məlumat.")\n\nfinally:\n    print("Əməliyyat tamamlandı.")''')
story += [H2('`raise`'),P('Bəzən Python özü xəta yaratmır, amma daxil edilən məlumat bizim proqramın qaydalarına uyğun olmur.'),P('Bu zaman özümüz exception yarada bilərik.')]; story += code('''yas = int(input("Yaş: "))\n\nif yas < 0:\n    raise ValueError("Yaş mənfi ola bilməz.")''')
story += [H2('Exception mesajını əldə etmək')]; story += code('''try:\n    yas = int(input("Yaş: "))\n\nexcept ValueError as xeta:\n    print(f"Xəta: {xeta}")''')
story += [H2('File Operations ilə birlikdə')]; story += code('''try:\n    with open("users.txt", "r", encoding="utf-8") as fayl:\n        melumat = fayl.read()\n\nexcept FileNotFoundError:\n    print("Fayl tapılmadı.")''')
story += [H1('Tapşırıq - Mağaza sifariş sistemi'),P('Bu homework boyunca **eyni proqram üzərində işləyəcəksiniz**.'),P('Hər yeni mərhələdə əvvəlki kodunuzu silməyin.'),P('Əvvəlki tapşırıqda yazdığınız proqramı inkişaf etdirin və yeni funksionallıq əlavə edin.'),P('Başlanğıc məhsullarımız:')]
story += code('''mehsullar = {\n    "laptop": 1800,\n    "telefon": 1200,\n    "monitor": 500,\n    "mouse": 50\n}''')
story += [H2('Mərhələ 1 - Məhsul və miqdarın alınması'),P('İlk olaraq sadə sifariş proqramı yaradın.'),P('İstifadəçidən:')]; story += code('''Məhsul:\nMiqdar:'''); story += [P('məlumatlarını alın.'),P('Məhsulun qiymətini `mehsullar` dictionary-sindən əldə edin.'),P('Sonra ümumi qiyməti hesablayın:')]; story += code('''ümumi qiymət = məhsulun qiyməti × miqdar'''); story += [P('Məsələn:')]; story += code('''Məhsul: monitor\nMiqdar: 2\n\nMəhsul: monitor\nMiqdar: 2\nÜmumi qiymət: 1000 AZN'''); story += [H3('Bu mərhələdə'),P('Hələ error handling əlavə etməyin.'),P('Əvvəlcə normal işləyən proqram yaradın.')]
story += [H2('Mərhələ 2 - Miqdar üçün `ValueError`'),P('İndi əvvəlki proqramınızı inkişaf etdirin.'),P('Hazırda istifadəçi belə bir məlumat daxil etsə:')]; story += code('''Miqdar: iki'''); story += [P('proqram xəta verəcək.'),P('Miqdarı `try / except` daxilində `int` tipinə çevirməyə çalışın.'),P('Əgər istifadəçi rəqəm əvəzinə mətn daxil edərsə:')]; story += code('''Miqdar rəqəm olmalıdır.'''); story += [P('mesajı göstərilməlidir.'),H3('İstifadə edin')]; story += code('''try\nexcept ValueError'''); story += [H3('Test edin')]; story += code('''Məhsul: monitor\nMiqdar: iki'''); story += [P('Proqram crash etməməlidir.')]
story += [H2('Mərhələ 3 - Miqdarın düzgünlüyünün yoxlanılması'),P('İndi proqram başqa bir problem yaşayır.'),P('İstifadəçi:')]; story += code('''Miqdar: -3'''); story += [P('yaza bilər.'),P('Python üçün `-3` düzgün integer-dir, ona görə `ValueError` avtomatik yaranmayacaq.'),P('Amma bizim mağazamız üçün mənfi miqdar düzgün deyil.'),P('Əgər miqdar `0` və ya mənfidirsə özünüz exception yaradın.')]; story += code('''raise ValueError(...)'''); story += [P('Mesaj:')]; story += code('''Miqdar 0-dan böyük olmalıdır.'''); story += [H3('Test 1')]; story += code('''Məhsul: monitor\nMiqdar: -2'''); story += [H3('Test 2')]; story += code('''Məhsul: monitor\nMiqdar: 0'''); story += [P('Hər iki halda proqram sifariş yaratmamalıdır.')]
story += [H2('Mərhələ 4 - Mövcud olmayan məhsul'),P('İndi məhsul hissəsini də təhlükəsiz edin.'),P('Hazırda istifadəçi:')]; story += code('''Məhsul: televizor'''); story += [P('yazarsa, dictionary-də belə key olmadığı üçün proqram:')]; story += code('''KeyError'''); story += [P('verəcək.'),P('Bu xətanı idarə edin.'),P('Məhsulu belə əldə etməyə çalışın:')]; story += code('''qiymet = mehsullar[mehsul]'''); story += [P('və `KeyError` baş verdikdə:')]; story += code('''Belə məhsul mövcud deyil.'''); story += [P('göstərin.'),H3('Şərt'),P('Bu mərhələdə:')]; story += code('''mehsullar.get(...)'''); story += [P('istifadə etməyin.'),P('Məqsəd `KeyError` exception-unu idarə etməkdir.'),H3('Test')]; story += code('''Məhsul: televizor\nMiqdar: 2'''); story += [P('Nəticə:')]; story += code('''Belə məhsul mövcud deyil.''')
story += [H2('Mərhələ 5 - Bir neçə exception-un idarə olunması'),P('Artıq proqramda ən azı iki fərqli xəta yarana bilər:')]; story += code('''ValueError\nKeyError'''); story += [P('Kodunuzu elə qurun ki, bunların hər biri ayrıca idarə olunsun.'),P('Struktur təxminən belə olmalıdır:')]; story += code('''try:\n    # məhsulun tapılması\n    # miqdarın alınması\n    # yoxlamalar\n    # qiymətin hesablanması\n\nexcept KeyError:\n    # məhsul tapılmadıqda\n\nexcept ValueError as xeta:\n    # miqdar düzgün olmadıqda'''); story += [H3('Test 1')]; story += code('''Məhsul: televizor\nMiqdar: 2'''); story += [H3('Test 2')]; story += code('''Məhsul: monitor\nMiqdar: üç'''); story += [H3('Test 3')]; story += code('''Məhsul: monitor\nMiqdar: -4'''); story += [H3('Test 4')]; story += code('''Məhsul: monitor\nMiqdar: 3'''); story += [P('Dörd fərqli vəziyyətdə proqram düzgün davranmalıdır.')]
story += [H2('Mərhələ 6 - `else` əlavə edin'),P('İndi uğurlu sifariş mesajını `try` blokunun içində göstərməyin.'),P('Bunun üçün `else` istifadə edin.'),P('Əgər heç bir exception baş verməzsə:')]; story += code('''Sifariş uğurla yaradıldı.\n\nMəhsul: monitor\nMiqdar: 2\nÜmumi qiymət: 1000 AZN'''); story += [P('göstərilməlidir.'),H3('Məqsəd'),P('Flow belə olmalıdır:')]; story += code('''Xəta var → except\n\nXəta yoxdur → else''')
story += [H2('Mərhələ 7 - Sifarişi fayla yazın'),P('İndi əvvəlki proqramınızı bir az da inkişaf etdirin.'),P('Sifariş uğurla yaradıldıqda məlumatı:')]; story += code('''orders.txt'''); story += [P('faylına yazın.'),P('Append mode istifadə edin:')]; story += code('''"a"'''); story += [P('Format:')]; story += code('''monitor,2,1000\nmouse,3,150\nlaptop,1,1800'''); story += [P('Hər yeni sifariş yeni sətirdə olmalıdır.'),H3('Nümunə'),P('İstifadəçi:')]; story += code('''Məhsul: mouse\nMiqdar: 3'''); story += [P('daxil edirsə, fayla:')]; story += code('''mouse,3,150'''); story += [P('əlavə olunmalıdır.'),H3('Vacib'),P('Səhv məlumat daxil edilərsə fayla heç nə yazılmamalıdır.')]
story += [H2('Mərhələ 8 - Sifariş tarixçəsini göstərmək'),P('İndi proqramın sonuna yeni hissə əlavə edin.'),P('Sifariş yaradıldıqdan sonra:')]; story += code('''orders.txt'''); story += [P('faylını oxuyun və bütün əvvəlki sifarişləri göstərin.'),P('Məsələn:')]; story += code('''--- Sifariş tarixçəsi ---\n\nmonitor,2,1000\nmouse,3,150\nlaptop,1,1800'''); story += [P('Amma bir problem var.'),P('Əgər proqram ilk dəfə işləyirsə və:')]; story += code('''orders.txt'''); story += [P('hələ mövcud deyilsə, proqram `FileNotFoundError` verə bilər.'),P('Bu xətanı da idarə edin.'),P('Mesaj:')]; story += code('''Hələ heç bir sifariş tarixçəsi yoxdur.'''); story += [H3('İstifadə edin')]; story += code('''except FileNotFoundError:''')
story += [H2('Mərhələ 9 - `finally` əlavə edin'),P('Proqramın əsas sifariş əməliyyatının sonunda `finally` istifadə edin.'),P('Sifariş uğurlu olsa da, xəta baş versə də:')]; story += code('''Sifariş əməliyyatı tamamlandı.'''); story += [P('mesajı göstərilməlidir.'),H3('Xatırlatma'),P('`finally`:'),bullet('xəta olduqda işləyir;'),bullet('xəta olmadıqda da işləyir.')]
story += [H1('Final nəticə'),P('Homework-un sonunda proqramınız aşağıdakı işləri bacarmalıdır:')]
final_items=['İstifadəçidən məhsul adı alır.','Məhsulu dictionary-də axtarır.','Mövcud olmayan məhsulu `KeyError` ilə idarə edir.','Miqdarı istifadəçidən alır.','Miqdar rəqəm deyilsə `ValueError` idarə edir.','Miqdar `0` və ya mənfidirsə `raise` istifadə edir.','Ümumi qiyməti hesablayır.','Uğurlu nəticəni `else` daxilində göstərir.','Sifarişi `orders.txt` faylına əlavə edir.','Sifariş tarixçəsini fayldan oxuyur.','Fayl mövcud deyilsə `FileNotFoundError` idarə edir.','`finally` istifadə edərək əməliyyatın bitdiyini göstərir.']
for i,t in enumerate(final_items,1): story.append(num_item(i,t))
doc.build(story)
print(OUT)
