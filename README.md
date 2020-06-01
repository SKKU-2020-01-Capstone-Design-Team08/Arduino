## Arduino    

Arduino code for the project 'Snoot'

GPS 모듈 사용법.
1. TinyGPS++ module 을 인터넷에서 다운받아서 Arduino 폴더 내에 있는 Libraries 폴더에 넣어둔다.
2. 압축 폴더를 받게 되면 압축을 풀고 이름을 TinyGPSPlus 로 변경한 후 Libraries 폴더에 둔다.
3. TinyGPS++.h 를 import 하고 사용하면 된다.



Bluetooth 모듈 사용법.
1. 검은색 긴 케이블 - 5V
2. 검은색 짧은 케이블 - 10 pin
3. 흰색 케이블 - 11 pin
4. 회색 케이블 - GND pin
5. TX는 바로 아두이노로 꼽으면 되지만, RX 같은 경우는 3.3V 로 만들어야 하기에 2K 저항과 1K 저항을 브레드보드에 설치후 사용해야 한다.
6. 저항 설치는 2K 저항을 GND 에 해두고, 1K 저항은 아두이노로 연결하는 선로로 만들고, 저항 사이를 모듈의 RX 와 연결한다.


WiFi 모듈 사용법.
1. 폴더 사진에 모듈을 뒤집어 놓은 사진이 있다.
2. | | | | |
	| | | | |