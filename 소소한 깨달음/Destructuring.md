# Destructuring



```javascript


const student = {
  name: '홍길동',
  age: 99,
}
Object.entries(student).forEach(items => {
  const [key, value] = items // ['name', '홍길동']
  console.log(key, value)
})



// 2. 
Object.entries(student).forEach(([key, value]) => {
  console.log(key, value)
})
```

