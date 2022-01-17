## NULL 처리하기

```MYSSQL
select animal_type, ifnull(name, "No name"), sex_upon_intake
from animal_ins
order by animal_id;

select animal_type, if (name is null, "No name", name), sex_upon_intake
from animal_ins
order by animal_id;
```