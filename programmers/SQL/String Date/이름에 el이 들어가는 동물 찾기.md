
```MYSQL
select animal_id, name
from animal_ins
where animal_type = "DOG" and name like("%EL%")
order by name;
```