```diff
- вы изменили этот файл. Он защищен хеш суммой. Какой негодник...
+ 23 из 30.

```
# Java Mid-Term Exam

**Student:** გივიშვილი ზურაბ

**Student ID:** 1613623

**Cheating detected:** Yes ya ne chiteril proga sama viletela

## Task 12

### Subtask 1

Что такое интерфейс в Java? Могут ли в интерфейсе быть методы с реализацией? Зачем нужны интерфейсы, не достаточно ли абстрактных и обычных классов?

```
Интерфейс - это контракт который определяет набор методов и констант которые класс должен реализовать, в интерфейсе описывается что должен уметь объект но не описывается как.

Могут быть методы с реализацией: 1. default-методы - имеют реализацию 2. static-меотды - имеют реализацию 3. private-методы - тоже могут иметь реализцаию но доступны внутри интерфейса. Обычные методы интерйеса реализации не имеют.

Интерфейсы нужны для разрыва жесткой зависимости между классами, поддержки множественного наследования поведения, гибкой архитектуры. Абстрактные классы это частичная реализация
```

### Subtask 2

Как наследуются методы интерфейса? Как наследовать интерфейс (ключевое слово) и возможно ли наследование нескольких интерфейсов одним классом?

```
класс который реализует интерфейс, обязан реализовать все его абстрактные методы, если сам не является абстрактным.default - методы наследуются автоматически. если есть конфликт, класс обязан переопределить этот меод самостоятельно. интерфейсы наследуются с помощью extends, класс реализует интерфейс с помощью implements, возможно наследование нескольких интерфейсов одним классом. у класса может быть только один родитель класс но сколько угодно интерфейсов
```


## Task 9

### Subtask 1

Что такое final классы и какая их связь с наследованием?

```
final класс - это класс который нельзя наследовать. final полностью запрещает наследование, то есть не дает изменить поведение класса через наследника.
```

### Subtask 2

Разрешено ли множественное наследование в Java и почему?

```
множественное наследование классов - запрещено, потому что существует проблема неоднозначного наследования. но множественное наследование интерфейсов разрешено
```

### Subtask 3

Для чего используется ключевое слово super? Как наследуются конструкторы родительских классов в дочерних?

```
super используется для обращения к членам родительского класса. с его помощью можно обращаться к полям родителя, скрытыми полями дочернего класса, вызывать методы родителя , вызывать конструктор родительского класса. конструкторы не наследуются. каждый класс имеет свои собственные конструкторы, но дочерний класс обязательно должен вызвать какойто конструктор родителя
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
	String username;

	// TODO: указать модификатор доступа
	String passwordHash;

	// TODO: указать модификатор доступа
	User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	// TODO: указать модификатор доступа
	boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}

	// TODO: указать модификатор доступа
	String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	// TODO: указать модификатор доступа
	int accessLevel;

	// TODO: указать модификатор доступа
	AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}

	// TODO: указать модификатор доступа
	boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	// TODO: указать модификатор доступа
	int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);

		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
	}
}

```

**Output:**

```

```
```diff
- даже не попытались
```

## Task 5

### Subtask 1

Дать определение “поле класса”

```
Поле класса - это переменная обьявленная внутри класса, но вне методов и конструкторов
```

```diff
- такое себе
```

### Subtask 2

Дать определение “метод класса”

```
Метод класса - это функция обьявленная внутри класса которое описывает поведение обьектов этого класса
```

### Subtask 3

Дать определение "Сигнатура метода" и её составляющие

```
Сигнатура метода класса в Java - это часть обьявления метода которая включает имя метода и список параметров
```

```diff
- такое себе тоже
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
String brand;
int waterlevel;
int beansLevel;
int waterLevel;
int cupsMade;

public CoffeeMachine(String brand, int waterLevel, int beansLevel) {
	this.brand = brand;
	this.waterLevel=waterLevel;
	this.beansLevel=beansLevel;
	this.cupsMade=0;
}

public void makeCoffee(int waterNeeded, int beansNeeded) {
	if (waterLevel >= waterNeeded && beansLevel >= beansNeeded) {
		waterLevel -= waterNeeded;
		beansLevel -= beansNeeded;
		cupsMade++;
		System.out.println("Кофе успешно приготовлен");
	} else {
		System.out.println("Недостаточно ресурсов");
	}
}

public void refillWater(int amount) {
	waterLevel += amount;
}

public void refillBeans(int amount) {
	beansLevel += amount;
}

public void printStatus (){
	System.out.println("---Статус" + brand + "---");
	System.out.println("Вода: " + waterLevel + "мл");
	System.out.println("Зерна: " + beansLevel + "г");
	System.out.println("Чашек: " + cupsMade);
    }
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
---������DeLonghi---
����: 1000��
�����: 200�
�����: 0
���� ������� �����������
���� ������� �����������

---������DeLonghi---
����: 650��
�����: 175�
�����: 2

```
