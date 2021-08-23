# امثلة برمجية


```
document.location = document.location.hash.slice(1);
```
exploit : http://vulnerable/page.html#https://www.attacker.com/


```
const rootDiv = document.getElementById('root');
const hash = decodeURIComponent(location.hash.substr(1));
rootDiv.innerHTML = hash;
```
exploit :http://vulnerable/page.html#<img onerror='alert(1); src='invalid-image' />
  
  
  للمزيد من الامثلة 
  
 - [Javascript](https://rules.sonarsource.com/javascript/)
 - [Php](https://rules.sonarsource.com/php)
 - [python](https://rules.sonarsource.com/python)
 - [More](https://rules.sonarsource.com/)
