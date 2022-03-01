#https://jjanggu1612.tistory.com/
#구글 웹드라이버를 사용하기 위한 추가구문
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import sys, os #exe 파일로 만들 때 필요한 코드

#exe 파일로 만들 때 필요한 코드 pyinstaller를 이용하면 가능하다.
#if  getattr(sys, 'frozen', False): 
#    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
#    driver = webdriver.Chrome(chromedriver_path)
#else:
#    driver = webdriver.Chrome('D:/chromedriver.exe')

#구글웹드라이버를 실행을 시킨후 해당사이트의 로그인페이지에 접속합니다.
browser = webdriver.Chrome('D:/chromedriver')
#browser = driver
browser.get('https://chicor.com/login?returnUrl=/mypage/mymain')
browser.implicitly_wait(3)

# 자동로그인을 하기 위한 사이트의 ID, 패스워드 속성값을 적습니다. 
# 접속하기 위한 사이트의 아이디, 패스워드를 적습니다.
browser.find_element_by_id('lginId').send_keys('아이디')
browser.find_element_by_id('lginPw').send_keys('패스워드')

# 로그인 버튼을 눌러주자.
browser.find_element_by_xpath('//*[@onclick="intgLogin();"]').click()

# 출석체크로 넘어간다 
browser.refresh()
browser.get('https://chicor.com/event/784')

# 출석체크를 한다 
try:
    #browser.find_element_by_xpath('//*[@onclick="anttendanceCheck()"]').find_element_by_xpath('..').click()
	browser.find_element_by_xpath('//*[@onclick="atdEvnt();"]').click()
	#출첵이 하루에 한번이라 작동되는지 내일 확인해 봐야한다
    #확인해 보니 잘 되니 그냥 쓰면 된다
except Exception:
    print("you already check!") #이미 출석체크 했으면 콘솔창에 문자열이 나타난다

#browser.implicitly_wait(30) #30초 대기라긴하는데 이놈이 안기다림

#크롬드라이버를 닫는다.
browser.quit()