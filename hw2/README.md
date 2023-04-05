Файл fulfill_db.py заливает датасет в базу и еще догенерирует данных.

<h3>CRUD-запросы</h3>

<h4>Чтение:</h4>
1) Найдем клиента по customer_id:  
```db.customers.findOne({customer_id: 1})```    
Результат (90 мс):

```
{
  _id: ObjectId("642d85ee2b4558b56194ed9c"),
  customer_id: 1,
  sex: 'Male',
  age: 19,
  annual_income: 15,
  spending_score: 39
}
```
  

2) Посмотрим на макс и мин annual_income и spending_score:

```
db.customers.aggregate([
    {
      $group: {
        _id: '$item',
        min_annual_income: { $min: '$annual_income' },
        max_annual_income: { $max: '$annual_income' },
        min_spending_score: { $min: '$spending_score' },
        max_spending_score: { $max: '$spending_score' }
      }
    }
])
```  

Результат (200 мс):

```
[
  {
    _id: null,
    min_annual_income: 15,
    max_annual_income: 137,
    min_spending_score: 1,
    max_spending_score: 99
  }
]
```
*Отсюда я и взял ограничения для генерации*

3) Посмотрим, сколько клиентов младше 30:
```
db.customers.count({age: {$lt: 30}})
```
Результат (125 мс): `55664`

4) Посмотрим, сколько клиентов старше 55:
```
db.customers.count({age: {$lt: 55}})
```
Результат (124 мс): `172178`

5) Посчитаем средний annual_income и spending_score у молодых (младше 30) и старших (старше 55):  
```
db.customers.aggregate([{$match: {age: {$lt: 30}}}, {$group: {_id: '$item', avg_annual_income: {$avg: '$annual_income'}, avg_spending_score: {$avg: '$spending_score'}}}])
db.customers.aggregate([{$match: {age: {gt: 55}}}, {$group: {_id: '$item', avg_annual_income: {$avg: '$annual_income'}, avg_spending_score: {$avg: '$spending_score'}}}])
```
Оба запроса заняли по 130 мс
  
**Добавим индексы**:  
```
db.customers.createIndex({"customer_id": 1}, {unique: true})
db.customers.createIndex({"age": 1})
```

Теперь запросы вроде (1) стали мгновенными (<1 мс) - потому что есть индекс на customer_id,   
запрос (2) занимает столько же времени,  
запросы (3) и (4) стали по 40 мс (в 3 раза быстрее) - потому что есть индекс на age,   
запросы (5) занимают столько же времени.


<h4>Запись:</h4>  
Добавим еще пару клиентов:
```
db.customers.insertOne({customer_id: 200000, sex: "Male", age: 20, "annual_income": 20, "spending_score": 40})
db.customers.insertOne({customer_id: 200001, sex: "Female", age: 55, "annual_income": 25, "spending_score": 45})
```

<h4>Обновление:</h4>  
Увеличим на 1 возраст добавленного мужчины:
```
db.customers.updateOne({customer_id: 200000}, {$inc: {age: 1}})
```
Увеличим доход всех женщин:
```
db.customers.updateMany({sex: "Female"}, {$inc: {annual_income: 10}})
```

<h4>Удалим добавленных вручную:</h4>
```db.customers.deleteMany({customer_id: {$gte: 200000}})```