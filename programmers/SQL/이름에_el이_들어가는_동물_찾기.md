## 이름에 el이 들어가는 동물 찾기

```MYSSQL
select animal_id, name
from animal_ins
where animal_type = "DOG" and name like("%EL%")
order by name;
```