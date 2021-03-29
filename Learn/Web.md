웹 표준

WHATWG



JSFiddle



### HTML

스타일 가이드 지키기

속성과 속성값은 공백 No

쌍따옴표 사용



웹에 대한 검색어 뒤쪽에 MDN붙여서 검색



시멘틱 태그 -> div와 동일하지만 의미를 부여

span 인라인요소로 div와 비슷하지만 div는 블록요소



<style>안쪽은 모두 css로 취급
</style>





### CSS

선택자 알아보기

보통 class 선택자만으로 대부분 해결함

margin: 0 auto;

-> 가운데 정렬

콤마로 구분하지 않고 보통 공백으로 구분

마진상쇄



###### Position

absolute

relative: static 위치를 기준으로 이동(상대 위치)
**relative는 기존의 배치는 그대로 두고 요소의 위치만 옮겨진다.**

absolute: static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대 위치)

**absolute는 부모나 조상을 기준으로 이동하고 나머지 요소들은 이 요소를 무시하고 배치된다.**

fixed:  부모 요소와 관계 없이 브라우저를 기준으로 이동( 고정 위치), 스크롤시에도 항상 같은 곳에 위치



z-index => z 축의 값	Position이 static일 때는 못씀

```
<input> 
id: html에서 요소를 식별하기 위해 사용하는 것
type: 어떤 방식으로 사용자한테 입력을 받을지 결정
name: 특정 서버로 전송시 반드시 존재해야 하는 옵션, 데이터의 이름(키)
placeholder: 작성 예시를 나타내는 것
value: 데이터의 값(value)
```



emmet 알아보기

#### Float

```css
.clearfix::after{
   content: "";
   display: block;
   clear: both;
  }
/*float를 실행했을 때 빈공간에 올라오지 않게 임의의 가상요소를 추가*/
```



#### Flexbox

```
- Flex Container를 만들고 그 안에 Flex Item을 집어 넣어 제어
- 축을 기준으로 배열

flex-wrap과 flex-direction는 기본적으로 항상 지정하기 때문에
줄여서 flex-flow로 지정할 수 있다.
ex) flex-flow: cloumn wrap;


모든 항목들은 Flex Container인 부모태그에서 제어하지만
align-self 항목은 각각의 태그 클래스에서 제어한다.

display: flex -> 자식 요소에만 영향이 간다.
자손까지 영향을 주기 위해서는 자식 요소에 다시 한번 flex를 설정하여야 한다.

##################Flex Froggy#####################
```



구조부터 파악하기( 하나씩 접으면서)

```
태그.클래스 {
	특정 태그의 클래스만 스타일 적용
}

:after
::after 동일한 의미
가상의 요소를 정의 할 때 주로 쓰임
```



#### Bootstrap

```
각 브라우저마다 기본 설정이 다르므로 css개발시 초기화부터 시키고 시작
(bootstrap reboot)
자바 스크립트는 script로 body안에 넣어서 선언

CDN을 통해 주소를 불러와서 적용가능

기본적으로 선언되어있는 클래스들을 불러와서 사용하는 형태

Bootstrap Grid system
container, row, column으로 컨텐츠를 배치하고 정렬
1. 12개의 column -> 약수가 많아서
2. 6개의 grid breakpoints
[xs, sm, md, lg, xl, xxl]

gridsystem
공식문서보고 한번씩 실행해보기

layout을 짤 때 gird로 대략적으로 짠 다음
내부 요소에 대해서는 flex box를 이용하면 좋다
```

#### hover

```
마우스를 올렸을 때 어떠한 서식을 지정할 지에 대한 서식
```

ex)a:hover

