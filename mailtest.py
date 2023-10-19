import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
import sys
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
from email.mime.base import MIMEBase
from email import encoders

start_time_str=""


if len(sys.argv) > 1:
    start_time_str = sys.argv[1]
    print(start_time_str)

if start_time_str :
    print("O")


video_name="video_"+start_time_str+".mp4"
img_name="img_"+start_time_str+".jpg"

def sendEmail(to_mail):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
    if re.match(reg, to_mail):
        smtp.sendmail(my_account, to_mail, msg.as_string())
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("받으실 메일 주소를 정확히 입력하십시오.")
 
# smpt 서버와 연결
gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
 
# 로그인
my_account = "5128166@gmail.com"
my_password = "dydgns9866!"
smtp.login(my_account, my_password)
 
# 메일을 받을 계정
to_mail = "5128166@gmail.com"

 
# 메일 기본 정보 설정
msg = MIMEMultipart()
msg["Subject"] = f"WA-CHI 알림 테스트"  # 메일 제목
msg["From"] = my_account
msg["To"] = to_mail
 

# # 메일 본문 내용
# content = "안녕하세요. \n\n\
# 데이터를 전달드립니다.\n\n\
# 감사합니다\n\n\
# "
# content_part = MIMEText(content, "plain")
# msg.attach(content_part)


# HTML 이메일 본문 생성
# html = """\
# <html>
#   <body>
#     <h3></h3>
#     <p>이메일에 이미지를 삽입합니다:</p>
#     <img src="cid:image_name">
#     <a href='tel:010-0000-0000'>전화하기</a>
#   </body>
# </html>
# """

with open('mailbody.html', 'r', encoding='utf-8') as html_file:
    html = html_file.read()
msg.attach(MIMEText(html, 'html'))
 
# 이미지 파일을 첨부
with open(video_name, 'rb') as file:
    video = MIMEBase('application', 'octet-stream')
    video.set_payload(file.read())
    encoders.encode_base64(video)
    video.add_header('Content-Disposition', f'attachment; filename="{video_name}"')
    msg.attach(video)

# 이미지 파일 삽입
with open(img_name, 'rb') as file:
    img = MIMEImage(file.read())
    img.add_header('Content-Disposition', 'attachment', filename=img_name)
    img.add_header('Content-ID',"<img_name")
    msg.attach(img)
    
 
# 받는 메일 유효성 검사 거친 후 메일 전송
sendEmail(to_mail)
 
# smtp 서버 연결 해제
smtp.quit()