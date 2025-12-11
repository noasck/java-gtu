```diff
- ну, в сумме 25/30



```

# Java Mid-Term Exam

**Student:** მაგომედოვ ალი

**Student ID:** 1790862

**Cheating detected:** No

## Task 12

### Subtask 1

Что такое интерфейс в Java? Могут ли в интерфейсе быть методы с реализацией? Зачем нужны интерфейсы, не достаточно ли абстрактных и обычных классов?

```
В интерфейсе не могут находится свойства но там находятся действия. Их используют чтобы заменить наследование нескольких классов
```

```diff
- ну какая-то логика есть
```

### Subtask 2

Как наследуются методы интерфейса? Как наследовать интерфейс (ключевое слово) и возможно ли наследование нескольких интерфейсов одним классом?

```
iplements позволяет наследовать интерфейс классом. класс может наследовать несколько интерфейсов в отличии от классов
```


## Task 9

### Subtask 1

Что такое final классы и какая их связь с наследованием?

```
final классы нельзя наследодовать.Поля с final нельзя менять значение и является неизменной - константой
```

### Subtask 2

Разрешено ли множественное наследование в Java и почему?

```
нет это может вызывать ошибка если в классах будут методы с одним и тем же названием. В подобных случаях мы использыем интерфейс
```

```diff
- А в интерфейсах не могут быть методы с одним и тем же названием?
```

### Subtask 3

Для чего используется ключевое слово super? Как наследуются конструкторы родительских классов в дочерних?

```
Конструкторы не наследуются но можно его вызвать в дочерних классах используя super
```

### Subtask 4

Вам даны два класса: <code>User</code> и <code>AdminUser</code>, а также тестирующий класс <code>Main</code>.<br><br>

В коде присутствуют комментарии <code>// TODO: поставить уровень доступа</code>.<br>
Необходимо заменить их на корректные модификаторы доступа (<code>public</code>, <code>protected</code>, <code>private</code>) так, чтобы соблюсти принцип <b>минимального раскрытия</b> (<i>least privilege</i>).<br><br>

<b>Требуется:</b><br>
<ul>
	<li>Скрыть все поля, которые не должны быть доступны напрямую</li>
	<li>Оставить доступ только там, где он действительно необходим</li>
	<li>Учитывать наследование класса <code>AdminUser</code> от <code>User</code></li>
	<li>Обеспечить корректную работу кода в классе <code>Main</code></li>
</ul>

<b>Примечание:</b><br>
В классе <code>Main</code> необходимо вызывать только те поля и методы, которые вы сочли публичными.


```java
class User {

	// TODO: указать модификатор доступа
	private String username;

	// TODO: указать модификатор доступа
	private String passwordHash;

	// TODO: указать модификатор доступа
	public User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	public boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}

	// TODO: указать модификатор доступа
	public String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	// TODO: указать модификатор доступа
	private int accessLevel;

	// TODO: указать модификатор доступа
	public AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}

	// TODO: указать модификатор доступа
	public boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	// TODO: указать модификатор доступа
	public int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);
System.out.println(admin.getUsername());
System.out.println(admin.checkPassword("abc123hash"));
System.out.println(admin.getAccessLevel());


		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
	}
}

```

**Output:**

```
root
true
10

```
``` diff
- это не private.
	// TODO: указать модификатор доступа
	private String username;

	// TODO: указать модификатор доступа
	private String passwordHash;

```


```diff
- ниже не оцениваю, вы могли это вообще не делать - у вас сданы лабы
```


## Task 5

### Subtask 1

Дать определение “поле класса”

```
Поле класса - это часть где находятся переменные (значения) и их тип данных
```

```diff
-не совсем так.
```


### Subtask 2

Дать определение “метод класса”

```
Метод класса - это это законченный фрагмент кода внутри класса. Описывает действие или поведение объекта
```

### Subtask 3

Дать определение "Сигнатура метода" и её составляющие

```
Сигнатура метода класса в Java - это сигнатура это способность писать методы с одинаковыми названиями но с разным количеством и типом данных
```

```diff
- перепутали понятие сигнатура и переопределение. это связанные понятия но разные
```

### Subtask 4

Дано описание предмета из реального мира.<br>
Необходимо реализовать класс <code>CoffeeMachine</code>.<br><br>

<b>Описание класса CoffeeMachine</b><br><br>

<b>Поля</b><br>
<ul>
	<li><code>brand</code> — бренд кофемашины (строка)</li>
	<li><code>waterLevel</code> — текущий уровень воды в миллилитрах (int)</li>
	<li><code>beansLevel</code> — уровень кофейных зёрен в граммах (int)</li>
	<li><code>cupsMade</code> — количество приготовленных чашек кофе (int)</li>
</ul>

<b>Конструктор</b><br>
Принимает:<br>
<ul>
	<li>бренд</li>
	<li>стартовый уровень воды</li>
	<li>стартовый уровень зёрен</li>
</ul>

<b>Методы</b><br><br>

<code>makeCoffee(int waterNeeded, int beansNeeded)</code><br>
Готовит кофе, если хватает ресурсов.<br>
Уменьшает уровень воды и зёрен, увеличивает <code>cupsMade</code>.<br>
Выводит сообщение об успешном приготовлении или об ошибке.<br><br>

<code>refillWater(int amount)</code><br>
Добавляет воду.<br><br>

<code>refillBeans(int amount)</code><br>
Добавляет зёрна.<br><br>

<code>printStatus()</code><br>
Выводит текущие уровни воды, зёрен и количество приготовленных чашек.<br><br>

<b>Разрешено изменять только класс <code>CoffeeMachine</code>.</b>


```java
class CoffeeMachine {

}

public class Main {
	public static void main(String[] args) {
		CoffeeMachine machine = new CoffeeMachine("DeLonghi", 1000, 200);

		machine.printStatus();
		machine.makeCoffee(150, 15);
		machine.makeCoffee(500, 50);

		System.out.println();

		machine.refillWater(300);
		machine.refillBeans(40);

		machine.printStatus();
	}
}

```

**Output:**

```
Compilation error:
C:\Users\GTU-Student\Desktop\Java\.\Main.java:7: error: constructor CoffeeMachine in class CoffeeMachine cannot be applied to given types;
		CoffeeMachine machine = new CoffeeMachine("DeLonghi", 1000, 200);
		                        ^
  required: no arguments
  found:    String,int,int
  reason: actual and formal argument lists differ in length
C:\Users\GTU-Student\Desktop\Java\.\Main.java:9: error: cannot find symbol
		machine.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable machine of type CoffeeMachine
C:\Users\GTU-Student\Desktop\Java\.\Main.java:10: error: cannot find symbol
		machine.makeCoffee(150, 15);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-Student\Desktop\Java\.\Main.java:11: error: cannot find symbol
		machine.makeCoffee(500, 50);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-Student\Desktop\Java\.\Main.java:15: error: cannot find symbol
		machine.refillWater(300);
		       ^
  symbol:   method refillWater(int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-Student\Desktop\Java\.\Main.java:16: error: cannot find symbol
		machine.refillBeans(40);
		       ^
  symbol:   method refillBeans(int)
  location: variable machine of type CoffeeMachine
C:\Users\GTU-Student\Desktop\Java\.\Main.java:18: error: cannot find symbol
		machine.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable machine of type CoffeeMachine
7 errors

```

```diff



