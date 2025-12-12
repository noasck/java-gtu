```diff
- 20/30 за экзамен

         wWWWw               wWWWw
   vVVVv (___) wWWWw         (___)  vVVVv
   (___)  ~Y~  (___)  vVVVv   ~Y~   (___)
    ~Y~   \|    ~Y~   (___)    |/    ~Y~
    \|   \ |/   \| /  \~Y~/   \|    \ |/
   \\|// \\|// \\|/// \\|//  \\|// \\\|///
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

```

# Java Mid-Term Exam

**Student:** არუთინოვა ელინა

**Student ID:** 1195903

**Cheating detected:** Yes

## Task 12

### Subtask 1

Что такое интерфейс в Java? Могут ли в интерфейсе быть методы с реализацией? Зачем нужны интерфейсы, не достаточно ли абстрактных и обычных классов?

```
интерфейс в Java - это контракт с набором методов без , реализации , в классе их может быть несколько.да в интерфейсе могут быть методы с реализацией такие ка defalt и ststic. они нужны для множественного наследования поведения , гибкой архитектуры, и ослобления связности
```

### Subtask 2

Как наследуются методы интерфейса? Как наследовать интерфейс (ключевое слово) и возможно ли наследование нескольких интерфейсов одним классом?

```
все методы интерфейса реализуется в классе , который его реализует, с помощью ключевого слова implements, и один класс может реализовать несколько интерфейсов одновременно
```


## Task 9

### Subtask 1

Что такое final классы и какая их связь с наследованием?

```
это клаcс от которого нельзя наследоваться,его нельзя расштрить
```

### Subtask 2

Разрешено ли множественное наследование в Java и почему?

```
нет не разрешено потому что приводит к неоднозначности , непонятно какой метод или реализацию брать из нескольких родительских метадов
```

### Subtask 3

Для чего используется ключевое слово super? Как наследуются конструкторы родительских классов в дочерних?

```
это слово используется для обращения к родительскому классу , чтобы вызвать его конструктор , получить длступ к его полям , методам.конструкторродительского классатвызывается из конструктора дочернего какраз с помощью этого ключевого слово super
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


	String username;


	String passwordHash;


	User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}


	String getUsername() {
		return username;
	}
}

class AdminUser extends User {


	int accessLevel;


	AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}


	boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);

		// вызвать все методы и поля,контрак
		// которые вы считаете публичными и вывести в stdout;
	}
}

```

**Output:**

```

```

```diff
- не попытались. ну ладно. Ну и у Вас есть некоторые неточности в теорке.
+ 0/4
```


## Task 5

### Subtask 1

Дать определение “поле класса”

```
Поле класса хранит состояние обьекта
```

### Subtask 2

Дать определение “метод класса”

```
Метод класса описывает его поведение
```

### Subtask 3

Дать определение "Сигнатура метода" и её составляющие

```
Сигнатура метода класса в Java состоит из имени и пораметров
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
	private string brand;
	private int waterlevel;
	private int beansLevel;
	private int cupMade;

	public CoffeeMachine (string brand,int waterLevel, int beansLevel){
		this.brand=brand;
		this.waterLevel = waterLevel;
		this.beansLevel = beansLevel;
		this.cupMade=0;
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
Compilation error:
C:\Users\Windows\Downloads\exam (2)\.\Main.java:2: error: cannot find symbol
	private string brand;
	        ^
  symbol:   class string
  location: class CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:7: error: cannot find symbol
	public CoffeeMachine (string brand,int waterLevel, int beansLevel){
	                      ^
  symbol:   class string
  location: class CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:9: error: cannot find symbol
		this.waterLevel = waterLevel;
		    ^
  symbol: variable waterLevel
C:\Users\Windows\Downloads\exam (2)\.\Main.java:20: error: cannot find symbol
		machine.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable machine of type CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:21: error: cannot find symbol
		machine.makeCoffee(150, 15);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:22: error: cannot find symbol
		machine.makeCoffee(500, 50);
		       ^
  symbol:   method makeCoffee(int,int)
  location: variable machine of type CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:26: error: cannot find symbol
		machine.refillWater(300);
		       ^
  symbol:   method refillWater(int)
  location: variable machine of type CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:27: error: cannot find symbol
		machine.refillBeans(40);
		       ^
  symbol:   method refillBeans(int)
  location: variable machine of type CoffeeMachine
C:\Users\Windows\Downloads\exam (2)\.\Main.java:29: error: cannot find symbol
		machine.printStatus();
		       ^
  symbol:   method printStatus()
  location: variable machine of type CoffeeMachine
9 errors

```

```diff
- попытались. 1/4.
```
