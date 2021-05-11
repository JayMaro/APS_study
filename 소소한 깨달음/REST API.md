# REST API

MTV에서 T를 클라이언트로 MV를 서버에서 구성

일종의 방법론 => 표준은 아님



RESTful API WEB => 나중에 좀 더 알아보자

=> 클라이언트와 서버를 구분

=> 서버는 단지 데이터만을 전달할 뿐 보여주지 않는다.

=> 서버로 부터 불러온 데이터를 클라이언트에서 가공해서 보여줌



URL은 정해진 static

URI는 Dynamic



1. URI를 통해 Resource를 표현하는데 계층구조를 잘 알도록(표현하도록) 해야한다.

2. 행위는 httpmethod로 만든다 => URI에 쓰지 않는다. GET, POST, PUT, DELETE



1. 자원(Resource) : URI로 표현한다.
   - 계층구조를 잘 맞춰서 표현한다.
2. 행위(Methods) : HTTP Methods로 자원의 행위를 표현한다.
   - GET, POST, PUT, DELETE
3. 표현(Representations) : JSON의 형태로 데이터를 표현한다.