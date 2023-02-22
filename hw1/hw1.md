Домашнее задание 1


<h3>DragonFly</h3>
DragonFly это по-сути Redis, но быстрее и удобнее. Как и в Redis'е, DragonFly жертвует доступностью (availability), оставляя согласованность и partition tolerance. Таким образом, это **CP**.

<h3>ScyllaDB</h3>
Окей, ScyllaDB это по-сути Cassandra на C++. Тут выбор идет в пользу доступности и partition tolerance, а уровень согласованности [может быть настроен](https://teddyma.gitbooks.io/learncassandra/content/about/the_cap_theorem.html). Таким образом, это **AP**.

<h3>ArenadataDB</h3>
ArenadataDB это русский форк Greenplum. По-сути это Postgres с массивно-параллельной архитектурой, таким образом это **CA**.