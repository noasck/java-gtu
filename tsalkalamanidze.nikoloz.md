```diff
- 30/30. Сдавайте лабы вовремя. Не делайте лишь бы сдать,
+ ВЫБИРАЙТЕ ИНТЕРЕСНЫЕ ДЛЯ ВАС ЗАДАЧИ.
```

# Java Mid-Term Exam

**Student:** ცალქალამანიძე ნიკოლოზ

**Student ID:** 1775958

**Cheating detected:** Yes

## Task 12

### Subtask 1

Что такое интерфейс в Java? Могут ли в интерфейсе быть методы с реализацией? Зачем нужны интерфейсы, не достаточно ли абстрактных и обычных классов?

```
интерфейсы это контракт, набор абстрактных методов без реализации только сигнатуры,s, с 8ой джавы была добавлена функция реализации методов default,  интерфейсы нужны  для обхода проблем наследования и для описанния необходимых методов которые должен реализовывать класс ( без привязки реализации)
```

### Subtask 2

Как наследуются методы интерфейса? Как наследовать интерфейс (ключевое слово) и возможно ли наследование нескольких интерфейсов одним классом?

```
класс который имплементирует интерфейс обязан реализовать все методы которые есть в данном интерфесе
 интерфейсы иплементируюутся при
 помощи ключ.слова implement
  каждый класс может имплементировать любое количевство интерфейсов
```


## Task 9

### Subtask 1

Что такое final классы и какая их связь с наследованием?

```
final классы тупиковые классы ветки эволюции их нельзя наследовать
```

### Subtask 2

Разрешено ли множественное наследование в Java и почему?

```
в джаве не разрешенно множественное наследованние для избежания проблем ромбовидного наследования
```

### Subtask 3

Для чего используется ключевое слово super? Как наследуются конструкторы родительских классов в дочерних?

```
конструкторы родительских классов не наследуются, для их вызова исплульзуюется ключевое слово супер которое вызывается родительский конструктор (оно обращяется к родительскому методу)
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
	 User(String username, String passwordHash) {
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
	AdminUser(String username, String passwordHash, int accessLevel) {
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

		// вызвать все методы и поля,
		// которые вы считаете публичными и вывести в stdout;
		System.out.println(admin.checkPassword("hashToTest"));
		System.out.println(admin.getUsername());
        int accesLevelOfAdmin = admin.getAccessLevel();
		System.out.println(accesLevelOfAdmin);
		System.out.println(admin.hasAccess(accesLevelOfAdmin));
	}
}

```

**Output:**

```
false
root
10
true

```


## Task 5

### Subtask 1

Дать определение “поле класса”

```
Поле класса - это параметры (примитивные и косплексные) которые описывают текущее состояние обьекта
```

### Subtask 2

Дать определение “метод класса”

```
Метод класса - описание действий обьекта, функция со своей сигнатурой
```

### Subtask 3

Дать определение "Сигнатура метода" и её составляющие

```
Сигнатура метода класса в Java - это модификаторы доступа, static/non static, а также параметры на ввод и получаемый результат, в сумме сигнатура это параметры определяющие метод без учёта конкретной реализации
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

public String brand;
public int waterLevel;
public int beansLevel;
public int cupsMade =0;

CoffeeMachine (String brand, int waterLevel, int beansLevel){
	this.brand = brand;
	this.waterLevel = waterLevel;
	this.beansLevel = beansLevel;
}

public void makeCoffee(int waterNedeed, int beansNedeed){
	if (waterNedeed <= waterLevel && beansNedeed <= beansLevel){
		waterLevel = waterLevel - waterNedeed;
		beansLevel = beansLevel - beansNedeed;
		cupsMade++;
		System.out.println("cofee" + cupsMade + "made");
	} else {
		System.out.println("not enough beans or  cofee");
	}
}

public void printStatus(){
	System.out.println("cups made " + cupsMade);
	System.out.println("water level " + waterLevel);
	System.out.println("beans level " + beansLevel);
}

public void refillWater(int amount){
	waterLevel = waterLevel + amount;
}

public void refillBeans(int amount){
	beansLevel = beansLevel + amount;
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
cups made 0
water level 1000
beans level 200
cofee1made
cofee2made

cups made 2
water level 650
beans level 175

```
