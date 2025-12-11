```diff
- 30/30
```

# Java Mid-Term Exam

**Student:** პრიკუპეც არტემიი

**Student ID:** 1034280

**Cheating detected:** No

## Task 4

### Subtask 1

Что такое инкапсуляция (обе части определения)?

```
Инкапсуляция - это один из ключевых механизмов и принципов объектно-ориентированного программирования.
Она включает в себя:
1. Сокрытие внутренней логики класса и пакета.
2. Объединение внутренней логики класса и пакета.
```

### Subtask 2

Что такое модификаторы доступа? Зачем они нужны? Перечислить модификаторы доступа и их назначение.

```
Модификаторы доступа - это механизм Java для ограничения доступа к методам и полям класса.

public - модиифкатор доступа, означающий, что метод или поле может быть вызван извне класса, в том числе из других пакетов.
private - модификатор доступа, означающий, что метод или поле может быть вызван только внутри класса.
package-private - стандартный (неявно применяется по умолчанию) модификатор доступа, означающий, что метод или поле может быть вызван извне класса, но только в рамках текущего пакета.
protected - модификатор доступа, означающий, что метод или поле может быть вызван только внутри класса, либо из его наследников.
```

### Subtask 3

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

	// В теории и private, и protected тут могут быть применимы на эти 2 поля.
	// Обе практики встречаются, но раз AdminUser даже getter'ы не применяет к этим полям, то склоняемся к private для least privilege.
	// Ну и в сообществе Java, в отличие, от, например TypeScript, в целом принято использовать геттеры и сеттеры всегда,
	// практически всегда строго запрещая прямой доступ к полям, т.к. в геттерах и сеттерах можно задавать дополнительное поведение при получении/изменении поля.

 	private String username;

	private String passwordHash;

	// Формально класс User сам по себе может оказаться полезным как public. Оба модификаторы тут применимы.
	// Но по принципу минимального раскрытия оставляем его protected чтобы он остался доступным только в AdminUser.
	protected User(String username, String passwordHash) {
		this.username = username;
		this.passwordHash = passwordHash;
	}

	public boolean checkPassword(String hash) {
		return passwordHash.equals(hash);
	}

	public String getUsername() {
		return username;
	}
}

class AdminUser extends User {

	private int accessLevel;

	public AdminUser(String username, String passwordHash, int accessLevel) {
		super(username, passwordHash);
		this.accessLevel = accessLevel;
	}

	public boolean hasAccess(int requiredLevel) {
		return accessLevel >= requiredLevel;
	}

	public int getAccessLevel() {
		return accessLevel;
	}
}

public class Main {
	public static void main(String[] args) {

		AdminUser admin = new AdminUser("root", "abc123hash", 10);

		// Показываем username админа
		System.out.println("Admin username: " + admin.getUsername());

		// Проверяем правильный ли мы передаем хэш пароля для этого админа
		System.out.println("Is password hash '345' correct for current user? Answer: " + admin.checkPassword("345"));

		// Показываем уровень доступа админа. Может пригодиться для общей сводки, не только для проверки доступа, которая уже реализована внутри AdminUser.
		System.out.println("Admin access level: " + admin.getAccessLevel());

		// Показываем имеет ли админ доступ к ресурсу с необходимым уровнем 15:
		System.out.println("Does admin has access to resource with required level 15? Answer: " + admin.hasAccess(15));
	}
}
// У меня не запустился код, поэтому напрямую проверить не смог, т.к. на Mac оно не дает доступа для этого.
```

**Output:**

```
Internal error: Cannot run program "/Users/gran/Downloads/exam/openjdk/bin/javac.exe" (in directory "."): error=13, Permission denied
```

```diff
- pozor.
 	private String username;

	private String passwordHash;
+ а чего оно private? ну следую логике у админа же тоже есть пароль:)
```


## Task 6

### Subtask 1

Дать определение понятию “конструктор класса” в java. Что такое конструктор по умолчанию?

```
Конструктор класса в Java - это стандартный метод для создания экземпляра класса (=объекта). Он существует по умолчанию, но так же может быть переопределен.
Пример: User user = new User("some-user", "some-password-hash"); // здесь мы вызываем конструктор, передавая 2 поля.
Конструктор всегда существует у класса, но он может быть недоступен для вызова извне, если мы работаем с abstract class. Тогда он будет доступен для вызова через super только в тех классах, которые реализуют данный класс.
Внутри конструктора = инициализация класса. Внутри него могут быть заданы стартовые значения для полей класса из аргументов и могут быть произведены и иные стартовые действия.
Конструктор по умолчанию (default constructor) - стандартный конструктор класса без аргументов. Существует всегда.
```

### Subtask 2

Почему есть конструктор но нет деструктора? Почему метод finalize никогда не стоит использовать?

```
В Java, в отличие, от, например C++ и некоторых других языков, не используются деструкторы.
В иных языках он используется для явного определения логики которая будет вызвана при терминализации объекта, т.е. в момент завершения его существования.
Метод finalize действительно существует для явного завершения существования объекта, но его нерекомендовано использовать, т.к. Java автоматичесики с помощью GC (Garbage Collector) занимается подчисткой объектов, а если вдруг нужно перед завершением закрыть какие-нибудь процессы, например I/O доступ к классу, или сетевые процессы, то для этого разработчик и так ими явно управляет через .close() и try with в соответствующих методах.
```

### Subtask 3

Наследуются ли конструкторы? Как вызвать конструктор родительского класса?

```
В Java можно наследовать конструктор с помощью вызова метода super() в конструкторе класса-потомка. Он вызывает конструктор родительского класса. В него так же можно передать и аргументы, если родительский конструктор их определил.
Метод super() сам по себе не возвращает экземпляр класса и он доступен только внутри конструктора потомка и только в первой строчке.

Однако метод super() используется не только для вызова конструктора родителя. В методах, помеченных аннотацией @Override() он используется для вызова в первой строчке оригинального метода класса-родителя (но это уже другая тема).
```

### Subtask 4

Дано описание предмета из реального мира.<br>
Необходимо реализовать класс <b>Printer3D</b>.<br><br>

<b>Описание класса Printer3D</b><br><br>

<b>Поля</b><br>
<ul>
	<li><code>model</code> — модель принтера (строка)</li>
	<li><code>filamentLevel</code> — текущий уровень филамента в граммах (int)</li>
	<li><code>powerLevel</code> — уровень заряда принтера в процентах (int)</li>
	<li><code>objectsPrinted</code> — количество напечатанных объектов (int)</li>
</ul>

<b>Конструктор</b><br>
Принимает:<br>
<ul>
	<li>модель принтера</li>
	<li>стартовый уровень филамента</li>
	<li>стартовый уровень заряда</li>
</ul>

<b>Методы</b><br><br>

<code>printObject(int filamentNeeded, int powerNeeded)</code><br>
Печатает объект, если хватает ресурсов.<br>
Уменьшает уровень филамента и заряда.<br>
Увеличивает счётчик <code>objectsPrinted</code>.<br>
Выводит сообщение об успешной печати или об ошибке.<br><br>

<code>refillFilament(int amount)</code><br>
Добавляет филамент.<br><br>

<code>recharge(int amount)</code><br>
Добавляет заряд.<br><br>

<code>printStatus()</code><br>
Выводит текущие уровни филамента, заряд и количество напечатанных объектов.


```java
class Printer3D {
	private String model;
	private int filamentLevel;
	private int powerLevel;
	private int objectsPrinted;

	public Printer3D(String model, int filamentLevel, int powerLevel) {
		this.model = model;
		this.filamentLevel = filamentLevel;
		this.powerLevel = powerLevel;
	}

	public printObject(int filamentNeeded, int powerNeeded) {
		if (this.filamentLevel < filamentNeeded) {
			System.out.println("Недостаточно филамента для печати");
			return; // Лучше вызвать кастомный Exception, но это надо отдельно его прописать
		}

		if(this.powerLevel < powerNeeded) {
			System.out.println("Недостаточно заряда для печати");
			return; // Лучше вызвать кастомный Exception, но это надо отдельно его прописать
		}

		// Заглушка для реального процесса печати (например для обращения к реальному физическму 3д-принтеру). В идеале в try-catch

		this.filamentLevel -= filamentNeeded;
		this.powerLevel -= powerNeeded;
		this.objectsPrinted++;

		System.out.println("Объект успешно напечатан");
	}

	public refillFilament(int amount) {
		this.filamentLevel += amount;
	}

	public recharge(int amount) {
		this.powerLevel += amount;
	}

	public printStatus() {
		System.out.println("Текущий уровень филамента: " + this.filamentLevel + "; Заряд: " + this.powerLevel + "; Напечатано объектов: " this.objectsPrinted);
	}
}

public class Main {
	public static void main(String[] args) {
		Printer3D printer = new Printer3D("Creality Ender 3", 500, 80);

		printer.printStatus();
		printer.printObject(50, 10);
		printer.printObject(200, 40);

		System.out.println();

		printer.refillFilament(100);
		printer.recharge(20);

		printer.printStatus();
	}
}
// У меня не запустился код, поэтому напрямую проверить не смог, т.к. на Mac оно не дает доступа для этого.

```

**Output:**

```
Internal error: Cannot run program "/Users/gran/Downloads/exam/openjdk/bin/javac.exe" (in directory "."): error=13, Permission denied
```


## Task 10

### Subtask 1

Дать определение полиморфизма типов в Java.

```

```

### Subtask 2

Сравнить тип объекта и тип ссылки в Java (Pointer type vs Object type). Подсказка: это имеет отношение к переопределению методов.

```

```

### Subtask 3

Как устроен специальный (параметрический) полиморфизм в джава? Как называется обеспечивающий его механизм

```

```

### Subtask 4

<b>Задача</b><br><br>

Вам дан рабочий класс <code>Main</code> и два класса компонентов:
<code>RenderComponent</code> и <code>PhysicsComponent</code>,
а также пустой базовый класс <code>Component</code>.<br><br>

Код частично работает, но содержит ошибки проектирования и дублирование.<br>
Ваша задача — исправить программу, вынеся общее поведение в базовый класс
<code>Component</code>.<br><br>

<b>Требуется:</b><br><br>

<b>1. Перенести общее в родительский класс</b><br>
В классах <code>RenderComponent</code> и <code>PhysicsComponent</code>
повторяются поля и методы:<br>
<ul>
	<li><code>id</code></li>
	<li><code>enabled</code></li>
	<li><code>priority</code></li>
	<li>методы <code>enable()</code> и <code>disable()</code></li>
	<li>часть логики метода <code>update()</code>
	(например, проверка <code>enabled</code> и уменьшение <code>priority</code>)</li>
</ul>
Вынесите всё общее в базовый класс <code>Component</code>.<br><br>

<b>2. Настроить корректное наследование</b><br>
<ul>
	<li>Класс <code>Component</code> должен иметь конструктор</li>
	<li>В дочерних классах
	(<code>RenderComponent</code>, <code>PhysicsComponent</code>)
	конструктор должен вызывать родительский через <code>super(...)</code></li>
</ul>


```java
public class Main {
    public static void main(String[] args) {
        RenderComponent rc = new RenderComponent("Renderer", true, 5, "Mesh_A");
        PhysicsComponent pc = new PhysicsComponent("Physics", true, 3, 0.98);

        rc.update();
        pc.update();

        System.out.println();

        Component[] components = { rc, pc };

        for (Component c : components) {
            c.disable();
            c.update();
            System.out.println();
        }

        System.out.println(rc.priority);
    }
}

class Component {
}

class RenderComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public String meshName;

    public RenderComponent(String id, boolean enabled, int priority, String meshName) {
        super();
        this.id = id;
        this.enabled = enabled;
        this.priority = priority;
        this.meshName = meshName;
    }

    public void enable() {
        enabled = true;
        System.out.println(id + " enabled");
    }

    public void disable() {
        enabled = false;
        System.out.println(id + " disabled");
    }

    public void update() {
        if (!enabled) {
            System.out.println(id + " is disabled, skipping update");
            return;
        }
        System.out.println(id + " renders mesh " + meshName);
        priority -= 1;
    }
}

class PhysicsComponent extends Component {
    public String id;
    public boolean enabled;
    public int priority;
    public double damping;

    public PhysicsComponent(String id, boolean enabled, int priority, double damping) {
        super();
        this.id = id;
        this.enabled = enabled;
        this.priority = priority;
        this.damping = damping;
    }

    public void enable() {
        enabled = true;
        System.out.println(id + " enabled");
    }

    public void disable() {
        enabled = false;
        System.out.println(id + " disabled");
    }

    public void update() {
        if (!enabled) {
            System.out.println(id + " is disabled, skipping update");
            return;
        }
        System.out.println(id + " applies physics with damping=" + damping);
        priority -= 1;
    }
}

```

**Output:**

```

```
