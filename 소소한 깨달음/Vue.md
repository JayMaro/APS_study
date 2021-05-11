vue



vue의 목적은 HTML 문서를 만드는 것이다!



불러오기, 등록하기, 사용하기



webpack 은 쪼개진 컴포넌트 들을 모아주는 작업을 해주는 역할 -> dist를 만든다.

Node.js를 이용해서 이루어 진다. -> 개발 환경을 구축하기 위해 Node.js 필요

npm run build를 통해 만들어진 dist 파일이 배포가 되는 것



main.js

```
webpack이 빌드를 시작할 때 가장 먼저 불러오는 Entry point(시작점)
단일파일에서 DOM과 연결했던 것과 동일한 작업들이 이루어짐
Vue의 전역에서 사용할 수 있는 모듈들을 등록 가능
```



package.json

```
scripts - 사용할 명령어 스크립트
dependencies - 개발환경 + 배포환경에서 사용할 모듈들
devdependencis - 개발환경에서 사용할 모듈들 requirement.txt 와 하는 역할이 같다.

```

pakage-lock.json

```
배포환경에서 정확히 동일한 환경(종속성)을 유지해야함 -> 그것을 도와주는 것!
개발과정에서 의존성 패키지 충돌을 방지
```



app.vue

```
최상위 컴포넌트
```



dist

```
배포 되는 파일들
```



src

```
프로젝트를 구성하는 리소스들
```



emit -> 자식 컴포넌트에서 원하는 시점에 원하는 이벤트를 발생시킬 수 있다.(HTML 이벤트가 아닌 커스텀 이벤트)





MVVM 모델

Vue.js를 쓰는 이유

CSR, SSR

SEO 검색엔진 최적화

https://kr.vuejs.org/v2/guide/index.html

https://kr.vuejs.org/v2/api/index.html#%EC%98%B5%EC%85%98-%EB%8D%B0%EC%9D%B4%ED%84%B0



vue methods에서 화살표 함수를 못 쓰는 이유
vue에서는 항상 this가 vue 객체를 가르킨다. <- 화살표 함수를 쓰면 window 객체를 가르킴



```
methods 아래 작성되는 함수들은 다 function 키워드

함수로 작성되는 속성들은 다 function 키워드

나머지 다 arrow function
```



function 함수 => this가 실행 컨텍스트를 가르킨다.(함수를 실행하는 객체)

arrow 함수(lexical scope) => 작성하고 있는 함수의 this를 따라간다.

directive



v-bind Object일 때 동작하는 것 알아보기



API_KEY 값은 로컬 개발환경에서는 .env.local 파일에서 저장하고 불러온다.

배포 환경에서는 환경변수로 설정해서 불러온다.



bootstrap에서는 index.html에 넣는다





